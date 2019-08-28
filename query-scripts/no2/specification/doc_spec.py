from no2.aws.athena_query_builder import AthenaQueryBuilder
from no2.sql.sql_builder import SqlBuilder


class DocSpec:
    def __init__(self, db_table, sheet_specs, table_specs):
        self.db_table = db_table
        self.sheet_specs = sheet_specs
        self.table_specs = table_specs

    def execute(self):
        sql_builder = SqlBuilder().with_junk_filter()
        athena_builder = AthenaQueryBuilder().db(self.db_table)

        for sheet_spec in self.sheet_specs:
            sheet_spec.execute(sql_builder, athena_builder, self.table_specs)
