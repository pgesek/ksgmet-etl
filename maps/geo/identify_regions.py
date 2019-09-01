import psycopg2
from shapely.geometry import shape, Point
import json

FILES = ['shoreline', 'rural', 'rural2', 'mountains']

LAT_STEP = LON_STEP = 0.0378444945891919

for file in FILES:
    with open('data/regions/{file}.geojson'.format(file=file)) as f:
        js = json.load(f)

    feature = js['features'][0]
    shoreline_polygon = shape(feature['geometry'])

    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user='postgres',
                                      password='password',
                                      host='127.0.0.1',
                                      port='5432',
                                      database='ksgmet')

        cursor = connection.cursor()

        query = 'SELECT id, langitude, longitude FROM dim_location'

        cursor.execute(query)

        data = cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    with open('data/regions/{file}_ids.txt'.format(file=file), 'w') as outfile:
        for row in data:
            db_id = row[0]
            lat = float(row[1])
            lon = float(row[2])

            if shoreline_polygon.contains(Point(lon, lat)) or\
               shoreline_polygon.contains(Point(lon, lat + LAT_STEP)) or\
               shoreline_polygon.contains(Point(lon + LON_STEP, lat)) or\
               shoreline_polygon.contains(Point(lon + LON_STEP, lat + LAT_STEP)):

                outfile.write(str(db_id) + '\n')
