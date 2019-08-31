class RegionSpec:

    def __init__(self, name, map_dir):
        self.name = name
        self.map_dir = map_dir

    def requires_clause(self):
        return self.name is not None

    def to_in_clause(self):
        if not self.requires_clause():
            return 'TRUE'

        with open(self.map_dir + '\\geojson\\data\\regions\\' + self.name + '_ids.txt') as id_file:
            ids = id_file.read().splitlines()

        id_query_list = ', '.join(ids)

        return 'location IN ( ' + id_query_list + ')'
