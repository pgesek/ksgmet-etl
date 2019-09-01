import geopandas as gpd
import geoplot
import geoplot.crs as gcrs

rectangles = gpd.read_file('geo/data/rectangles.geojson')
europe = gpd.read_file('https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson')
poland = gpd.read_file('https://gist.githubusercontent.com/filipstachura/391ecb779d56483c070616a4d9239cc7/raw'
                       '/b0793391ab0478e0d92052d204e7af493a7ecc92/poland_woj.json')

ax = geoplot.polyplot(europe, figsize=(24, 16), facecolor='white', edgecolor='black')
ax2 = geoplot.polyplot(rectangles, ax=ax, edgecolor='lightgray')

#plt.savefig("D:\workspace\MGR\\rectangles.png", bbox_inches='tight')

#plot = ax2.plot()
fig = ax2.get_figure()
fig.savefig("D:\\workspace\\MGR\\rectangles.png")
