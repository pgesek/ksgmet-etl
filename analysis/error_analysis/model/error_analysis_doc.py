import os
from copy import copy
from aws.athena_query_builder import AthenaQueryBuilder
from sql.sql_builder import SqlBuilder
from xlsx.xlsx_doc import XlsxDoc


class ErrorAnalysisDoc:
    def __init__(self, analysis_fields, sheets):
        self.analysis_fields = analysis_fields
        self.sheets = sheets

    def execute_and_write(self, target_doc_dir):
        os.makedirs(name=target_doc_dir, exist_ok=True)

        xlsx_doc = XlsxDoc()

        sql_builder = SqlBuilder()\
            .with_junk_filter()

        athena_builder = AthenaQueryBuilder() \
            .build_mocks(False)

        for sheet in self.sheets:
            sheet.execute_and_write(
                analysis_fields=self.analysis_fields,
                sql_builder=copy(sql_builder),
                athena_builder=copy(athena_builder),
                xlsx_doc=xlsx_doc
            )

        doc_path = target_doc_dir + '\\' 'analiza_bledow.xlsx'

        print('Saving results to: ' + doc_path)

        xlsx_doc.save(doc_path)
