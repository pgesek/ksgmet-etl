from geojson import dump, Polygon, Feature, FeatureCollection

POMORZE = 'pomorze'
MAZOWSZE = 'mazowsze'
POLUDNIE = 'poludnie'

def generate_geojson(filename, prop_dict, default_props):

    regions = ['shoreline', 'rural', 'rural2', 'mountains']
    region_ids_dict = dict()

    for region in regions:
        with open('data/regions/{region}_ids.txt'.format(region=region),
                  'r') as file:
            lines = file.readlines()
            ids = [int(line.strip()) for line in lines]
            region_ids_dict[region] = ids

    lon_start = 13.236774
    lat_start = 48.802824
    lat_step = lon_step = 0.0378444945891919

    lon_step_count = 325
    lat_step_count = 170

    features = []

    for lon_index in range(lon_step_count):
        for lat_index in range(lat_step_count):
            lon = lon_start + (lon_step * lon_index)
            lat = lat_start + (lat_step * lat_index)

            polygon = Polygon([[(lon, lat), (lon + lon_step, lat), (lon + lon_step, lat + lat_step),
                                (lon, lat + lat_step), (lon, lat)]])

            props = dict(default_props) if default_props else {}
            loc_id = calc_location_id(lon_index, lat_index)
            if loc_id in prop_dict:
                props = dict(prop_dict[loc_id])

            add_region_props(props, loc_id, region_ids_dict)
            add_old_region_props(props, lon_index, lat_index)

            features.append(Feature(geometry=polygon, properties=props))

    collection = FeatureCollection(features)

    with open(filename, 'w') as outfile:
        dump(collection, indent=4, sort_keys=True, fp=outfile)


def calc_location_id(x, y):
    start_pl_locations = 24445
    return start_pl_locations + (170 * x) + y


def add_region_props(props, loc_id, region_ids_dict):
    for region in region_ids_dict:
        region_ids = region_ids_dict[region]
        if loc_id in region_ids:
            props[region] = 1
        else:
            props[region] = 0


def add_old_region_props(props, x, y):
    if 131 < x < 149 and 145 < y < 153:
        props[POMORZE] = 1
    else:
        props[POMORZE] = 0

    if 175 < x < 228 and 106 < y < 117:
        props[MAZOWSZE] = 1
    else:
        props[MAZOWSZE] = 0

    if 154 < x < 178 and 13 < y < 38:
        props[POLUDNIE] = 1
    else:
        props[POLUDNIE] = 0
