

class ByLengthSheet:
    def __init__(self, db, db_table, tables):
        self.db = db
        self.db_table = db_table
        self.tables = tables

    def execute(self, xlsx_doc, dest_path):
        xlsx_doc.create_sheet(
            title=self.db_table,
            description="Placeholder"
        )

        for table in self.tables:
            table.execute(
                xlsx_doc=xlsx_doc,
                db=self.db,
                table=self.db_table,
                dest_path=dest_path
            )
