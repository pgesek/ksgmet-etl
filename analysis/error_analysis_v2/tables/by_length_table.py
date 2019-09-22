from error_analysis_v2.query.count_query import CountQuery
from error_analysis_v2.query.by_length_query import ByLengthQuery
from error_analysis_v2.query.by_length_count_query import ByLengthCountQuery
from .table_display import TableDisplay
from error_analysis_v2.charts.bar_chart import generate_bar_chart


class ByLengthTable:
    def __init__(self, field, error_threshold):
        self.field = field
        self.error_threshold = error_threshold

    def execute(self, xlsx_doc, db, table, dest_path):
        count_query = CountQuery(
            db=db,
            table=table,
            error_threshold=self.error_threshold,
            field=self.field
        )

        count = count_query.execute()

        by_length_count_query = ByLengthCountQuery(
            db=db,
            table=table
        )

        by_length_counts = by_length_count_query.execute()

        by_length_query = ByLengthQuery(
            db=db,
            table=table,
            error_threshold=self.error_threshold,
            field=self.field
        )

        result = by_length_query.execute(count)

        percentage_of_error_row = []
        for count_row, result_row in zip(by_length_counts, result):
            percentage = TableDisplay.print_percentage(float(result_row['count']) / float(count_row['count']) * 100.00)
            percentage_of_error_row.append(percentage)

        error_count_row = [int(row['count']) for row in result]
        header_row = [row['prediction_length'] + 'h' for row in result]

        data = dict([
            ('title', 'Pole: ' + self.field),
            ('col_headers', header_row),
            ('row_headers', ['Długość prognozy', 'Liczba', "Omylność"]),
            ('content', [error_count_row, percentage_of_error_row])
        ])

        xlsx_doc.write_table(data)

        chart_path = dest_path + '\\' + table + '_' + self.field + '_percent_of_error.png'

        generate_bar_chart(
            legend=tuple(header_row),
            values=[float(percent[:-1]) for percent in percentage_of_error_row],
            title='Procent błędu dla pola ' + self.field,
            path=chart_path
        )

        xlsx_doc.write_image(chart_path)
