import psycopg2
import generate_geojson


DATE_RANGES = [(None, None, 'data/first_analysis/all_data.geojson'),
               (57, 122, 'data/first_analysis/2018-10-27_to_2018-12-31.geojson'),
               (123, 181, 'data/first_analysis/2019-01-01_to_2019-02-28.geojson'),
               (182, 213, 'data/first_analysis/2019-03-01_to_2019-04-01.geojson')]

DEFAULT_PROPS = dict({
    'count': 0,
    't2mean2m_delta_avg': 0.0,
    't2mean2m_delta_abs_avg': 0.0,
    't2mean2m_delta_std_dev': 0.0,
    'tmax2m_delta_avg': 0.0,
    'tmax2m_delta_abs_avg': 0.0,
    'tmax2m_delta_std_dev': 0.0,
    'tmin2m_delta_avg': 0.0,
    'tmin2m_delta_abs_avg': 0.0,
    'tmin2m_delta_std_dev': 0.0
})


def execute_query(cur, date_range):

    query = 'SELECT location, COUNT(*)'

    for field in 't2mean2m_delta', 'tmax2m_delta', 'tmin2m_delta':
        query += ', AVG({field}), AVG(ABS({field})), STDDEV_POP({field})'\
            .format(field=field)

    query += ' FROM fact_prediction'

    if date_range[0]:
        query += ' WHERE prediction_date >= {start} AND prediction_date <= {end}'\
            .format(start=date_range[0], end=date_range[1])

    query += ' GROUP BY location'

    print('Executing query: ' + query)

    cur.execute(query)

    return cur.fetchall()


for dt_range in DATE_RANGES:
    connection = None
    cursor = None

    props = dict()

    try:
        print('Working on date range: ' + dt_range[2])

        connection = psycopg2.connect(user='postgres',
                                      password='password',
                                      host='127.0.0.1',
                                      port='5432',
                                      database='ksgmet')

        cursor = connection.cursor()

        data = execute_query(cursor, dt_range)

        for row in data:
            location = row[0]

            obj_props = dict({
                'count': row[1],
                't2mean2m_delta_avg': float(row[2]),
                't2mean2m_delta_abs_avg': float(row[3]),
                't2mean2m_delta_std_dev': float(row[4]),
                'tmax2m_delta_avg': float(row[5]),
                'tmax2m_delta_abs_avg': float(row[6]),
                'tmax2m_delta_std_dev': float(row[7]),
                'tmin2m_delta_avg': float(row[8]),
                'tmin2m_delta_abs_avg': float(row[9]),
                'tmin2m_delta_std_dev': float(row[10])
            })

            props[location] = obj_props

        print('Generating GeoJSON')

        generate_geojson.generate_geojson(dt_range[2], props, DEFAULT_PROPS)

        print('GeoJSON generated')
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
