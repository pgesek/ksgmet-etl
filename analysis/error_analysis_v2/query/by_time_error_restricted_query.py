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
                hour_list.build_case_list()
            ])\
            .group_by(hour_list.build_group_by())\
            .order_by(hour_list.build_group_by() + ' ASC')

        return super()._execute_on_athena(sql_builder.build())
