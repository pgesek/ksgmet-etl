class HoursSpec:
    def __init__(self, name, made_on_hour_range, prediction_length_range):
        self.name = name
        self.made_on_hour_range = made_on_hour_range
        self.prediction_length_range = prediction_length_range

    def requires_where_clause(self):
        return self.made_on_hour_range is not None

    def to_where_clause(self):
        return '(prediction_time BETWEEN ' + str(self.made_on_hour_range[0]) +\
               ' AND ' + str(self.made_on_hour_range[1]) + ') AND ' +\
               '(prediction_length BETWEEN ' + str(self.prediction_length_range[0]) +\
               ' AND ' + str(self.prediction_length_range[1]) + ')'
