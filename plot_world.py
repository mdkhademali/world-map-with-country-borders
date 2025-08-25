import geopandas as gpd
import matplotlib.pyplot as plt

# shapefile path
world = gpd.read_file("ne_110m_admin_0_countries.shp")

# plot
world.plot(edgecolor="orange", facecolor="lightblue")
plt.title("World Map with Country Borders")
plt.show()