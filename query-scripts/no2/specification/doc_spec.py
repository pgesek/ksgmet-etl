from aws.athena_query_builder import AthenaQueryBuilder
from sql.sql_builder import SqlBuilder
from xlsx.xlsx_doc import XlsxDoc
import copy


class DocSpec:
    def __init__(self, db_table, sheet_specs):
        self.db_table = db_table
        self.sheet_specs = sheet_specs

    def execute(self):
        sql_builder = SqlBuilder().with_junk_filter()
        athena_builder = AthenaQueryBuilder().with_db(self.db_table)

        for sheet_spec in self.sheet_specs:
            sheet_spec.execute(copy.copy(sql_builder), athena_builder)

    def write_to_doc(self, dest_path):
        doc = XlsxDoc()

        for sheet_spec in self.sheet_specs:
            sheet_spec.write_to_doc(doc)

        doc.save(dest_path)
