from geojson import dumps, Polygon, Feature, FeatureCollection

lat_start = 13.236774
lon_start = 48.802824
lon_step = lat_step = 0.0378444945891919

lat_step_count = 325
lon_step_count = 170

features = []

for lat_index in range(lat_step_count):
    for lon_index in range(lon_step_count):
        lat = lat_start + (lat_step * lat_index)
        lon = lon_start + (lon_step * lon_index)

        polygon = Polygon([[(lat, lon), (lat + lat_step, lon), (lat + lat_step, lon + lon_step),
                           (lat, lon + lon_step), (lat, lon)]])

        features.append(Feature(geometry=polygon))

collection = FeatureCollection(features)

print(dumps(collection, indent=4, sort_keys=True))
