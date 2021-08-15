import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

from apps.chartRMPM import FPP


layout = html.Div(children=[

    html.H1(children='RMPM', style={
        "text-align": "center"
    }),

    html.Div(dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'FPP', 'value': 'a'},
            {'label': 'FKP', 'value': 'b'},
            {'label': 'Monitor Buffer Stock', 'value': 'c'},
        ],
        value=''), style={
            "display": "inline-block",
            "width": "20%"
    }),

    html.Div(id='chart-content', children=[])
])


@ app.callback(Output('chart-content', 'children'),
               [Input('dropdown', 'value')])
def display_page(label):
    # if label == 'FKP':
    #     return FKP.layout
    if label == 'a':
        return FPP.layout
    if label == 'b':
        return FPP.layout
    if label == 'c':
        return FPP.layout
    else:
        return "Silahkan klik dropdown diatas dan pilih kategori!"
