from error_analysis_v2.tables.by_time_table import ByTimeTable
from .doc import Doc


class ByTimeDoc(Doc):
    def __init__(self, error_threshold):
        tables = [ByTimeTable(field=field, error_threshold=error_threshold)
                  for field in ['t2mean2m', 'tmin2m', 'tmax2m']]

        super().__init__(
            tables=tables,
            db_tables=['november', 'may', 'june'],
            doc_name='analiza_bledu_czas'
        )
