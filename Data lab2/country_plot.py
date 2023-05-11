#%%
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import shapely as shp

#%%


#%%
# load the Ukraine data, from this we only need the geometry (multipolygon) to plot
ua = gpd.read_file(r'.\Ukraine\UKR_adm0.shp')
ua_boarder = ua['geometry'][0]

# %%
# load satellite data
modis = gpd.read_file(r'.\MODIS_C6_1_Europe_24h\MODIS_C6_1_Europe_24h.shp')
viirs = gpd.read_file(r'.\J1_VIIRS_C2_Europe_24h\J1_VIIRS_C2_Europe_24h.shp')
suomi_viirs = gpd.read_file(r'.\SUOMI_VIIRS_C2_Europe_24h\SUOMI_VIIRS_C2_Europe_24h.shp')

#%%
# return points in given counrty as list
# input, gpd.dataframe with points and gpd.dataframe of country
def points_in_country(pointsdf,countrydf):
    points = pointsdf['geometry']
    country_boarder = countrydf['geometry'][0]
    mask = [country_boarder.contains(p) for p in list(points)]
    return points[mask]

#%%
# then we can select only the points that are containt in Ukraine from modis
modis_in_ua = points_in_country(modis,ua)

# %%
# plot points from satellite in Ukraine
def plot_points_in_country(pointsdf,countrydf):
    points = points_in_country(pointsdf,countrydf)
    fig,ax = plt.subplots(figsize = (15,15))
    countrydf.plot(ax = ax)
    points.plot(ax = ax, color = 'r')

#%%
# plots the modis data in Ukraine
plot_points_in_country(modis,ua)

# %%
plot_points_in_country(viirs,ua)

# %%
plot_points_in_country(suomi_viirs,ua)
# %%
