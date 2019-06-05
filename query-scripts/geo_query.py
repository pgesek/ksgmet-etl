import psycopg2


class Coordinates:
    def __init__(self, min_x, max_x, min_y, max_y, name):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.name = name

    def query_part(self):
        return 'x >= {min_x} AND x <= {max_x} AND y >= {min_y} AND y <= {max_y}'\
                .format(min_x=self.min_x, max_x=self.max_x, min_y=self.min_y,
                        max_y=self.max_y)


class DateRange:
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description

    def query_part(self):
        if self.x:
            return ' AND prediction_date >= {x} AND prediction_date <= {y}'\
                .format(x=self.x, y=self.y)
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
            return 'All Data'
        else:
            return '{start}h-{end}h'.format(start=self.start, end=self.end)


def execute_query(cur, reg, dt_range, query_field, pred):
    query = ('SELECT COUNT(*), AVG({field}), AVG(ABS({field})) FROM fact_prediction' +\
             ' WHERE {region_query}{date_range_query}{prediction_query}')\
        .format(field=query_field,
                region_query=reg.query_part(),
                date_range_query=dt_range.query_part(),
                prediction_query=pred.query_part())

    print('Executing query: ' + query)

    cur.execute(query)

    row = cur.fetchone()

    print('Data for {region}, period: {period}, field: {field}, prediction: {prediction}'
          .format(region=reg.name, period=dt_range.description, field=query_field,
                  prediction=prediction.description()))

    print('Row count: {count}, AVG: {avg}, ABS AVG: {abs_avg}'
          .format(count=row[0], avg=row[1], abs_avg=row[2]))


# Coordinates come from get_geo_params.sql
POMORZE = Coordinates(131, 149, 145, 153, 'Pomorze')
MAZOWSZE = Coordinates(175, 228, 106, 117, 'Mazowsze')
POLUDNIE = Coordinates(154, 178, 13, 38, 'Południe')

REGIONS = [POMORZE, MAZOWSZE, POLUDNIE]
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

connection = None
cursor = None

try:
    connection = psycopg2.connect(user='postgres',
                                  password='password',
                                  host='127.0.0.1',
                                  port='5432',
                                  database='ksgmet')
    cursor = connection.cursor()

    for region in REGIONS:
        for date_range in DATE_RANGES:
            for field in FIELDS:
                for prediction in PREDICTIONS:
                    execute_query(cursor, region, date_range, field, prediction)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
