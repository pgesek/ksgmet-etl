from aws.athena_query_builder import AthenaQueryBuilder
from sql.sql_builder import SqlBuilder
from xlsx.xlsx_doc import XlsxDoc
import copy


class DocSpec:
    def __init__(
            self,
            db_name,
            db_table,
            sheet_specs,
            map_dir,
            use_mocks=False):
        self.db_name = db_name
        self.db_table = db_table
        self.sheet_specs = sheet_specs
        self.map_dir = map_dir
        self.use_mocks = use_mocks

    def execute(self):
        sql_builder = SqlBuilder()\
            .with_junk_filter()\
            .table(self.db_table)

        athena_builder = AthenaQueryBuilder()\
            .build_mocks(self.use_mocks)\
            .with_db(self.db_name)

        for sheet_spec in self.sheet_specs:
            sheet_spec.execute(copy.copy(sql_builder), athena_builder)

    def write_to_doc(self, dest_path):
        doc = XlsxDoc()

        img_dir = self.map_dir + '\\' + self.db_name

        for sheet_spec in self.sheet_specs:
            sheet_spec.write_to_doc(
                doc=doc,
                img_dir=img_dir
            )

        doc_path = dest_path + '\\' + self.db_name + '_analiza.xlsx'

        print('Saving results to: ' + doc_path)

        doc.save(doc_path)
