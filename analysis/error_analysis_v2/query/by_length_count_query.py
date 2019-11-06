from .query import Query


class ByLengthCountQuery(Query):
    def __init__(self, db, table, field):
        super().__init__(db, table)
        self.field = field

    def execute(self):
        sql_builder = super().sql_builder()\
            .fields([
                'COUNT(*) AS count',
                'prediction_length AS prediction_length'
            ])\
            .group_by('prediction_length')\
            .order_by('prediction_length ASC')

        return super()._execute_on_athena(sql_builder.build())
