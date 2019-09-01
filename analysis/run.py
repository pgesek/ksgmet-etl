from queries.execute_first_query_set import run as run_first_query_set
from queries.execute_second_query_set import run as run_second_query_set
from dotenv import load_dotenv
from maps.delta_map import run as generate_delta_maps
from maps.rectangles_map import run as generate_rectangles_map
from maps.region_map import run as generate_region_map
from maps.geo.generate_geojson_first_analysis import run as generate_geojson_first_analysis
from maps.geo.generate_geojson_second_analysis import run as generate_geojson_second_analysis
from maps.geo.generate_rectangles import run as generate_rectangles


load_dotenv()

#run_first_query_set()
#run_second_query_set('ksgmet-test', 'test')
#generate_delta_maps()
#generate_rectangles_map()
#generate_region_map()
#generate_geojson_first_analysis()
generate_geojson_second_analysis('ksgmet-november', 'november')
#generate_rectangles()
