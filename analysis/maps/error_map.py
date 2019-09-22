import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt
import os
import math
from shapely.geometry.polygon import Polygon

FIELDS = ['t2mean2m', 'tmax2m', 'tmin2m']


def run(map_dir_name, files):

    # europe = gpd.read_file('https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson')
    poland = gpd.read_file('https://gist.githubusercontent.com/filipstachura/391ecb779d56483c070616a4d9239cc7/raw'
                           '/b0793391ab0478e0d92052d204e7af493a7ecc92/poland_woj.json')

    for file in files:
        print('Generating maps for: ' + file)

        geo_file = 'maps/geo/data/error_analysis/{file}.geojson'\
            .format(
                dir_name=map_dir_name,
                file=file
            )
        data = gpd.read_file(geo_file)

        print('Geo file loaded')

        for field in FIELDS:

            print('Generating map for: ' + field)

            prop = 'error_percentage_' + field

            for row in data.values:
                for val in row:
                    if not isinstance(val, Polygon):
                        if math.isnan(val):
                            raise Exception('L:::')

            ax = geoplot.choropleth(data,
                                    hue=prop,
                                    cmap='YlOrRd',
                                    legend=True,
                                    edgecolor='lightgray',
                                    linewidth=0.0,
                                    scheme='fisher_jenks_sampled')

            ax2 = geoplot.polyplot(poland,
                                   figsize=(24, 16),
                                   ax=ax,
                                   edgecolor='black')

            plt.title('Pole: {field}, {title}'.format(field=field,
                                                      title='Procent błędów > 2.0, pole: '
                                                            + field))

            path = 'D:\\workspace\\MGR\\maps\\{dir_name}\\{file}'\
                .format(dir_name=map_dir_name, file=file)
            os.makedirs(name=path, exist_ok=True)

            fig = ax.get_figure()
            fig.savefig(path + '\\{field}.png'.format(field=field))

            plt.close(fig)

        print('Maps generated')
