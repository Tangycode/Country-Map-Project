import cartopy.crs as ct
import matplotlib.pyplot as plt
import cartopy.feature as cf
import numpy as np
dat = {
    "India" : [68.1766, 97.3954, 6.7535, 35.5133],
    "USA" : [-125.0, -66.9346, 24.3963, 49.3844],
    "China" : [73.4994, 134.7755, 18.1977, 53.5609],
    "Brazil" : [-73.9872, -34.7299, -33.7473, 5.2718],
    "Australia" : [113.3389, 153.5695, -43.6346, -10.6682],
    "Canada": [-141.0, -52.6176, 41.6766, 83.1139],
    "Russia": [19.6604, 180.0, 41.1851, 81.8587],
    "South Africa": [16.2817, 32.8939, -34.8192, -22.1266],
     "Germany": [5.8663, 15.0419, 47.2701, 55.0581],
    "Japan": [122.9346, 153.9867, 24.3963, 45.5515]
        }
print(dat)
def yp(dat,country):
    fig = plt.figure(figsize=(7,6))
    a = fig.add_subplot(1,1,1, projection = ct.PlateCarree())
    a.gridlines(linestyle='--', alpha=0.9, linewidth=1, color="black", draw_labels=True)
    e = dat[country]
    a.set_extent(e,crs=ct.PlateCarree())
    a.add_feature(cf.OCEAN)
    a.add_feature(cf.LAKES)
    a.add_feature(cf.COASTLINE)
    a.add_feature(cf.LAND)
    a.add_feature(cf.RIVERS)
    plt.title(f"Map of {country}")
    plt.show()

o = input("Enter a country's name which is specified in the list: ")

if o in dat:
    yp(dat,o)
else:
    print("Country data unavailable")
