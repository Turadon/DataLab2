#%%
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

#%%


#%%
ua = gpd.read_file(r'.\Ukraine\UKR_adm0.shp')

# %%
firms = gpd.read_file(r'.\MODIS_C6_1_Europe_24h\MODIS_C6_1_Europe_24h.shp')

# %%
# use for selecting points in certain country, doesn't work yet
from geopandas.tools import sjoin
firms_in_ua = sjoin(firms, ua, how = 'left')
firms_in_ua.head()

# %%
fig,ax = plt.subplots(figsize = (15,15))
ua.plot(ax = ax)
firms_in_ua.plot(ax = ax, color = 'r')

# 
minx, miny, maxx, maxy = ua.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)
# %%
