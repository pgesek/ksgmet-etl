from sql.sql_builder import SqlBuilder
from aws.athena_query_builder import AthenaQueryBuilder
from uuid import uuid4


class Query:
    def __init__(self, db, table):
        self.db = db
        self.table = table

    def sql_builder(self):
        return SqlBuilder()\
            .with_junk_filter()\
            .table(self.table)

    def _execute_on_athena(self, sql):
        athena_builder = AthenaQueryBuilder()\
            .with_db(self.db)

        athena_query = athena_builder.build(sql, str(uuid4()))

        return athena_query.execute_and_wait_for_result()
