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
        id='upload-dataMBS',
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
    html.Div(id='filename-MBS'),

    html.Div([
        dcc.Tabs(id='tabs-MBS', value='tab-1', children=[
            dcc.Tab(label='All Supplier', value='tab-1'),
            dcc.Tab(label='Specific Supplier', value='tab-2'),
        ]),
        html.Div(id='tabs-MBS-content')
    ])
])


@app.callback(
    Output("upload-dataMBS", "style"),
    [Input("upload-dataMBS", "contents")]
)
def hide_upload(contents):
    if contents is not None:
        return {"display": "none"}
    return dash.no_update


@app.callback(Output('tabs-MBS-content', 'children'),
              Input('tabs-MBS', 'value'),
              Input('upload-dataMBS', 'contents'),
              Input('upload-dataMBS', 'filename'),

              )
def render_content(tab, contents, filename):
    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)
        x = df.pivot_table(columns=['Supplier'], aggfunc='size')
        nama_suplier = x.index.tolist()
        if filename != 'Req PM.xlsx':
            return html.Div([
                'File yang anda input tidak bernama Req PM.xlsx atau nama sheet tidak sesuai, mohon dicek kembali dan refresh page ! '
            ])
        else:
            if tab == 'tab-1':
                return html.Div([
                    html.Div('Tanggal'),
                    'Bulan',
                    dcc.Input(
                        id="bulan",
                        value=0.0,
                        type="number"
                    ),
                    html.Div(dcc.Graph(
                        id='SupGraph1',
                    ), style={
                        "display": "inline-block",
                        "width": "100%"
                    }),
                ])
            elif tab == 'tab-2':
                return html.Div([
                    html.Div(dcc.Dropdown(
                        id='dropdown1',

                        options=[
                            {'label': i, 'value': i} for i in nama_suplier
                        ],
                        value=''), style={
                        "display": "inline-block",
                        "width": "20%"
                    }),

                    html.Div(id='chart-2', children=[])

                ]),


def parse_data(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    if filename != 'Req PM.xlsx':
        return html.Div([
            'There was an error processing this file.'
        ])
    else:
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV or TXT file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded), index_col=None,
                                   sheet_name='Buffer Stock')
            elif 'txt' or 'tsv' in filename:
                # Assume that the user upl, delimiter = r'\s+'oaded an excel file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')), delimiter=r'\s+')
        except Exception as e:

            return html.Div([
                'There was an error processing this file.'
            ])
        return df


@app.callback(Output('SupGraph1', 'figure'),
              [
    Input('upload-dataMBS', 'contents'),
    Input('upload-dataMBS', 'filename'),
    Input("bulan", "value")
])
def update_graph1(contents, filename, bulan):
    fig = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)
        # tanggal = df[df['Month'] == '2021-01-01']
        tanggal = df[df['Month'].map(lambda x: x.month) == bulan]
        # CHART1 SUPLIER VS AVERAGE
        Req_pm = tanggal
        x = df.pivot_table(columns=['Supplier'], aggfunc='size')

        labels1 = x.index.tolist()
        values1 = []
        for i in range(0, len(labels1)):
            A = labels1[i]
            name_label = Req_pm[Req_pm['Supplier'] == A]
            B = name_label['Level %'].mean()
            values1.append(B)

        nama_Supplier = labels1
        hasil_value = values1

        df1 = pd.DataFrame(data=nama_Supplier, columns=['Vendor'])
        df2 = pd.DataFrame(data=hasil_value, columns=['Hasil'])
        result = pd.concat([df1, df2], axis=1)
        df3 = pd.DataFrame(data=result)

        layout = go.Layout(title='SPENDING MBS (MTD Qty)')
        fig = go.Figure(
            data=[go.Bar(
                x=df3['Vendor'],
                y=df3['Hasil'],
                name="Amcor Flexibles"
            )], layout=layout)

    return fig


@ app.callback(Output('chart-2', 'children'),
               [Input('dropdown1', 'value')])
def display_page(label):
    # if label == 'FKP':
    #     return FKP.layout
    if label is not None:

        return html.H1(children='test1', style={
            "text-align": "center"
        }),
    else:
        return "404 Page Error! Please choose a link"
