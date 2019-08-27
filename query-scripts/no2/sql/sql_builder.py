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
            self.query += ' WHERE '
        else:
            self.query += ' AND '

        self.query += clause

        return self

    def build(self):
        return self.query
