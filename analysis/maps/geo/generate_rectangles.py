from maps.geo.generate_geojson import generate_geojson


def run():
    generate_geojson('data/rectangles.geojson', dict(), dict())
