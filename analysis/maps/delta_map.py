import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt
import os


FIELDS = ['t2mean2m_delta', 'tmax2m_delta', 'tmin2m_delta']
SUFFIXES = ['_avg', '_abs_avg', '_std_dev']

TITLES = {'_avg':  'Średnia delta', '_abs_avg': 'Średnie delta wartości bezwzględnej',
          '_std_dev': 'Odchylenie standardowe'}


def run(map_dir_name, files):

    # europe = gpd.read_file('https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson')
    poland = gpd.read_file('https://gist.githubusercontent.com/filipstachura/391ecb779d56483c070616a4d9239cc7/raw'
                           '/b0793391ab0478e0d92052d204e7af493a7ecc92/poland_woj.json')

    for file in files:
        print('Generating maps for: ' + file)

        geo_file = 'maps/geo/data/{dir_name}/{file}.geojson'\
            .format(
                dir_name=map_dir_name,
                file=file
            )
        data = gpd.read_file(geo_file)

        print('Geo file loaded')

        for field in FIELDS:
            for suffix in SUFFIXES:

                prop = field + suffix

                print('Generating map for: ' + prop)

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
                                                          title=TITLES[suffix]))

                path = 'D:\\workspace\\MGR\\maps\\{dir_name}\\{file}'\
                    .format(dir_name=map_dir_name, file=file)
                os.makedirs(name=path, exist_ok=True)

                fig = ax.get_figure()
                fig.savefig(path + '\\{prop}_ad.png'.format(prop=prop))

                plt.close(fig)

        print('Maps generated')
