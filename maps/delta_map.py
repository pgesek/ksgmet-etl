import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt

FIELDS = ['t2mean2m_delta', 'tmax2m_delta', 'tmin2m_delta']
SUFFIXES = ['_avg', '_abs_avg', '_std_dev']

TITLES = {'_avg':  'Średnia delta', '_abs_avg': 'Średnie delta wartości bezwzględnej',
          '_std_dev': 'Odchylenie standardowe'}

FILES = ['all_data', '2018-10-27_to_2018-12-31',
         '2019-01-01_to_2019-02-28', '2019-03-01_to_2019-04-01']

# europe = gpd.read_file('https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson')
poland = gpd.read_file('https://gist.githubusercontent.com/filipstachura/391ecb779d56483c070616a4d9239cc7/raw'
                       '/b0793391ab0478e0d92052d204e7af493a7ecc92/poland_woj.json')

for file in FILES:
    geo_file = 'geo/data/first_analysis/{file}.geojson.g'.format(file=file)
    data = gpd.read_file(geo_file)

    for field in FIELDS:
        for suffix in SUFFIXES:

            prop = field + suffix

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

            fig = ax.get_figure()
            fig.savefig('D:\\workspace\\MGR\\maps\\first_analysis\\{file}\\{prop}_ad.png'
                        .format(file=file, prop=prop))

            plt.close(fig)
