from error_analysis_v2.docs.sheet import Sheet
from xlsx.xlsx_doc import XlsxDoc
import os


class Doc:
    def __init__(self, tables, db_tables, doc_name):

        self.sheets = [Sheet(
                db='ksgmet-' + db_table,
                db_table=db_table,
                tables=tables
        ) for db_table in db_tables]

        self.doc_name = doc_name

    def execute(self, dest_path):
        xlsx_doc = XlsxDoc()

        for sheet in self.sheets:
            sheet.execute(
                xlsx_doc=xlsx_doc,
                dest_path=dest_path
            )

        os.makedirs(name=dest_path, exist_ok=True)
        xlsx_doc.save(dest_path + '\\' + self.doc_name + '.xlsx')
