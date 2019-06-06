#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font,  Alignment
from openpyxl.utils import get_column_letter


class Coordinates:
    def __init__(self, min_x, max_x, min_y, max_y, name):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.name = name

    def query_part(self):
        if self.min_x:
            return 'x >= {min_x} AND x <= {max_x} AND y >= {min_y} AND y <= {max_y}'\
                    .format(min_x=self.min_x, max_x=self.max_x, min_y=self.min_y,
                            max_y=self.max_y)
        else:
            return ''


class DateRange:
    def __init__(self, start, end, description):
        self.start = start
        self.end = end
        self.description = description

    def query_part(self):
        if self.start:
            return ' AND prediction_date >= {x} AND prediction_date <= {y}'\
                .format(x=self.start, y=self.end)
        else:
            return ''


class Prediction:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def query_part(self):
        if self.start:
            return ' AND prediction_length >= {start} AND prediction_length <= {end}'\
                .format(start=self.start, end=self.end)
        else:
            return ''

    def description(self):
        if self.start:
            return '{start}h-{end}h'.format(start=self.start, end=self.end)
        else:
            return 'All Data'


def execute_query(cur, reg, dt_range, query_field, pred):
    query = ('SELECT COUNT(*), AVG({field}), AVG(ABS({field})) FROM fact_prediction' +
             ' WHERE {region_query}{date_range_query}{prediction_query}')\
        .format(field=query_field,
                region_query=reg.query_part(),
                date_range_query=dt_range.query_part(),
                prediction_query=pred.query_part())
    if query.endswith('WHERE '):
        query = query[:-6]

    query = query.replace('WHERE  AND', 'WHERE')

    print('Executing query: ' + query)

    cur.execute(query)

    row = cur.fetchone()

    print('Data for {region}, period: {period}, field: {field}, prediction: {prediction}'
          .format(region=reg.name, period=dt_range.description, field=query_field,
                  prediction=prediction.description()))

    print('Row count: {count}, AVG: {avg}, ABS AVG: {abs_avg}'
          .format(count=row[0], avg=row[1], abs_avg=row[2]))

    return row


# Coordinates come from get_geo_params.sql
ALL_DATA = Coordinates(None, None, None, None, 'All Data')
POMORZE = Coordinates(131, 149, 145, 153, 'Pomorze')
MAZOWSZE = Coordinates(175, 228, 106, 117, 'Mazowsze')
POLUDNIE = Coordinates(154, 178, 13, 38, 'Południe')

REGIONS = [ALL_DATA, POMORZE, MAZOWSZE, POLUDNIE]
DATE_RANGES = [DateRange(None, None, 'All Data'),
               DateRange(57, 122, '2018-10-27 to 2018-12-31'),
               DateRange(123, 181, '2019-01-01 to 2019-02-28'),
               DateRange(182, 213, '2019-03-01 to 2019-04-01')]
FIELDS = ['t2mean2m_delta', 'tmin2m_delta', 'tmax2m_delta']
PREDICTIONS = [Prediction(None, None),
               Prediction(4, 6),
               Prediction(7, 12),
               Prediction(13, 18),
               Prediction(19, 24),
               Prediction(25, 30),
               Prediction(31, 36),
               Prediction(37, 41)]

BOLD_FONT = Font(bold=True)

connection = None
cursor = None

try:
    connection = psycopg2.connect(user='postgres',
                                  password='password',
                                  host='127.0.0.1',
                                  port='5432',
                                  database='ksgmet')
    cursor = connection.cursor()

    workbook = Workbook()
    sheet = None

    for region in REGIONS:
        if sheet:
            sheet = workbook.create_sheet()
        else:
            sheet = workbook.active

        sheet.title = region.name
        sheet.page_setup.fitToWidth = 1

        x, y = 1, 1

        for field in FIELDS:

            sheet.cell(row=x, column=y, value='Pole ' + field)
            sheet.merge_cells(start_row=x, start_column=y, end_row=x, end_column=y + 5)

            field_row = sheet.row_dimensions[x]
            field_row.font = BOLD_FONT
            field_row.fill = PatternFill('solid', fgColor='FFFF00')

            x += 1
            y = 1

            for date_range in DATE_RANGES:

                # Header
                header = '{} - {}'.format(field, date_range.description)
                header_cell = sheet.cell(row=x, column=y, value=header)
                sheet.merge_cells(start_row=x, start_column=y, end_row=x, end_column=y + len(PREDICTIONS))

                header_cell.font = BOLD_FONT
                header_cell.alignment = Alignment(horizontal='center')

                x += 2

                cell = sheet.cell(row=x, column=y, value='Ilość wierszy prognoz')
                cell.font = BOLD_FONT
                x += 1

                cell = sheet.cell(row=x, column=y, value='Średnia delta')
                cell.font = BOLD_FONT
                x += 1

                cell = sheet.cell(row=x, column=y, value='Średnia delta z abs')
                cell.font = BOLD_FONT

                col = sheet.column_dimensions[get_column_letter(y)]
                col.width = 25

                # Go to data coll
                x -= 3
                y += 1

                for prediction in PREDICTIONS:
                    cell = sheet.cell(row=x, column=y, value=prediction.description())
                    cell.font = BOLD_FONT
                    x += 1

                    data = execute_query(cursor, region, date_range, field, prediction)

                    for val in data:
                        sheet.cell(row=x, column=y, value=val)
                        x += 1

                    # Back up to data coll start and go to the next one
                    y += 1
                    x -= 4

                # Go back to header
                x -= 1
                # Space between date ranges
                col = sheet.column_dimensions[get_column_letter(y)]
                col.fill = PatternFill('solid', fgColor='E0E0E0')
                y += 1

            # New field, 6 = 5 data rows and one space
            x += 6
            y = 1

    workbook.save('D:\\workspace\\MGR\\data.xlsx')

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
