from error_analysis_v2.query.count_query import CountQuery
from error_analysis_v2.query.by_length_query import ByLengthQuery
from error_analysis_v2.query.by_length_count_query import ByLengthCountQuery
from .table_display import TableDisplay
from error_analysis_v2.charts.bar_chart import generate_bar_chart
from .table import Table
from itertools import zip_longest
import os


class ByLengthTable(Table):
    def __init__(self, field, error_threshold):
        super().__init__(field, error_threshold)

    def execute(self, xlsx_doc, db, db_table, dest_path):
        count_query = CountQuery(
            db=db,
            table=db_table,
            error_threshold=self.error_threshold,
            field=self.field
        )

        count = count_query.execute()

        by_length_count_query = ByLengthCountQuery(
            db=db,
            table=db_table,
            field=self.field
        )

        by_length_counts = by_length_count_query.execute()

        by_length_query = ByLengthQuery(
            db=db,
            table=db_table,
            error_threshold=self.error_threshold,
            field=self.field
        )

        result = by_length_query.execute(count)

        percentage_of_error_row = []
        for count_row, result_row in zip_longest(by_length_counts, result):
            err_count = float(result_row['count']) if result_row else 0.0
            percentage = TableDisplay.print_percentage(err_count / float(count_row['count']) * 100.00)
            percentage_of_error_row.append(percentage)

        error_count_row = [int(row['count']) for row in result]
        header_row = [row['prediction_length'] + 'h' for row in result]
        avg_row = [float(row['avg']) for row in by_length_counts]
        avg_abs_row = [float(row['avg_abs']) for row in by_length_counts]

        data = dict([
            ('title', 'Pole: ' + self.field),
            ('col_headers', header_row),
            ('row_headers', ['Długość prognozy', 'Liczba błędów > 2.0',
                             'Procent błędów większych niż 2.0', 'Średnia błędów',
                             'Średnia bezwzględna błędów']),
            ('content', [error_count_row, percentage_of_error_row,
                         avg_row, avg_abs_row])
        ])

        xlsx_doc.write_table(data)

        chart_path = os.path.join(dest_path, db_table + '_' + self.field + '_percent_of_error.png')

        os.makedirs(name=dest_path, exist_ok=True)

        generate_bar_chart(
            legend=tuple(header_row),
            values=[float(percent[:-1]) for percent in percentage_of_error_row],
            title='Procent błędu dla pola ' + self.field,
            path=chart_path
        )

        xlsx_doc.write_image(
            img_path=chart_path,
            img_width=1200,
            img_height=600,
            img_row_height=500,
            img_num_of_cols=4
        )
