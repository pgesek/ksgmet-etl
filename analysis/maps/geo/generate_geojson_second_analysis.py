from maps.geo.generate_geojson import generate_geojson
from aws.athena_query import AthenaQuery
from sql.sql_builder import SqlBuilder
from restrictions.acm_total_percip_restriction import AcmTotalPercipRestriction
import uuid
import os


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


def execute_query(db, table, restrictions):
    fields = ['location AS location', 'COUNT(*) AS count']

    for field in 't2mean2m_delta', 'tmax2m_delta', 'tmin2m_delta':
        fields += [
            'AVG({field}) AS {field}_avg'.format(field=field),
            'AVG(ABS({field})) AS {field}_abs_avg'.format(field=field),
            'STDDEV_POP({field}) AS {field}_std_dev'.format(field=field)
        ]

    sql_builder = SqlBuilder() \
        .fields(fields) \
        .table(table) \
        .with_junk_filter()

    for restriction in restrictions:
        restriction.extend_where_clause(sql_builder)

    sql_builder.group_by('location')

    athena_query = AthenaQuery(
        db=db,
        sql=sql_builder.build(),
        output_key='geojson_v2_' + str(uuid.uuid4())
    )

    return athena_query.execute_and_wait_for_result()


def run(db, table, rain_restriction=None):

    props = dict()

    restrictions = []
    if rain_restriction:
        restrictions.append(AcmTotalPercipRestriction(rain_restriction))

    data = execute_query(db, table, restrictions)

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

    suffixes = ''
    for restriction in restrictions:
        suffixes += restriction.suffix()

    out_dir = 'maps/geo/data/second_analysis' + suffixes
    os.makedirs(name=out_dir, exist_ok=True)

    generate_geojson(out_dir + '/' + db + '.geojson', props, DEFAULT_PROPS)

    print('GeoJSON generated')
