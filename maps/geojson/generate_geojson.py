from geojson import dump, Polygon, Feature, FeatureCollection


def generate_geojson(filename, prop_dict, default_props):
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

            props = default_props if default_props else {}
            loc_id = calc_location_id(lon_index, lat_index)
            if loc_id in prop_dict:
                props = prop_dict[loc_id]

            features.append(Feature(geometry=polygon, properties=props))

    collection = FeatureCollection(features)

    with open(filename, 'w') as outfile:
        dump(collection, indent=4, sort_keys=True, fp=outfile)


def calc_location_id(x, y):
    start_pl_locations = 24445
    return start_pl_locations + (170 * x) + y
