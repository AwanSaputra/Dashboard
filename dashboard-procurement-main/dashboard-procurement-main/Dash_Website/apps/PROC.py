import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
A = ['FPP', 'FKP', 'MBS']
layout = html.Div(children=[
    html.H1(children='PROC', style={
        "text-align": "center"
    }),
    html.H3(children='Maintenance', style={
        "text-align": "center"
    }),
    html.Div(dcc.Dropdown(
        id='dropdown',

        options=[
            {'label': i, 'value': i} for i in A
        ],
        value=''), style={
            "display": "inline-block",
            "width": "20%"
    }),
    html.Div(id='chart-1', children=[])
])


@ app.callback(Output('chart-1', 'children'),
               [Input('dropdown', 'value')])
def display_page(label):
    # if label == 'FKP':
    #     return FKP.layout
    if label == 'FPP':
        print(label)
        return html.H1(children='test1', style={
            "text-align": "center"
        }),
    if label == 'FKP':
        return html.H1(children='test2', style={
            "text-align": "center"
        }),
    if label == 'MBS':
        return html.H1(children='test3', style={
            "text-align": "center"
        }),
    else:
        return "404 Page Error! Please choose a link"
