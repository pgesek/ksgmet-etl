class SheetSpec:

    def __init__(self, name, description, region_spec):
        self.name = name
        self.description = description
        self.region_spec = region_spec

    def execute(self, table_specs, sql_builder, athena_query_builder):
        if self.region_spec.requires_clause():
            sql_builder.where(self.region_spec.to_in_clause())

        for table_spec in table_specs:
            table_spec.execute(sql_builder, athena_query_builder)
