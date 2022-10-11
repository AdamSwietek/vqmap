import dash
import dash_leaflet as dl

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

def genGHX(data, sel_var, thres):
    gdf_hxbn = (data.groupby(['Agglo_Name','index_left'])[sel_var]
            .agg(prob    = lambda x: (100*(np.mean( x > thres))).astype(np.int16),
                 med     = lambda x: np.median(x).round(2),
                 avg     = lambda x: np.mean(x).round(2),
                 count   = lambda x: len(x))
      ).reset_index().query('count > 100')
    gdf_hxbn = pd.merge(gdf_hxbn, ch_hexbin.reset_index(), left_on='index_left', right_on= 'index', how='right')
    gdf_hxbn = gpd.GeoDataFrame(gdf_hxbn, geometry= gdf_hxbn.geometry , crs = 2056)
    return gdf_hxbn.dropna()[['prob','med','avg','count','geometry']].to_crs(4326)

#Inputs 

#Filter and Summarize Viewdata
ghx_smooth = genGHX(data = gdf, sel_var = 'smoothed', thres = 1)
ghx_smooth = (ghx_smooth
       .assign(avg = (ghx_smooth.avg/1000).astype(np.int16))
       .assign(med = (ghx_smooth.med/1000).astype(np.int16))
      )

#Filter and Summarize Viewdata
ghx_diff = genGHX(data = gdf.query('abs(norm_diff) < 4'), sel_var = 'norm_diff', thres = 1)


import json
import dash
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign, arrow_function, Namespace
import seaborn as sns
import mapclassify as mc

from dash import dcc
from dash import html
from dash_leaflet import LayerGroup
from dash.dependencies import Input, Output

layer_dict = {  'vc'    :   (ghx_smooth, 'PuBuGn'),'diff'  :   (ghx_diff, 'vlag')}

def genLayer(dat_option):
    color_prop = 'avg'
    dat = dat_option[0] #ghx_diff
    vmin, vmax = dat[color_prop].min(), dat[color_prop].max()

    style = dict(weight = 0, opacity = 0, color = 'white', dashArray = "3", fillOpacity = 1)

    # # Create colorbar.
    classes = mc.NaturalBreaks(dat[color_prop], k = 10).bins.tolist()
    # classes = np.linspace(vmin,vmax,50).tolist()
    colorscale = sns.color_palette(dat_option[1],len(classes)).as_hex()

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

def genHX(dat_option):
    dat, style_handle, classes, style, vmin, vmax, colorscale = genLayer(dat_option)
    layer = dl.GeoJSON(
                    id = 'geojson',
                    data = json.loads(dat.to_json()), #zoomToBounds = True,
                    options = dict(style = style_handle),
                    hideout=dict(colorProp='avg', classes = classes, style = style,min=vmin, max=vmax, colorscale=colorscale)
                    )
    return layer

def genCBAR(dat_option):
    dat, style_handle, classes, style, vmin, vmax, colorscale = genLayer(dat_option)
    colorbar = dl.Colorbar(id = 'cbar', colorscale=colorscale, width=20, height=150, min=vmin, max=vmax, unit='-', nTicks = 2)
    return colorbar

drop_lst = dcc.Dropdown(['vc', 'diff'], 'vc', id='dropdown')


layergrp = genHX(layer_dict['vc'])
cbargrp = genCBAR(layer_dict['vc'])

app = dash.Dash()
app.layout = html.Div([
    dash.dcc.Dropdown(id='geo_dropdown',
        options=[{'label': x, 'value': x} for x in ['prob', 'avg','med']],
        value=None,
        ),
    html.Button('Click Me', id = 'btn'),
    dl.Map(
        [   dl.TileLayer(),
        layergrp, cbargrp
            # dl.LayerGroup(children = [layergrp, cbargrp], id = 'layer_grp') 
            ],
        style = {'width':'100%','height':'500px'},
        center=(46.5197,6.6323), 
        zoom = 9,
        id = 'map'
        )
    
]
)

# @app.callback(Output('lac', 'children'),Input('geo_dropdown', 'value'))
@app.callback([Output('cbar', 'nTicks'),
                Output('geojson','colorProp')],
                [Input('btn', 'n_clicks'), 
                Input('geo_dropdown','val')])
def update_ticks(n_clicks):
    return n_clicks

def update_layer(val):
    return val

# def update_output(value):
#     return genLayer(layer_dict[value])


if __name__ == '__main__':
    app.run_server()

