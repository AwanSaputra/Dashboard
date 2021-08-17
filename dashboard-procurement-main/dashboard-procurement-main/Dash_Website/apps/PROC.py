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
])
