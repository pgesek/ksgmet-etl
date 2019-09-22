from .query import Query


class ByLengthCountQuery(Query):
    def __init__(self, db, table):
        super().__init__(db, table)

    def execute(self):
        sql_builder = super().sql_builder()\
            .fields([
                'COUNT(*) as count',
                'prediction_length as prediction_length'
            ])\
            .group_by('prediction_length')\
            .order_by('prediction_length ASC')

        return super()._execute_on_athena(sql_builder.build())
