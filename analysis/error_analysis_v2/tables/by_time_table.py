from error_analysis_v2.query.by_time_query import ByTimeQuery
from .table_display import TableDisplay
from error_analysis_v2.charts.bar_chart import generate_bar_chart
from .table import Table
from error_analysis_v2.query.by_time_error_restricted_query import ByTimeErrorRestrictedQuery
from specification.hour_spec_list import HourSpecList


class ByTimeTable(Table):
    def __init__(self, field, error_threshold):
        super().__init__(field, error_threshold)

    def execute(self, xlsx_doc, db, db_table, dest_path):
        by_time_query = ByTimeQuery(db=db, table=db_table, field=self.field)

        by_time_res = by_time_query.execute()

        by_time_err_query = ByTimeErrorRestrictedQuery(
            db=db,
            table=db_table,
            error_threshold=self.error_threshold,
            field=self.field
        )

        by_time_err_res = by_time_err_query.execute()

        header_row = [row[HourSpecList.TIME_GROUPER] for row in by_time_res]

        count_row = []
        err_count_row = []
        err_percentage_row = []
        avg_err_row = []
        avg_abs_err_row = []

        for by_time_row, by_time_err_row in zip(by_time_res, by_time_err_res):
            count = int(by_time_row['count'])
            err_count = int(by_time_err_row['count'])

            count_row.append(int(count))
            err_count_row.append(int(err_count))

            percentage = err_count / count * 100.00
            err_percentage_row.append(TableDisplay.print_percentage(percentage))

            avg_err_row.append(float(by_time_row['avg']))
            avg_abs_err_row.append(float(by_time_row['avg_abs']))

        data = dict([
            ('title', 'Pole: ' + self.field),
            ('col_headers', header_row),
            ('row_headers', ['Prognozowana godzina', 'Liczba prognoz',
                             'Liczba blędów bezwzględnie > 2.0', 'Procent błędów',
                             'Średnia błędu', 'Średnia bezwzględna błędu']),
            ('content', [count_row, err_count_row, err_percentage_row,
                         avg_err_row, avg_abs_err_row])
        ])

        xlsx_doc.write_table(data)

        chart_path = dest_path + '\\' + db_table + '_' +\
            self.field + '_percent_of_error_time.png'

        generate_bar_chart(
            legend=tuple(header_row),
            values=[float(percent[:-1]) for percent in err_percentage_row],
            title='Procent błędu dla pola ' + self.field,
            path=chart_path
        )

        xlsx_doc.write_image(
            img_path=chart_path,
            img_width=1024,
            img_height=600,
            img_row_height=500,
            img_num_of_cols=4
        )
