from .error_restricted_query import ErrorRestrictedQuery
from .hour_list import HourList


class ByTimeErrorRestrictedQuery(ErrorRestrictedQuery):
    def __init__(self, db, table, error_threshold, field):
        super().__init__(db, table, error_threshold, field)

    def execute(self):
        hour_list = HourList()

        sql_builder = super().sql_builder()\
            .fields([
                'COUNT(*) AS count',
                'AVG({field}_delta) AS avg'.format(field=self.field),
                'AVG(ABS({field}_delta)) AS avg_abs'.format(field=self.field),
                hour_list.build_case_list()
            ])\
            .group_by(hour_list.build_group_by())\
            .order_by(hour_list.build_group_by() + ' ASC')

        return super()._execute_on_athena(sql_builder.build())
