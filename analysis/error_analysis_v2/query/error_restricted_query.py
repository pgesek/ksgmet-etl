from .query import Query


class ErrorRestrictedQuery(Query):
    def __init__(self, db, table, error_threshold, field):
        super().__init__(db, table)

        self.error_threshold = error_threshold
        self.field = field

    def sql_builder(self):
        return super().sql_builder()\
            .where('ABS({field}_delta) >= {error}'.format(
                field=self.field,
                error=self.error_threshold
                )
            )
