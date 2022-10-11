from turtle import width
import pandas as pd
import geopandas as gpd

gdf = gpd.read_file('../geodata/ch_pred_res/res_hexbins_20220915.gpkg')
gdf['smoothed'] = (gdf.smoothed/1000).round(0)
import json
import dash
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign, arrow_function, Namespace
import seaborn as sns
import mapclassify as mc

from dash import dcc
from dash import html
from dash_leaflet import LayerGroup
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px


vc_cols = ['norm_diff','smoothed']
maxvsh_cols = gdf.columns[5:26].tolist()

sel_cols = vc_cols+maxvsh_cols
cmap_lst = ['RdBu','PuBuGn']  + len(maxvsh_cols)* ['viridis']
sel_dict = dict(zip(sel_cols, cmap_lst))

style = dict(weight = 0, opacity = 0, color = 'white', dashArray = "3", fillOpacity = 1)
style_handle = assign("""function(feature, context){
const {classes, colorscale, style, colorProp} = context.props.hideout;  // get props from hideout
const value = feature.properties[colorProp];  // get value the determines the color
style.fillColor = colorscale
for (let i = 0; i < classes.length; ++i) {
    if (value > classes[i]) {
        style.fillColor = colorscale[i];  // set the fill color according to the class
    }
}
return style;
}""")

def genLayer(color_prop):
    dat = gdf[['Agglo_Name','index_left', color_prop,'geometry']].dropna()
    if (color_prop == 'norm_diff'):
        dat = dat.query('abs(norm_diff) < 4')
        vmin, vmax = -4,4
    vmin, vmax = dat[color_prop].min(), dat[color_prop].max()

    # # Create colorbar.
    classes = mc.NaturalBreaks(dat[color_prop], k = 50).bins.tolist()
    # classes = np.linspace(vmin,vmax,50).tolist()
    colorscale = sns.color_palette(sel_dict[color_prop],len(classes)).as_hex()

    return (dat, classes, vmin, vmax, colorscale )

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": '7rem',
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#black",
}
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        html.Div(
            className = 'row', 
            classNamechildren = [
                html.Button('Commune', id='commune-bin', n_clicks=0),
                html.Button('Commune', id='commune-bin', n_clicks=0)
                ]),
            dcc.Graph(
            id='viewdist', 
            # style = {'width': '100%','height':'10%'},
            config= {'displayModeBar': False}),
    ],
    style=SIDEBAR_STYLE,
)
url = 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
map_ = dl.Map(
                id = 'map',
                children = dl.TileLayer(url = url),
                style = {
                    'height':'100vh', 
                    "margin-left": "18rem",
                    "padding": "2rem 2rem"
                },
                center=(46.5197,6.6323), 
                zoom = 9
                )
                
navbar = html.Div(
    className='row',
    children = [
        html.H4('What the Swiss See', style = {'height':'1rem'}),
        # html.Hr(style={
        #         # 'borderWidth': "0.3vh", 
        #         "width": "100%", 
        #         "backgroundColor": "#939799","opacity":".5"}),
        dcc.RadioItems(
            id = 'viewindicator', 
            options = sel_cols, 
            value = 'Gew1', 
            inline=True ),
    ], style = {'background-color':'white'})

app = dash.Dash()
app.layout = html.Div(children=[navbar,
                      html.Div(className='row',  # Define the row element
                               children=[sidebar, map_]),

                                ])

@app.callback(
    Output("map",'children'),
    Input('viewindicator','value')
)

def update_map(viewindicator):
    dat, classes, vmin, vmax, colorscale = genLayer(viewindicator)
    ctg = ["{}+".format(cls, classes[i + 1]) for i, cls in enumerate(classes[:-1])] + ["{}+".format(classes[-1])]
    colorbar = dlx.categorical_colorbar(
        categories=ctg, 
        colorscale=colorscale, 
        width=30, height=300, 
        tickDecimals = 0 if viewindicator == 'smoothed' else 1, 
        unit = '-%' if (viewindicator in maxvsh_cols) else '',
        position = "topright")
    colorbar = dl.Colorbar(
        id = 'cbar', 
        colorscale=colorscale, 
        width=300, height=30, min=vmin, max=vmax, unit='-', 
        tickValues = [-4,-3,-2,-1,0,1,2,3,4] if viewindicator == 'norm_diff' else classes[0::20], 
        position = 'topright')
    layer = dl.GeoJSON(
                    id = 'geojson',
                    data = json.loads(dat.to_json()), #zoomToBounds = True,
                    options = dict(style = style_handle),
                    hideout=dict(colorProp=viewindicator, classes = classes, 
                                    style = style,min=vmin, max=vmax, colorscale=colorscale),
                    zoomToBoundsOnClick=True,
                    )
    return [dl.TileLayer(url = url),layer, colorbar]

@app.callback(
    Output("viewdist",'figure'),
    Input('viewindicator','value')
)

def updateHist(viewindicator):
    fig = px.box(gdf[viewindicator].dropna(),  x = viewindicator)
    fig.update_layout(paper_bgcolor="black")
    return fig
if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = True)
    
    
 
