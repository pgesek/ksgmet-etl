from error_analysis_v2.tables.by_length_table import ByLengthTable
from error_analysis_v2.docs.by_length_sheet import ByLengthSheet
from xlsx.xlsx_doc import XlsxDoc
import os


class ByLengthDoc:
    def __init__(self, error_threshold):
        tables = [ByLengthTable(field=field, error_threshold=error_threshold)
                  for field in ['t2mean2m', 'tmin2m', 'tmax2m']]

        self.sheets = [
            #ByLengthSheet(db='ksgmet-test', db_table='test', tables=tables)
            ByLengthSheet(db='ksgmet-may', db_table='may', tables=tables),
            ByLengthSheet(db='ksgmet-june', db_table='june', tables=tables),
            ByLengthSheet(db='ksgmet-november', db_table='november', tables=tables)
        ]

    def execute(self, dest_path):
        xlsx_doc = XlsxDoc()

        for sheet in self.sheets:
            sheet.execute(
                xlsx_doc=xlsx_doc,
                dest_path=dest_path
            )

        os.makedirs(name=dest_path, exist_ok=True)
        xlsx_doc.save(dest_path + '\\analiza_bledu_dlugosc.xlsx')
