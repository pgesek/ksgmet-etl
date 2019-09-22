from .query import Query


class ByLocationQuery(Query):
    def __init__(self, db, table):
        super().__init__(db, table)

    def execute(self):
        sql_builder = super().sql_builder()\
            .fields([
                'COUNT(*) AS count',
                'location AS location'
            ])\
            .group_by('location')\
            .order_by('location ASC')

        return super()._execute_on_athena(sql_builder.build())
