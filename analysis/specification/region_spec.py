class RegionSpec:

    def __init__(self, name, map_dir, overview_map_path=None):
        self.name = name
        self.map_dir = map_dir
        self.overview_map_path = overview_map_path

    def requires_clause(self):
        return self.name is not None

    def to_in_clause(self):
        if not self.requires_clause():
            return 'TRUE'

        with open('maps/geo/data/regions/' + self.name + '_ids.txt') as id_file:
            ids = id_file.read().splitlines()

        id_query_list = ', '.join(ids)

        return 'location IN ( ' + id_query_list + ')'

    def write_overview_map(self, doc):
        if self.overview_map_path:
            doc.write_image(self.overview_map_path)
