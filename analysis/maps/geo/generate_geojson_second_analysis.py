from maps.geo.generate_geojson import generate_geojson
from aws.athena_query import AthenaQuery
from sql.sql_builder import SqlBuilder
import uuid


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


def execute_query(db, table):

    query = 'SELECT location AS location, COUNT(*) AS count'

    for field in 't2mean2m_delta', 'tmax2m_delta', 'tmin2m_delta':
        query += ', AVG({field}) AS {field}_avg, AVG(ABS({field})) AS {field}_abs_avg,' \
                 ' STDDEV_POP({field}) AS {field}_std_dev'\
            .format(field=field)

    query += ' FROM ' + table

    query += ' WHERE ' + SqlBuilder.CLEANER_CLAUSE

    query += ' GROUP BY location'

    athena_query = AthenaQuery(
        db=db,
        sql=query,
        output_key='geojson_v2_' + str(uuid.uuid4())
    )

    return athena_query.execute_and_wait_for_result()


def run(db, table):

    props = dict()

    data = execute_query(db, table)

    for row in data:
        location = int(row['location'])

        obj_props = dict({
            'count': row['count'],
            't2mean2m_delta_avg': float(row['t2mean2m_delta_avg']),
            't2mean2m_delta_abs_avg': float(row['t2mean2m_delta_abs_avg']),
            't2mean2m_delta_std_dev': float(row['t2mean2m_delta_std_dev']),
            'tmax2m_delta_avg': float(row['tmax2m_delta_avg']),
            'tmax2m_delta_abs_avg': float(row['tmax2m_delta_abs_avg']),
            'tmax2m_delta_std_dev': float(row['tmax2m_delta_std_dev']),
            'tmin2m_delta_avg': float(row['tmin2m_delta_avg']),
            'tmin2m_delta_abs_avg': float(row['tmin2m_delta_abs_avg']),
            'tmin2m_delta_std_dev': float(row['tmin2m_delta_std_dev'])
        })

        props[location] = obj_props

    print('Generating GeoJSON')

    generate_geojson('maps/geo/data/second_analysis/' + db + '.geojson', props, DEFAULT_PROPS)

    print('GeoJSON generated')
