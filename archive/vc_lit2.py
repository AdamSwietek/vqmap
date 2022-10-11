
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import geopandas as gpd
import folium
import mapclassify as mc

st.set_page_config(layout="wide")


st.sidebar.title("Visual Capital")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Choose Spatial Grouping:",
    ("Commune","Hexbins" ), key = 'groupby_var'
    )
add_colorbox = st.sidebar.selectbox(
    "Change CMap",
    ("YlGnBu", 'RdBu'), key = 'cmap_var'
    )

# Using "with" notation
with st.sidebar:
    add_radio = st.selectbox(
        "Choose Metric Type",
        ('Economic', 'Visual Composition', 'Visual Configuration'), 
        key = 'metric_var'
    )


st.sidebar.info(
    """
    A.R. Swietek:
    [GitHub](https://github.com/AdamSwietek) | [Twitter](https://twitter.com/aswietek) | [LinkedIn](https://ch.linkedin.com/in/adamrswietek)
    """
)
# LOAD DATA ONCE

# st.write(st.session_state['groupby_var'])

# @st.experimental_singleton
# def load_data(grp_by_var):
#     if grp_by_var == 'Hexbins':
#         data = gpd.read_file('../vc_app/data/hexbin_visualcapital_031022.gpkg', crs = 2056)
#     if grp_by_var == 'Commune':
#         data = gpd.read_file('../vc_app/data/commune_visualcapital_031022.gpkg', crs = 2056)
#     return data

# df = load_data(st.session_state['groupby_var'])
# LOAD DATA ONCE
@st.experimental_singleton
def load_hexdata():
    return gpd.read_file('../vc_app/data/hexbin_visualcapital_031022.gpkg', crs = 2056)
@st.experimental_singleton
def load_comdata():
    return gpd.read_file('../vc_app/data/commune_visualcapital_031022.gpkg', crs = 2056)

# get and cache data from API
df_hex = load_hexdata()
df_com = load_comdata()

c1, c2 = st.columns([.1,30])
with c2:

    if st.session_state['metric_var'] == 'Economic':
        sel_cols = df_hex.columns[3:8]
    elif st.session_state['metric_var'] == 'Visual Composition':
        sel_cols = df_hex.columns[3:8]
    elif st.session_state['metric_var'] == 'Visual Configuration':
        sel_cols = df_hex.columns[3:8]
    st.radio("Choose Layer", sel_cols, key = 'color_var', horizontal=True)

    m = folium.Map(location=(46.5197,6.6323),zoom_start=10,tiles = "Stamen Terrain")

    if st.session_state['color_var'] is not None: 
        @st.experimental_singleton   
        def createHexMap(color_var, cmap_var):
    
            return  df_hex.explore(color_var, cmap = cmap_var, 
                        tooltip = list(df_hex.columns[3:8]), 
                        scheme  = "NaturalBreaks", m=m
                        )
        @st.experimental_singleton   
        def createComMap(color_var, cmap_var):
    
            return  df_com.explore(color_var, cmap = cmap_var, 
                        tooltip = list(df_com.columns[3:8]), 
                        scheme  = "NaturalBreaks", m=m
                        )

        if st.session_state['groupby_var'] == 'Hexbins':
            m = createHexMap(st.session_state['color_var'], st.session_state['cmap_var'])
            # createHexMap(st.session_state['color_var'], st.session_state['cmap_var']).add_to(m)

            # map_data = st_folium(m)
        if st.session_state['groupby_var'] == 'Commune':
            m = createComMap(st.session_state['color_var'], st.session_state['cmap_var'])
            # createComMap(st.session_state['color_var'], st.session_state['cmap_var']).add_to(m)
        # createComMap(st.session_state['color_var'], st.session_state['cmap_var']).add_to(m)

    map_data = st_folium(m)#,width=1500, height=900


# st.write(st.session_state['color_var'], st.session_state['cmap_var'], df.head())
st.write(df.head())