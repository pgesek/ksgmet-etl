class SqlBuilder:

    def __init__(self):
        self.query = 'SELECT ${fields} FROM ${table}'

    def fields(self, *args):
        fields = ','.join([repr(arg) for arg in args])
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

    def add_junk_filter(self):
        self.where('tmin2m != -999000000 AND tmin2m_delta < 200 AND ' +
                   'tmax2m != -999000000 AND tmax2m_delta < 200 AND' +
                   't2mean2m != -999000000 AND t2mean2m_delta < 200')

    def build(self):
        return self.query
