import dash
import dash_core_components as dcc
import dash_html_components as html
from matplotlib.pyplot import title

import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import base64
import io
from app import app

colors = {
    "graphBackground": "#F5F5F5",
    "background": "#ffffff",
    "text": "#000000"
}

layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(dcc.Graph(
        id='FPPGRAPH',
    ), style={
        "display": "block",
        "width": "100%"
    }),
])


def parse_data(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV or TXT file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded),
                               sheet_name='FPP', skiprows=4, usecols="B,D,O")
        elif 'txt' or 'tsv' in filename:
            # Assume that the user upl, delimiter = r'\s+'oaded an excel file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), delimiter=r'\s+')
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    print(df)
    return df


@app.callback(Output('FPPGRAPH', 'figure'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph1(contents, filename):
    fig = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)
        planning = df.loc[df['tier1'] == 'planning'].count()[0]
        ADMINISTRASI = df.loc[df['tier1'] == 'ADMINISTRASI'].count()[0]
        NaN = df['tier1'].isnull().values.any().sum()
        mask = df['TGL'].map(lambda x: x.month) == 2
        df_with_good_dates = df.loc[mask]
        print(df_with_good_dates)
        month_list = [i.strftime("%b-%y")
                      for i in df_with_good_dates['TGL']]

        labels = sorted(set(month_list))
        # c = df_with_good_dates[df_with_good_dates.tier1 ==
        #                        'planning'].groupby(['tier1', 'TGL']).TGL.count()
        # print(c)
        values = [planning, ADMINISTRASI, NaN]
        layout = go.Layout(title='Trend Category Per Bulan', barmode='stack')
        fig = go.Figure(data=[
            go.Bar(name='Planning', x=labels, y=values),
            go.Bar(name='ADMINISTRASI', x=labels, y=values),
            go.Bar(name='NaN', x=labels, y=values)
        ])

    return fig