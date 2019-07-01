import geopandas as gpd
import geoplot

rectangles = gpd.read_file('geojson/data/rectangles.json')
europe = gpd.read_file('https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson')

ax = geoplot.polyplot(rectangles, figsize=(16, 8))
ax2 = geoplot.polyplot(europe, ax=ax, figsize=(16, 8))

#plt.savefig("D:\workspace\MGR\\rectangles.png", bbox_inches='tight')

#plot = ax2.plot()
fig = ax2.get_figure()
fig.savefig("D:\\workspace\\MGR\\rectangles.png")
