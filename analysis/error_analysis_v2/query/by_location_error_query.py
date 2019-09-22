from .error_restricted_query import ErrorRestrictedQuery


class ByLocationErrorQuery(ErrorRestrictedQuery):
    def __init__(self, db, table, error_threshold, field):
        super().__init__(
            db=db,
            table=table,
            error_threshold=error_threshold,
            field=field
        )

    def execute(self):
        sql_builder = super().sql_builder()\
            .fields([
                'COUNT(*) AS count',
                'location AS location',
            ])\
            .group_by('location')\
            .order_by('location ASC')

        return super()._execute_on_athena(sql_builder.build())
