from .athena_query import AthenaQuery
from .mock_athena_query import MockAthenaQuery


class AthenaQueryBuilder:

    def __init__(self):
        self.db = None

    def with_db(self, db):
        self.db = db
        return self

    def build(self, sql, output_key):
        # return AthenaQuery(
        return MockAthenaQuery(
            db=self.db,
            sql=sql,
            output_key=output_key
        )
