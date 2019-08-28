class HoursSpec:
    def __init__(self, name, made_on_hour_range, prediction_length_range):
        self.name = name
        self.made_on_hour_range = made_on_hour_range
        self.prediction_length_range = prediction_length_range

    def to_where_clause(self):
        return '(prediction_time BETWEEN ' + self.made_on_hour_range[0] +\
               ' AND ' + self.made_on_hour_range[1] + ') AND ' +\
               '(prediction_length BETWEEN ' + self.prediction_length_range[0] +\
               ' AND ' + self.prediction_length_range[1]
