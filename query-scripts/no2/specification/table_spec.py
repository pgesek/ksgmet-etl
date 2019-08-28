import uuid


class TableSpec:
    def __init__(self, field, hour_specs):
        self.field = field
        self.hour_specs = hour_specs

        self.results = []

    def field_list(self):
        return [
            'COUNT(*)',
            'AVG({}_delta)'.format(self.field),
            'AVG(ABS{{}_delta))'.format(self.field),
            'STDDEV_POP({})'.format(self.field)
        ]

    def execute(self, sql_builder, athena_query_builder):
        sql_queries = [
            self._build_sql_query(sql_builder, None),
            (self._build_sql_query(sql_builder, hour_spec)
             for hour_spec in self.hour_specs)
        ]

        athena_queries = TableSpec._build_athena_queries(
            sql_queries,
            athena_query_builder)

        self._execute_and_gather_athena_queries(athena_queries)

    def _build_sql_query(self, sql_builder, hour_spec):
        sql_builder.fields(self.field_list())

        if hour_spec:
            sql_builder.where(hour_spec.to_where_clause())

        return sql_builder.build()

    def _execute_and_gather_athena_queries(self, athena_queries):
        for query in athena_queries:
            query.execute()

        query_results = []
        for query in athena_queries:
            query.wait_to_execute()
            row = query.retrieve_result()
            query_results.append(row)

        self.results = query_results

    @staticmethod
    def _build_athena_queries(sql_queries, athena_query_builder):
        athena_queries = []
        for sql_query in sql_queries:
            athena_query = athena_query_builder.build(sql_query, str(uuid.uuid4()))
            athena_queries.append(athena_query)
        return athena_queries
