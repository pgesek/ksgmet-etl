from copy import copy
import uuid
from .field_keys import field_keys


class SheetQueryExecution:
    def __init__(self, fields, hour_spec_list):
        self.fields = fields
        self.hour_spec_list = hour_spec_list

    def execute(self, sql_builder, athena_query_builder):
        sql_queries = [
            self._build_all_data_query(copy(sql_builder)),
            self._build_grouped_query(copy(sql_builder))
        ]

        athena_queries = SheetQueryExecution._build_athena_queries(
            sql_queries=sql_queries,
            athena_query_builder=athena_query_builder
        )

        results = SheetQueryExecution._execute_and_gather_athena_queries(
            athena_queries=athena_queries
        )

        return self._parse_results(results)

    def _field_list(self, with_grouping):
        fields_list = [
            'COUNT(*) AS count'
        ]
        for field in self.fields:
            fields_list += [
                'AVG({0}_delta) AS {0}_delta_avg'.format(field),
                'AVG(ABS({0}_delta)) AS {0}_delta_avg_abs'.format(field),
                'STDDEV_POP({0}_delta) AS {0}_delta_std_dev'.format(field)
            ]
        if with_grouping:
            fields_list += [
                self.hour_spec_list.build_prediction_time_case(),
                self.hour_spec_list.build_prediction_length_case()
            ]
        return fields_list

    def _build_all_data_query(self, sql_builder):
        sql_builder.fields(self._field_list(False))
        return sql_builder.build()

    def _build_grouped_query(self, sql_builder):
        sql_builder.fields(self._field_list(True))
        sql_builder.group_by(self.hour_spec_list.group_by_fields())
        return sql_builder.build()

    def _parse_results(self, results):
        tables = dict()
        for field in self.fields:
            table = []
            for key in field_keys(field):
                table_row = []
                for hours_spec in self.hour_spec_list.hour_specs:
                    row = SheetQueryExecution._find_row(results, hours_spec)
                    val = row.get(key, '0')
                    table_row.append(val)
                table.append(table_row)
            tables[field] = table
        return tables

    @staticmethod
    def _execute_and_gather_athena_queries(athena_queries):
        for query in athena_queries:
            query.execute()

        query_results = []
        for query in athena_queries:
            query.wait_to_complete()
            rows = query.retrieve_result()
            query_results += rows

        return query_results

    @staticmethod
    def _build_athena_queries(sql_queries, athena_query_builder):
        athena_queries = []
        for sql_query in sql_queries:
            athena_query = athena_query_builder.build(sql_query, str(uuid.uuid4()))
            athena_queries.append(athena_query)
        return athena_queries

    @staticmethod
    def _find_row(rows, hours_spec):
        for row in rows:
            if row.get('prediction_length_group', None) == hours_spec.length_header and\
               row.get('prediction_time_group', None) == hours_spec.time_header:
                return row

        return dict()
