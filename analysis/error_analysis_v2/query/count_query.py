from .error_restricted_query import ErrorRestrictedQuery


class CountQuery(ErrorRestrictedQuery):

    def __init__(self, db, table, error_threshold, field):
        super().__init__(db, table, error_threshold, field)

    def execute(self):
        sql_builder = super().sql_builder()\
            .fields(['COUNT(*) as count'])

        result = super().execute_on_athena(sql_builder.build())

        return result[0]['count']
