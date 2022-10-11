from cmath import nan
from re import L
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import geopandas as gpd
import folium
import mapclassify as mc

# from pysal.contrib.viz import folium_mapping as fm

st.set_page_config(layout="wide")

# LOAD DATA ONCE
# @st.experimental_singleton
# def load_rawdata():
#     dataset   = pd.read_pickle('../vc_app/data/visualcapital_031022.csv')
#     ch_hexbin = gpd.read_file('../geodata/ch_terrain/ch_slope_2056.gpkg')
#     ch_income = gpd.read_file('../geodata/ch_districts/ch_income_per_commune_2018.gpkg')
#     ch_hexbin = ch_hexbin.assign(slope_median = ch_hexbin._median.astype(np.float32), 
#                                 slope_mean = ch_hexbin._mean.astype(np.float32))
#     return dataset,ch_hexbin,ch_income

def aggBy(df, grp_var):
    #aggreate visual capital and diversity by hexbin
    
    threshold = 100

    dat = (df.groupby(['Agglo_Name',grp_var])['pred']
                .agg(bldg_count   = lambda x: len(x),
                     rich    = lambda x: sum( x > threshold),
                     prob    = lambda x: np.mean( x > threshold),
                     cv      = lambda x: stats.variation(x),
#                      gini    = lambda x: qe.gini_coefficient(x.values),
                     med     = lambda x: np.median(x),
                     avg     = lambda x: np.mean(x),
                     )
          ).reset_index()
    
    #aggreate by net-income
    dat = pd.merge(left=dat, 
                        right= (df.groupby(['Agglo_Name',grp_var])['net_income_ptp'].mean()).
                        reset_index(), 
                        on = ['Agglo_Name',grp_var]
                       )
    #aggreate by proportion greater than local mean
    dat = pd.merge(left=dat, 
                        right= (df.groupby(['Agglo_Name',grp_var])['l_prob'].mean()).
                        reset_index(), 
                        on = ['Agglo_Name',grp_var]
                       )
    return dat
# LOAD DATA ONCE
@st.experimental_singleton
def load_data():
    dataset,ch_hexbin,ch_income = load_rawdata()

    dataset = gpd.read_file('../geodata/ch_pred_res/pred_hexbin_1002222.gpkg', crs = 2056)
    dataset = dataset.loc[dataset.hexbin_id == "Lausanne",:]
    
    if st.session_state['groupby_var'] == 'Hexbins':
        gdf = aggBy(dataset, 'hexbin_id')
    
    if st.session_state['groupby_var'] == 'Communes':
        gdf = aggBy(dataset, 'hexbin_id')
    
    def createGeoHX(df, new_crs):
        df2 = pd.merge(df, ch_hexbin[['slope_median','slope_mean','geometry']].reset_index(), 
                            left_on="hexbin_id", right_on= 'index', how='right')
        df2 =  gpd.GeoDataFrame(df2, geometry= df2.geometry , crs = 2056).dropna()
        
        return df2#.to_crs(new_crs)

    gdf_hxbn = createGeoHX(gdf, 4326)
    return gdf_hxbn
# LOAD DATA ONCE
@st.experimental_singleton
def load_data():
    dataset = gpd.read_file('../vc_app/data/hexbin_visualcapital_031022.gpkg', crs = 2056)
    dataset = dataset.loc[dataset.hexbin_id == "Lausanne",:]
    return dataset#,maxvsh_cols,vaccess_cols,mean_cols,dist_cols,vconfig_cols

# # LOAD DATA ONCE
# @st.experimental_singleton
# def load_data():
#     dataset = gpd.read_file('../vc_app/data/hexbin_visualcapital_031022.gpkg', crs = 2056)
#     dataset = dataset.loc[dataset.hexbin_id == "Lausanne",:]
#     # dataset['hexbin_id'] = dataset['index_left'].astype(str)
#     # dataset = dataset.drop(columns = ['index', 'left', 'bottom','right', 'top'])
#     # dataset = dataset.to_crs(epsg = 4326)

#     fcols = dataset.select_dtypes('float').columns
#     icols = dataset.select_dtypes('integer').columns

#     dataset[fcols] = dataset[fcols].apply(pd.to_numeric).astype(np.float16)
#     dataset[icols] = dataset[icols].apply(pd.to_numeric).astype(np.int16)

#     dataset[['count','rich','bldg_count']] = dataset[['count','rich','bldg_count']].astype(np.int16)
    
#     geo = dataset[['index_left','geometry']].to_json()
#     # dataset = pd.DataFrame(dataset.drop(columns = 'geometry'))
#     # maxvsh_cols    = []#dataset.columns[np.where(dataset.columns == 'Abb7')[0][0]: np.where(dataset.columns == 'sky')[0][0]+1].tolist()
#     # vaccess_cols   = []#dataset.columns[dataset.columns.str.contains('vwa')].tolist()
#     # mean_cols      = []#dataset.columns[dataset.columns.str.contains('mn')].tolist()
#     # dist_cols      = dataset.columns[dataset.columns.str.contains('Sh')].tolist()
#     # vconfig_cols   = dataset.columns[np.where(dataset.columns == 'cmpx_rh')[0][0]: np.where(dataset.columns == 'refuge')[0][0]+1].tolist()

