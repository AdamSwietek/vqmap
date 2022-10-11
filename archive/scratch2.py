from decimal import Overflow
from pydoc import classname
from turtle import position
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import dash
import dash_leaflet as dl
import dash_leaflet.express as dlx

import numpy as np

sel_cols =['Lake','Nature','Sky','Road','HPRoad','Vegitation','Industrial','Sewage','Airport','Agriculture']
def getBTNS(sel_cols):
    return [dbc.Button(var, outline = True, color = 'primary',size="sm") for i, var in enumerate(sel_cols)]
# the style arguments for the sidebar. We use position:fixed and a fixed width

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

groupby_section = html.Div(
    children= [
        html.Label("group",style=dict(width = '50%')),
        html.Div(
            children= [
                dcc.RadioItems(
                    id='grp-type', 
                    options=['communes','hexbins'],
                    value="hexbins",
                    # inline=True,
                    )], style=dict(display='flex', padding = '0rem 2rem')
                )]#, style=dict(display='flex', padding = '.5rem 1rem')
                )

navbar = dbc.NavbarSimple(
    brand="Visual Capital",
    brand_href="#",
    color="primary",
    dark=True,
)

navbar2 = dbc.NavbarSimple(
    # brand="Visual Capital",
    brand_href="#",
    color="light",
    dark=True,
)
# url = 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
url = 'https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png'
map_ = dl.Map(
                id = 'map',
                children = dl.TileLayer(url = url),
                style = {
                    # 'position':'fixed',
                    'height':'100vh', 
                    'width':'100%',
                #     "margin-left": "27rem",
                # #     # "margin-right": "10rem",
                #     "padding": "2rem 2rem"
                },
                center=(46.5197,6.6323), 
                zoom = 9
                )

row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns"), width = 2),
                dbc.Col(html.Div(children=map_)),
            ]
        ),
    ]
)

app.layout = html.Div([navbar, navbar2, row])

if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = True)
    
    
 
