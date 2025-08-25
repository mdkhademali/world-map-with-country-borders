## World Map Plot with GeoPandas

This project uses Python and GeoPandas to plot a world map with country borders.

## Requirements

- Python 3.x
- GeoPandas
- Matplotlib

Install required libraries via pip:

```bash
pip install geopandas matplotlib
```

## Files in this Project

- `plot_world.py` — Python script to plot the world map.
- `ne_110m_admin_0_countries.shp` — Shapefile containing world countries.
- `ne_110m_admin_0_countries.shx`
- `ne_110m_admin_0_countries.dbf`
- `ne_110m_admin_0_countries.prj`

Make sure all the shapefile components are in the same folder as `plot_world.py`.

## How to Run

1. Open terminal or command prompt.
2. Navigate to the project folder:

```bash
cd path_to_your_project_folder
```

3. Run the Python script:

```bash
python plot_world.py
```

A window will open showing the world map with **orange country borders** and **light blue faces**.

## Example Python Code

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Shapefile path
world = gpd.read_file("ne_110m_admin_0_countries.shp")

# Plot
world.plot(edgecolor="orange", facecolor="lightblue")
plt.title("World Map with Country Borders")
plt.show()
```

## Screenshots

You can add a screenshot of your map by placing it in this folder and referencing it:

```markdown
![World Map Screenshot](image/image.pngimage.png)
```

## Notes

- Ensure the shapefile and all its associated files (`.shx`, `.dbf`, `.prj`) are in the same directory as the script.
- If you face path issues, use absolute paths instead of relative paths.

© mdkhademali