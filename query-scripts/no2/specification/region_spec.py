class RegionSpec:

    def __init__(self, name):
        self.name = name

    def requires_clause(self):
        return self.name is not None

    def to_in_clause(self):
        if not self.requires_clause():
            return 'true'

        with open('maps/geojson/data/regions/' + self.name + '.txt') as id_file:
            ids = id_file.readlines()

        id_query_list = ', '.join(ids)

        return 'location IN ( ' + id_query_list + ')'
