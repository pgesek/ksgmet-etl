class AcmTotalPercipRestriction:
    def __init__(self, min_value):
        self.min_value = min_value

    def extend_where_clause(self, sql_builder):
        return sql_builder.where(
            'acm_total_percip_actual > ' + str(self.min_value)
        )

    def suffix(self):
        return '_rain_min_' + str(self.min_value)
