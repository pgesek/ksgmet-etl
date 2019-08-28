from .athena_query import AthenaQuery


class AthenaQueryBuilder:

    def __init__(self):
        self.db = None

    def db(self, db):
        self.db = db

    def build(self, sql, output_key):
        return AthenaQuery(
            db=self.db,
            sql=sql,
            output_key=output_key
        )
