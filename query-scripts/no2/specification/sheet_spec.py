import copy


class SheetSpec:

    def __init__(self, name, description, region_spec, table_specs):
        self.name = name
        self.description = description
        self.region_spec = region_spec
        self.table_specs = table_specs

    def execute(self, sql_builder, athena_query_builder):
        if self.region_spec.requires_clause():
            sql_builder.where(self.region_spec.to_in_clause())

        for table_spec in self.table_specs:
            table_spec.execute(
                sql_builder=copy.copy(sql_builder),
                athena_query_builder=athena_query_builder
            )

    def write_to_doc(self, doc):
        doc.create_sheet(title=self.name, description=self.description)

        for table_spec in self.table_specs:
            table_spec.write_to_doc(doc)
