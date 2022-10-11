import pandas as pd
import geopandas as gpd

gdf2 = gpd.read_file('../geodata/ch_pred_res/res_hexbins_20220915.gpkg')

vc_cols = ['norm_diff','smoothed']
maxvsh_cols = gdf2.columns[5:26].tolist()
sel_cols = vc_cols + maxvsh_cols

df_geo = gdf2.loc[gdf2[sel_cols].dropna(axis=0, how = 'all').index,sel_cols+['Agglo_Name','geometry']]
geojson = df_geo.__geo_interface__

import plotly.express as px
from dash import Dash, dcc, html, Input, Output

token = open("mapbox_token.txt").read() # you will need your own token

cmap_lst = ['icefire','PuBuGn']  + len(maxvsh_cols)* ['viridis']
sel_dict = dict(zip(sel_cols, cmap_lst))

app = Dash()

app.layout = html.Div([
    html.H4('What the Swiss See'),
    html.P("Select a Visual Indicator:"),
    dcc.RadioItems(
        id='candidate', 
        options=vc_cols + maxvsh_cols,
        value="smoothed",
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("candidate", "value"))
def display_choropleth(candidate):
    fig = px.choropleth_mapbox(df_geo.reset_index(), geojson=geojson, locations = 'index', color=candidate,
                            color_continuous_scale=sel_dict[candidate],
                            color_continuous_midpoint= 0 if candidate == 'norm_diff' else None,
    #                            range_color=(0, 12),
                            mapbox_style="carto-positron",
                            # zoom=6, center = {"lat": 46.8182,  "lon": 8.2275 },#CH
                            zoom = 8, center = {"lat":46.5197,  "lon": 6.6323 },#Lausanne Center
                            opacity=0.5,
                            range_color = (-3,3) if candidate == 'norm_diff' else None,
                            
                            )
    fig = fig.update_traces(
        marker_line_width=0,
        colorbar_orientation='h'
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                        coloraxis_colorbar_thickness=15)
    return fig


app.run_server(debug=True)