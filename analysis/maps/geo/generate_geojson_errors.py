from error_analysis_v2.query.by_location_query import ByLocationQuery
from error_analysis_v2.query.by_location_error_query import ByLocationErrorQuery
from maps.geo.generate_geojson import generate_geojson
import os


DEFAULT_PROPS = dict({
    'count': 0.0,
    'error_count_t2mean2m': 0.0,
    'error_percentage_t2mean2m': 0.0,
    'error_count_tmin2m': 0.0,
    'error_percentage_tmin2m': 0.0,
    'error_count_tmax2m': 0.0,
    'error_percentage_tmax2m': 0.0
})


def run(db, table, error_threshold=2.0):
    geojson_props = dict()

    by_location_query = ByLocationQuery(
        db=db,
        table=table
    )

    result = by_location_query.execute()

    for row in result:
        location = int(row['location'])

        obj_props = dict({
            'count': int(row['count'])
        })

        geojson_props[location] = obj_props

    for field in ['t2mean2m', 'tmin2m', 'tmax2m']:
        by_location_error_query = ByLocationErrorQuery(
            db=db,
            table=table,
            error_threshold=error_threshold,
            field=field
        )

        err_result = by_location_error_query.execute()

        for err_row in err_result:
            location = int(err_row['location'])

            obj_props = geojson_props[location]

            field_err_key = 'error_count_' + field

            obj_props[field_err_key] = float(err_row['count'])

            percentage = obj_props[field_err_key] / obj_props['count'] * 100.00
            obj_props['error_percentage_' + field] = percentage

    print('Generating GeoJSON')

    out_dir = 'maps/geo/data/error_analysis'
    os.makedirs(name=out_dir, exist_ok=True)

    generate_geojson(out_dir + '/' + db + '.geojson', geojson_props, DEFAULT_PROPS)

    print('GeoJSON generated')
