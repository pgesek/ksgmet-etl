from error_analysis_v2.tables.by_length_table import ByLengthTable
from .doc import Doc


class ByLengthDoc(Doc):
    def __init__(self, error_threshold):
        tables = [ByLengthTable(field=field, error_threshold=error_threshold)
                  for field in ['t2mean2m', 'tmin2m', 'tmax2m']]

        super().__init__(
            tables=tables,
            db_tables=['november', 'may', 'june'],
            doc_name='analiza_bledu_dlugosc'
        )
