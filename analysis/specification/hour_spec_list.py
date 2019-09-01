class HourSpecList:

    LENGTH_GROUPER = 'prediction_length_group'
    TIME_GROUPER = 'prediction_time_group'

    def __init__(self, hour_specs):
        self.hour_specs = hour_specs

    def build_prediction_length_case(self, include_alias=True):
        conditions = ''
        for hour_spec in self.hour_specs:
            if hour_spec.requires_grouping():
                conditions += hour_spec.prediction_length_condition()
                conditions += ' '

        return '(CASE {0} END){1}'.format(
            conditions,
            'AS ' + HourSpecList.LENGTH_GROUPER if include_alias else ''
        )

    def build_prediction_time_case(self, include_alias=True):
        conditions = ''
        for hour_spec in self.hour_specs:
            if hour_spec.requires_grouping():
                conditions += hour_spec.prediction_time_condition()
                conditions += ' '

        return '(CASE {0} END){1}'.format(
            conditions,
            'AS ' + HourSpecList.TIME_GROUPER if include_alias else ''
        )

    def header_list(self):
        return [hour_spec.header() for hour_spec in self.hour_specs]

    def group_by_fields(self):
        return self.build_prediction_time_case(False) + ', ' +\
               self.build_prediction_length_case(False)
