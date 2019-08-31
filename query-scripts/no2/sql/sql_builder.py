class SqlBuilder:

    def __init__(self):
        self.query = 'SELECT ${fields} FROM ${table}'

    def fields(self, field_list):
        fields = ', '.join(field_list)
        self.query = self.query.replace('${fields}', fields)
        return self

    def table(self, table):
        self.query = self.query.replace('${table}', table)
        return self

    def where(self, clause):
        if 'WHERE' not in self.query:
            self.query += ' WHERE ('
        else:
            self.query += ' AND ('

        self.query += clause
        self.query += ')'

        return self

    def group_by(self, fields):
        self.query += ' GROUP BY ' + fields
        return self

    def with_junk_filter(self):
        self.where('tmin2m_predicted != -999000000 AND tmin2m_actual != -999000000 AND tmin2m_delta < 200 AND ' +
                   'tmax2m_predicted != -999000000 AND tmax2m_actual != -999000000 AND tmax2m_delta < 200 AND ' +
                   't2mean2m_predicted != -999000000 AND t2mean2m_actual != -999000000  AND t2mean2m_delta < 200')
        return self

    def build(self):
        return self.query
