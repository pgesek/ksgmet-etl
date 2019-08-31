from .athena_query import AthenaQuery
from .mock_athena_query import MockAthenaQuery


class AthenaQueryBuilder:

    def __init__(self):
        self.db = None
        self.should_build_mocks = False

    def with_db(self, db):
        self.db = db
        return self

    def build_mocks(self, build_mocks):
        self.should_build_mocks = build_mocks
        return self

    def build(self, sql, output_key):
        if self.should_build_mocks:
            return MockAthenaQuery(
                db=self.db,
                sql=sql,
                output_key=output_key
            )
        else:
            return AthenaQuery(
                db=self.db,
                sql=sql,
                output_key=output_key
            )
