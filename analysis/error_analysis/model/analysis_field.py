class AnalysisField:
    def __init__(self, field, alias, header):
        self.field = field
        self.alias = alias
        self.header = header

    def to_sql_field(self, analysed_field):
        return (self.field + ' AS ' + self.alias).format(field=analysed_field)

    def get_alias(self, analysed_field):
        return self.alias.format(field=analysed_field)
