import folium
import streamlit as st
from streamlit_folium import st_folium

import pandas as pd
import numpy as np
import geopandas as gpd
import mapclassify as mc

st.set_page_config(layout="wide")

@st.experimental_singleton
def get_data():
    dat_hex = gpd.read_file('../vc_app/visuapcapital/data/hexbin_visualcapital_031022.gpkg', crs = 2056)
    dat_com = gpd.read_file('../vc_app/visuapcapital/data/commune_visualcapital_031022.gpkg', crs = 2056)
    return dat_hex, dat_com

dat_hex, dat_com = get_data()
# Using "with" notation-------------------------
with st.sidebar:
    st.sidebar.title("VC : Visual Capital")

    add_selectbox = st.sidebar.selectbox(
    "Choose Spatial Grouping:",
    ("Commune","Hexbins" ), key = 'groupby_var'
    )
    add_colorbox = st.sidebar.selectbox(
        "Change CMap",
        ("YlGnBu", 'RdBu'), key = 'cmap_var'
        )
    add_radio = st.selectbox(
        "Choose Metric Type",
        ('Economic', 'Visual Composition (coming soon)', 'Visual Configuration (coming soon)'), 
        key = 'metric_var'
    )


@st.experimental_memo
def sel_data(grp_by):
    if grp_by == 'Hexbins':
        dat = dat_hex
        form_cols = np.array(['net_income_ptp','bldg_count','slope_median','slope_mean'])
    elif grp_by == 'Commune':
        dat = dat_com
        form_cols = np.array(['net_income_ptp','bldg_count'])

    dat = dat#.loc[dat.Agglo_Name == 'Lausanne']#.to_crs(4326)
    vc_cols = np.array(['l_prob','avg','med','rich','prob','cv'])
    return dat,form_cols,vc_cols

df,form_cols,vc_cols = sel_data(st.session_state['groupby_var'])

form_var_options = {
    'l_prob': "% Local High VC",
    'avg' : "Average VC",
    'med':'Median VC',
    'rich': "Count of High VC",
    'prob': "% Global High VC",
    'cv' : "Disparity of VC",
    'net_income_ptp': "Net-Income PTP",
    'bldg_count': "Urban Intensity",
    'slope_median': 'Median Terrain Slope',
    'slope_mean': 'Average Terrain Slope'

}
st.sidebar.selectbox("Urban Form Indicator: ", 
                    np.append(vc_cols, form_cols),
                    format_func = lambda x: form_var_options[x],
                    key = 'color_var')#,horizontal = True)


form_text_options = {
    'l_prob': "Proportion of buildings with Visual Capital greater than average Agglomeration VC",
    'avg' : "Average Visual Capital for buildings within boundary",
    'med':'Median Visual Capital for buildings within boundary',
    'rich': "Proportion of building within boundary with Visual Capital greater than CHF 100k",
    'prob': "Proportion of building within boundary with Visual Capital greater than CHF 100k",
    'cv' : "Coefficient of Variability of Visual Capital within boundary",
    'net_income_ptp': "Average net-income pertaxpayer for a given commune",
    'bldg_count': "Number of building within boundary",
    'slope_median': 'Median slope of terrain within boundary',
    'slope_mean': 'Average slope of terrain within boundary'

}
st.sidebar.caption(form_text_options[st.session_state['color_var']])


# st.write(df.head(2))
# Place Map
m = folium.Map(location=(46.5197,6.6323),zoom_start=10,tiles = "Stamen Terrain")

@st.experimental_singleton
def create_map(dat, color_var, cmap_var, grpby_var,m):
    grp_choices = {'Commune': "GMDNAME", 'Hexbins': "hexbin_id"}

    # dat = dat.to_crs(4326)
    # return dat.explore(color_var, cmap =cmap_var, scheme ='NaturalBreaks', m= m)
    return folium.Choropleth( 
            geo_data = dat.iloc[:,[1,13]].to_json(),
            name = 'Choropleth',
            data = dat,
            columns = [grp_choices[grpby_var],color_var],
            key_on = 'feature.properties.'+(grp_choices[grpby_var]),
            # threshold_scale = getBins(df[color_var]),
            fill_color = cmap_var,
            fill_opacity = 0.5,
            line_color = cmap_var,
            line_opacity = 1,
            legend_name = color_var,
            smooth_factor=  0
)

# create_map(
#     df.to_crs(4326),
#     st.session_state['color_var'],
#     st.session_state['cmap_var'] ,
#     st.session_state['groupby_var'],m) 

m = df.explore(st.session_state['color_var'], cmap =st.session_state['cmap_var'], scheme ='NaturalBreaks', m= m)
map_data = st_folium(m,key="fig1",  width= 1650, height=1000)



st.sidebar.info(
    """
    A.R. Swietek:
    [GitHub](https://github.com/AdamSwietek) | [Twitter](https://twitter.com/aswietek) | [LinkedIn](https://ch.linkedin.com/in/adamrswietek)
    """
)


