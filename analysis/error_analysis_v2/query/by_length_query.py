from .error_restricted_query import ErrorRestrictedQuery


class ByLengthQuery(ErrorRestrictedQuery):
    def __init__(self, db, table, error_threshold, field):
        super().__init__(db, table, error_threshold, field)

    def execute(self, error_item_count):
        sql_builder = super().sql_builder()\
            .fields(
                [
                    'COUNT(*) AS count',
                    'prediction_length AS prediction_length',
                    '(COUNT(*) * 100.00 / {error_count}) AS percentage'
                    .format(error_count=error_item_count)
                ])\
            .group_by('prediction_length')\
            .order_by('prediction_length ASC')

        return super()._execute_on_athena(sql_builder.build())
