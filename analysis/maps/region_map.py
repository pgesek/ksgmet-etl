import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt

REGIONS = ['shoreline', 'rural', 'rural2', 'mountains', 'pomorze',
           'mazowsze', 'poludnie']


def run():
    rectangles = gpd.read_file('geo/data/rectangles.geojson')
    poland = gpd.read_file('https://gist.githubusercontent.com/filipstachura/391ecb779d56483c070616a4d9239cc7/raw'
                           '/b0793391ab0478e0d92052d204e7af493a7ecc92/poland_woj.json')

    for region in REGIONS:
        ax = geoplot.choropleth(rectangles,
                                hue=region,
                                cmap='Purples',
                                legend=False,
                                edgecolor='lightgray',
                                linewidth=0.0)

        ax2 = geoplot.polyplot(poland,
                               figsize=(24, 16),
                               ax=ax,
                               edgecolor='black')

        fig = ax.get_figure()
        fig.savefig('D:\\workspace\\MGR\\maps\\regions\\{region}.png'
                    .format(region=region))

        plt.close(fig)
