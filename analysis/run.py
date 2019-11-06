from queries.execute_first_query_set import run as run_first_query_set
from queries.execute_second_query_set import run as run_second_query_set
from dotenv import load_dotenv
from maps.delta_map import run as generate_delta_maps
from maps.rectangles_map import run as generate_rectangles_map
from maps.region_map import run as generate_region_map
from maps.geo.generate_geojson_first_analysis import run as generate_geojson_first_analysis
from maps.geo.generate_geojson_second_analysis import run as generate_geojson_second_analysis
from maps.geo.generate_rectangles import run as generate_rectangles
from error_analysis.error_analysis_query import run as run_error_analysis
from error_analysis_v2.by_length_error_analysis import run as error_by_length
from error_analysis_v2.by_time_error_analysis import run as error_by_time
from maps.geo.generate_geojson_errors import run as generate_geojson_error_analysis
from maps.error_map import run as generate_error_maps


load_dotenv()

FIRST_ANALYSIS_FILES = [
    'all_data',
    '2018-10-27_to_2018-12-31',
    '2019-01-01_to_2019-02-28',
    '2019-03-01_to_2019-04-01'
]

#generate_rectangles_map()
#generate_region_map()
#generate_geojson_first_analysis()
#generate_geojson_second_analysis('ksgmet-november', 'november', None)
#generate_geojson_second_analysis('ksgmet-may', 'may', None)
#generate_geojson_second_analysis('ksgmet-june', 'june', None)
#generate_geojson_second_analysis('ksgmet-november', 'november', 0.5)
#generate_geojson_second_analysis('ksgmet-may', 'may', 0.5)
#generate_geojson_second_analysis('ksgmet-june', 'june', 0.5)

#generate_delta_maps(
#    map_dir_name='second_analysis',
#    files=['ksgmet-november', 'ksgmet-may', 'ksgmet-june']
#)

#run_first_query_set()
#run_second_query_set('ksgmet-november', 'november', rain_restriction=None)
#run_second_query_set('ksgmet-may', 'may', rain_restriction=None)
#run_second_query_set('ksgmet-june', 'june', rain_restriction=None)
#run_second_query_set('ksgmet-november', 'november', rain_restriction=0.5)
#run_second_query_set('ksgmet-may', 'may', rain_restriction=0.5)
#run_second_query_set('ksgmet-june', 'june', rain_restriction=0.5)


#generate_rectangles()
#run_error_analysis()
#error_by_length()
error_by_time()

#generate_geojson_error_analysis('ksgmet-november', 'november')
#generate_geojson_error_analysis('ksgmet-may', 'may')
#generate_geojson_error_analysis('ksgmet-june', 'june')
#
#generate_error_maps(
#    map_dir_name='error_analysis',
#    files=['ksgmet-november', 'ksgmet-may', 'ksgmet-june']
#)