#     return geo, dataset#,maxvsh_cols,vaccess_cols,mean_cols,dist_cols,vconfig_cols


st.sidebar.title("Visual Capital")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How to spatially group buildings?",
    ("Hexbins", "Commune"), key = 'groupby_var'
    )
add_colorbox = st.sidebar.selectbox(
    "Select cmap?",
    ("YlGnBu", 'RdBu'), key = 'cmap_var'
    )

# Using "with" notation
with st.sidebar:
    add_radio = st.selectbox(
        "Choose Attribute",
        ('count', 'rich', 'prob', 'cv', 'gini',
       'med', 'avg', 'net_income_ptp', 'l_prob', 'index', 'left', 'bottom',
       'right', 'top', '_mean', '_median', 'geometry', 'dist2lago',
       'local_slope'), key = 'color_var'
    )


st.sidebar.info(
    """
    A.R. Swietek:
    [GitHub](https://github.com/AdamSwietek) | [Twitter](https://twitter.com/aswietek) | [LinkedIn](https://ch.linkedin.com/in/adamrswietek)
    """
)


# define layout
# c1, c2 = st.columns((2,3))

def getBins(color_var):
    x = df[color_var]
    return [x.min()]+mc.NaturalBreaks(x,5).bins.round(2).tolist()



# get and cache data from API
df = load_data()

# st.write(df.head(100))
# bins = mc.NaturalBreaks(df[st.session_state['color_var']],5).bins
ce, c1, ce, c2, c3 = st.columns([0.1, 0.1, 0.1, 15, 0.07])
with c2:
    m = folium.Map(location=(46.5197,6.6323),zoom_start=10,tiles = "Stamen Terrain")

    if st.session_state['color_var'] is not None: 
        @st.experimental_singleton
        def createMap(color_var, cmap_var):
            # return folium.Choropleth(
            #             geo_data = geo,
            #             name = 'Choropleth',
            #             data = df,
            #             columns = ['index_left',color_var],
            #             key_on = 'feature.properties.index_left',
            #             threshold_scale = getBins(df[color_var]),
            #             fill_color = cmap_var,
            #             fill_opacity = 0.5,
            #             line_opacity = 0,
            #             legend_name = color_var,
            #             smooth_factor=  0
            # )
            return  df.explore(color_var, cmap = cmap_var, 
                        tooltip =['prob','count','slope_median'], 
                        scheme = "NaturalBreaks", m=m
                        )

        # st.write(st.session_state['color_var'], st.session_state['cmap_var'],getBins(st.session_state['color_var']))
        m = createMap(st.session_state['color_var'], st.session_state['cmap_var'])

    map_data = st_folium(m)

# m = gdf.explore(st.session_state['color_var'], scheme = "NaturalBreaks",tiles = "Stamen Terrain", m= m)





# def app():


# app()









# def get_gdf(color_var):
#     gdf2 = read_gdf()

# @st.cache(allow_output_mutation=True)
# def read_gdf():
#     gdf = gpd.read_file('../geodata/ch_pred_res/pred_hexbin_1002222.gpkg')
#     return gdf

# @st.cache(allow_output_mutation=True)
# def getM(gdf,  color_var):
#     m = gdf.explore(color_var, scheme = "NaturalBreaks")
#     return m

# def display_map(df, color_var):

#     map = folium.Map()
    
#     choropleth = folium.Choropleth(
#         geo_data=df,#'../geodata/ch_pred_res/pred_hexbin_1002222.geojson',
#         data=df,
#         columns=['index_left', 'prob'],
#         key_on='feature.properties.state',
#         line_opacity=0.8,
#         highlight=True
#     )
#     choropleth.geojson.add_to(map)

#     # df_indexed = df.set_index('State Name')
#     # for feature in choropleth.geojson.data['features']:
#     #     state_name = feature['properties']['name']
#     #     feature['properties']['population'] = 'Population: ' + '{:,}'.format(df_indexed.loc[state_name, 'State Pop'][0]) if state_name in list(df_indexed.index) else ''
#     #     feature['properties']['per_100k'] = 'Reports/100K Population: ' + str(round(df_indexed.loc[state_name, 'Reports per 100K-F&O together'][0])) if state_name in list(df_indexed.index) else ''

#     # choropleth.geojson.add_child(
#     #     folium.features.GeoJsonTooltip(['name', 'population', 'per_100k'], labels=False)
#     # )
    
#     st_map = st_folium(map, width=700, height=450)

#     # state_name = ''
#     # if st_map['last_active_drawing']:
#     #     state_name = st_map['last_active_drawing']['properties']['name']
#     # return state_name


# def app():
#     #create view indicator options
#     mapping = {"VC": "prob", "Diff": "norm_diff"}
#     color_var = st.radio("Filter", ("VC", "Diff"), format_func=lambda x: mapping[x])
#     #select color var
#     color_var = 'prob'
#     gdf2 = read_gdf()

#     #filter gdf 
#     gdf = gdf2[[color_var, 'geometry']].dropna()

#     m = display_map(gdf, color_var)

#     #create map
#     # Add a title and intro textst.title('Earthquake Data Explorer')
#     # m.to_streamlit()
    
#     # st_map = st_folium()

#     # st.text('Visual Capital')
#     # st_data = st_folium(m)

# st.text('Visual Capital')
# app()


# app()