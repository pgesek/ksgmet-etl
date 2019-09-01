class HoursSpec:
    def __init__(
            self,
            made_on_hour_range=None,
            prediction_length_range=None,
            length_header=None,
            time_header=None,
            override_header=None):
        self.length_header = length_header
        self.time_header = time_header
        self.made_on_hour_range = made_on_hour_range
        self.prediction_length_range = prediction_length_range
        self.override_name = override_header

    def requires_where_clause(self):
        return self.made_on_hour_range is not None

    def requires_grouping(self):
        return self.requires_where_clause()

    def to_where_clause(self):
        return '(prediction_time BETWEEN ' + str(self.made_on_hour_range[0]) +\
               ' AND ' + str(self.made_on_hour_range[1]) + ') AND ' +\
               '(prediction_length BETWEEN ' + str(self.prediction_length_range[0]) +\
               ' AND ' + str(self.prediction_length_range[1]) + ')'

    def prediction_length_condition(self):
        return 'WHEN prediction_length BETWEEN {0} AND {1} THEN \'{2}\''\
            .format(
                self.prediction_length_range[0],
                self.prediction_length_range[1],
                self.length_header)

    def prediction_time_condition(self):
        return 'WHEN prediction_time BETWEEN {0} AND {1} THEN \'{2}\''\
            .format(
                self.made_on_hour_range[0],
                self.made_on_hour_range[1],
                self.time_header)

    def header(self):
        if self.override_name:
            return self.override_name
        else:
            return self.time_header + ' ' + self.length_header
