from specification.hours_spec import HoursSpec
from specification.hour_spec_list import HourSpecList


class HourList:
    def __init__(self):
        self.specs = HourSpecList(
            [HoursSpec(
                    made_on_hour_range=(hour * 60 + 1, (hour + 1) * 60 + 1),
                    time_header=HourList.header(hour)
            ) for hour in range(0, 23)]
        )

    def build_case_list(self):
        return self.specs.build_prediction_time_case(True)

    def build_group_by(self):
        return self.specs.build_prediction_time_case(False)

    @staticmethod
    def header_list():
        return [HourList.header(hour) for hour in range(0, 23)]

    @staticmethod
    def header(hour):
        return '{hour:02d}:00'.format(hour=hour)
