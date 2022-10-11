# create single dataframe of average values for each variable in dropdown

import pandas as pd
data = pd.read_parquet('../geodata/ch_pred_res/res_july26_220908_wsmooth.parquet.gzip')

import geopandas as gpd
ch_hexbin = gpd.read_file('../geodata/ch_grids/ch_hexbin_1km.gpkg')
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(x = data.FassPktX, y = data.FassPktY), crs = 2056).reset_index(drop = True)
gdf = gpd.sjoin(ch_hexbin[['geometry']],gdf,how='right')

import numpy as np
def getZ(x):
    return ((x-x.mean())/x.std())

gdf['diff'] = np.log(gdf.smoothed/gdf.income_ptp)
gdf['norm_diff'] = getZ(gdf['diff'])

vc_cols = ['norm_diff','smoothed']
maxvsh_cols = data.columns[9:30].tolist()

def genGHX(data, sel_var, func):
    gdf_hxbn = data.groupby(['Agglo_Name','index_left'])[sel_var].apply(func)
    return gdf_hxbn

def mergeGHX(gdf_agg, ch_hexbin, min_pop = 100):
    gdf_agg = gdf_agg.query('count > @min_pop')
    gdf_hxbn = pd.merge(gdf_agg.reset_index(), ch_hexbin.reset_index(), left_on='index_left', right_on= 'index', how='right')
    gdf_hxbn = gpd.GeoDataFrame(gdf_hxbn, geometry= gdf_hxbn.geometry , crs = 2056)
    return gdf_hxbn.to_crs(4326)
    # return gdf_hxbn.dropna()[['prob','med','avg','count','geometry']].to_crs(4326)

df0 = gdf.groupby(['Agglo_Name','index_left'])['smoothed'].count() 
df0.name = 'count'
df1 = genGHX(gdf, vc_cols, func = lambda x: np.mean(x))
df2 = genGHX(gdf, maxvsh_cols, func = lambda x: np.mean(x > 1))*100

gdf_hxbn = pd.concat([df0, df1, df2], axis = 1).round(2)
gdf_hxbn = mergeGHX(gdf_hxbn, ch_hexbin, 100)

gdf_hxbn.to_file('../geodata/ch_pred_res/res_hexbins_20220915.gpkg',   driver = 'GPKG')
gdf_hxbn.to_parquet('../geodata/ch_pred_res/res_hexbins_20220915.parquet.gzip')
