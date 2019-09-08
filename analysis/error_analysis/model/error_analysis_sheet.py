from copy import copy


class ErrorAnalysisSheet:
    def __init__(self, db_name, table_name, description, tables) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.description = description
        self.tables = tables

    def execute_and_write(self, analysis_fields, athena_builder, sql_builder, xlsx_doc):
        xlsx_doc.create_sheet(
            title=self.table_name.capitalize(),
            description=self.description
        )

        sql_builder.table(self.table_name)
        athena_builder.with_db(self.db_name)

        for table in self.tables:
            table.execute_and_write(
                analysis_fields=analysis_fields,
                sql_builder=copy(sql_builder),
                athena_builder=copy(athena_builder),
                xlsx_doc=xlsx_doc
            )
