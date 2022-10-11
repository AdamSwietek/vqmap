import pandas as pd
import geopandas as gpd

gdf = gpd.read_file('../geodata/ch_pred_res/res_hexbins_20220915.gpkg')


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

vc_cols = ['norm_diff','smoothed']
maxvsh_cols = gdf.columns[5:26].tolist()

sel_cols = vc_cols+maxvsh_cols
cmap_lst = ['vlag','PuBuGn']  + len(maxvsh_cols)* ['magma']
sel_dict = dict(zip(sel_cols, cmap_lst))

# drop_lst = dash.dcc.Dropdown(sel_cols, 'smoothed', id='dropdown')

def genLayer(color_prop):
    dat = gdf[['Agglo_Name','index_left', color_prop,'geometry']].dropna()
    vmin, vmax = dat[color_prop].min(), dat[color_prop].max()


    # # Create colorbar.
    classes = mc.NaturalBreaks(dat[color_prop], k = 10).bins.tolist()
    # classes = np.linspace(vmin,vmax,50).tolist()
    colorscale = sns.color_palette(sel_dict[color_prop],len(classes)).as_hex()

    # # Geojson rendering logic, must be JavaScript as it is executed in clientside.
    style_handle = assign("""function(feature, context){
        const {classes, colorscale, style, colorProp} = context.props.hideout;  // get props from hideout
        const value = feature.properties[colorProp];  // get value the determines the color
        for (let i = 0; i < classes.length; ++i) {
            if (value > classes[i]) {
                style.fillColor = colorscale[i];  // set the fill color according to the class
            }
        }
        return style;
        }""")
    return (dat, style_handle, classes, style, vmin, vmax, colorscale )

def genHX(color_prop):
    dat, style_handle, classes, style, vmin, vmax, colorscale = genLayer(color_prop)
    layer = dl.GeoJSON(
                    id = 'geojson',
                    data = json.loads(dat.to_json()), #zoomToBounds = True,
                    options = dict(style = style_handle),
                    hideout=dict(colorProp=color_prop, classes = classes, 
                                    style = style,min=vmin, max=vmax, colorscale=colorscale)
                    )
    return layer

def genCBAR(color_prop):
    dat, style_handle, classes, style, vmin, vmax, colorscale = genLayer(color_prop)
    colorbar = dl.Colorbar(id = 'cbar', colorscale=colorscale, width=20, height=150, min=vmin, max=vmax, unit='-', nTicks = 2)
    return colorbar


style_handle = assign("""function(feature, context){
const {classes, colorscale, style, colorProp} = context.props.hideout;  // get props from hideout
const value = feature.properties[colorProp];  // get value the determines the color
for (let i = 0; i < classes.length; ++i) {
    if (value > classes[i]) {
        style.fillColor = colorscale[i];  // set the fill color according to the class
    }
}
return style;
}""")
style = dict(weight = 0, opacity = 0, color = 'white', dashArray = "3", fillOpacity = 1)

# layergrp = genHX('smoothed')
# cbargrp = genCBAR('smoothed') 

color_prop = "Gew1"
dat, style_handle, classes, style, vmin, vmax, colorscale = genLayer(color_prop)


app = dash.Dash()
app.layout = html.Div([
        dcc.RadioItems(sel_cols, 'Gew1', inline=True, id = 'view-radio'),
        # dash.dcc.Dropdown(sel_cols, id='dropdown'),
        html.Div(id='pandas-output-container-2'),
        html.Button('Click Me', id = 'btn'),
        dl.Map(children = 
            [ dl.TileLayer(),
            dl.GeoJSON(
                    id = 'geojson',
                    data = json.loads(dat.to_json()), #zoomToBounds = True,
                    options = dict(style = style_handle),
                    hideout = dict(colorProp=color_prop, classes = classes, style = style,min=vmin, max=vmax, colorscale=colorscale)
                    )
            ],
            style = {'width':'100%','height':'500px'},
            center=(46.5197,6.6323), 
            zoom = 9,
            id = 'map'
            )
]
)

# @app.callback(
#     Output('pandas-output-container-2', 'children'),
#     Input('view-radio', 'value')
# )
# def update_output(value):
#     return f'You have selected {value}'

# @app.callback(Output('cbar', 'nTicks'),
#               Input('btn', 'n_clicks')
#                 )
                
# def update_ticks(n_clicks):
# #     return n_clicks


@app.callback([Output('geojson','hideout')
                ],
                [Input('view-radio','value')],
                prevent_initial_callback=False)

def update_geojson(value):
    print(value)
    if value == None:
        print('No Value Selected')
    else:
        print(value)
        dat, style_handle, classes, style, vmin, vmax, colorscale = genLayer(value)
        # dat = json.loads(dat.to_json())
        hideout=dict(colorProp=value, classes = classes, style = style,min=vmin, max=vmax, colorscale=colorscale)
        return hideout


if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = True)
    
    
    
    # def update_colorscale(val):
#     _, _, _, _, _, _, colorscale = genLayer(val)
#     return colorscale

# def update_output(value):
#     return genLayer(layer_dict[value])