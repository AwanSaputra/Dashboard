import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

from apps.chartRMPM import summary, FPP


layout = html.Div(children=[
    html.Div(dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'FPP', 'value': 'FPP'},
            {'label': 'FKP', 'value': 'FKP'},
            {'label': 'SUMMARY', 'value': 'SUMMARY'}
        ],
        value='SUMMARY'), style={
            "display": "inline-block",
            "width": "20%"
    }),

    html.H1('RMPM', style={
        "color": "red",
        "text-align": "center",
        "background-color": "lightblue",
        "display": "inline-block",
        "width": "80%"
    }),

    html.Div(id='chart-content', children=[])
])


@ app.callback(Output('chart-content', 'children'),
               [Input('dropdown', 'value')])
def display_page(label):
    if label == 'SUMMARY':
        return summary.layout
    if label == 'FPP':
        return FPP.layout
    else:
        return "404 Page Error! Please choose a link"
