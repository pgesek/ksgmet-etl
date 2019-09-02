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

FIRST_ANALYSIS_FILES = [
    'all_data',
    '2018-10-27_to_2018-12-31',
    '2019-01-01_to_2019-02-28',
    '2019-03-01_to_2019-04-01'
]

#run_first_query_set()
run_second_query_set('ksgmet-test', 'test')
#generate_delta_maps(
#    map_dir_name='second_analysis',
#    files=['ksgmet-test', 'ksgmet-may', 'ksgmet-november']
#)
#generate_rectangles_map()
#generate_region_map()
#generate_geojson_first_analysis()
#generate_geojson_second_analysis('ksgmet-november', 'november')
#generate_rectangles()
