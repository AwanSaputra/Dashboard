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
    html.Div(id='filename-summary'),

    html.Div([
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
            dcc.Tab(label='Value', value='tab-1'),
            dcc.Tab(label='Supplier', value='tab-2'),
        ]),
        html.Div(id='tabs-example-content')
    ])
])


@app.callback(
    Output("upload-data", "style"),
    [Input("upload-data", "contents")]
)
def hide_upload(contents):
    if contents is not None:
        return {"display": "none"}
    return dash.no_update


@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'),
              Input('upload-data', 'filename'),
              Input('upload-data', 'filename')
              )
def render_content(tab, contents, filename):
    if contents:
        contents = contents[0]
        filename = filename[0]
        print(filename)
        print('diatas itu render content')
        if filename != 'RTS Apr21.xlsx':
            return html.Div([
                'File yang anda input tidak bernama RTS Apr21.xlsx atau nama sheet tidak sesuai, mohon dicek kembali dan refresh page ! '
            ])
        else:
            if tab == 'tab-1':
                return html.Div([
                    html.Div(dcc.Graph(
                        id='Mygraph1',
                    ), style={
                        "display": "inline-block",
                        "width": "30%"
                    }),
                    html.Div(dcc.Graph(
                        id='Mygraph2',
                    ), style={
                        "display": "inline-block",
                        "width": "30%"
                    }),
                    html.Div(dcc.Graph(
                        id='Mygraph3',
                    ), style={
                        "display": "inline-block",
                        "width": "30%"
                    }),
                ])
            elif tab == 'tab-2':
                return html.Div([
                    html.Div(dcc.Graph(
                        id='Mygraph4',
                    ), style={

                    }),
                    html.Div(dcc.Graph(
                        id='Mygraph5',
                    ), style={
                        "display": "block",
                        "width": "100%"
                    }),
                    html.Div(dcc.Graph(
                        id='Mygraph6',
                    ), style={
                        "display": "block",
                        "width": "100%"
                    })
                ])


def parse_data(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    if filename != 'RTS Apr21.xlsx':
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
                                   sheet_name='SHP___Receiving_Transaction_Su_', skiprows=7, usecols="B,F,K,L,M,N")
            elif 'txt' or 'tsv' in filename:
                # Assume that the user upl, delimiter = r'\s+'oaded an excel file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')), delimiter=r'\s+')
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
        return df


@app.callback(Output('filename-summary', 'children'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
]
)
def update_output2(contents, filename):
    string_prefix = 'You have selected: '
    table = html.Div()
    print("Sebelum if contents :", filename)
    if contents:
        contents = contents[0]
        filename = filename[0]
        print("Sesudah if contents :", filename)
        string_prefix = string_prefix + filename
    if len(string_prefix) == len('You have selected: '):
        return 'Select a file to see it displayed here'
    else:
        return string_prefix


@app.callback(Output('Mygraph1', 'figure'),
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
        Data_RTS = parse_data(contents, filename)
        # CHART1 SPENDING SUMMARY (MTD Qty)
        x = Data_RTS.pivot_table(columns=['category'], aggfunc='size')
        labels1 = x.index.tolist()
        values1 = []
        for i in range(0, len(labels1)):
            A = labels1[i]
            name_label = Data_RTS[Data_RTS['category'] == A]
            B = name_label['MTD Qty'].sum()
            values1.append(B)

        layout = go.Layout(title='SPENDING SUMMARY (MTD Qty)')
        fig = go.Figure(
            data=[go.Pie(labels=labels1, values=values1)], layout=layout)

    return fig


@app.callback(Output('Mygraph2', 'figure'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph2(contents, filename):
    fig2 = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        Data_RTS = parse_data(contents, filename)
        # CHART2 SPENDING SUMMARY (YTD Qty)
        x = Data_RTS.pivot_table(columns=['category'], aggfunc='size')
        labels2 = x.index.tolist()
        values2 = []
        for i in range(0, len(labels2)):
            A = labels2[i]
            name_label = Data_RTS[Data_RTS['category'] == A]
            B = name_label['YTD Qty'].sum()
            values2.append(B)

        layout2 = go.Layout(title='SPENDING SUMMARY (YTD Qty)',
                            hovermode='closest')
        fig2 = go.Figure(
            data=[go.Pie(labels=labels2, values=values2)], layout=layout2)

    return fig2


@app.callback(Output('Mygraph3', 'figure'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph2(contents, filename):
    fig3 = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        Data_RTS = parse_data(contents, filename)
        # CHART3 SPENDING SUMMARY (YTD Qty)
        x = Data_RTS.pivot_table(columns=['category'], aggfunc='size')
        labels3 = x.index.tolist()
        values3 = []
        for i in range(0, len(labels3)):
            A = labels3[i]
            name_label = Data_RTS[Data_RTS['category'] == A]
            B = name_label['MTD Value'].sum()
            values3.append(B)

        layout3 = go.Layout(title='SPENDING SUMMARY (MTD Value)',
                            hovermode='closest')
        fig3 = go.Figure(
            data=[go.Pie(labels=labels3, values=values3)], layout=layout3)

    return fig3


@app.callback(Output('Mygraph4', 'figure'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph4(contents, filename):
    fig4 = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        Data_RTS = parse_data(contents, filename)
        # CHART4 SPENDING SUMMARY SUPPLIER(MTD Qty)
        x = Data_RTS.pivot_table(columns=['Vendor Name'], aggfunc='size')
        labels4 = x.index.tolist()
        values4 = []
        for i in range(0, len(labels4)):
            A = labels4[i]
            name_label = Data_RTS[Data_RTS['Vendor Name'] == A]
            B = name_label['MTD Qty'].sum()
            values4.append(B)

        layout4 = go.Layout(
            title='SPENDING SUMMARY SUPPLIER(MTD Qty)', height=700)
        fig4 = go.Figure(
            data=[go.Pie(labels=labels4, values=values4)], layout=layout4)

    return fig4


@app.callback(Output('Mygraph5', 'figure'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph5(contents, filename):
    fig5 = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        Data_RTS = parse_data(contents, filename)
        # CHART5 SPENDING SUMMARY SUPPLIER(YTD Qty)
        x = Data_RTS.pivot_table(columns=['Vendor Name'], aggfunc='size')
        labels5 = x.index.tolist()
        values5 = []
        for i in range(0, len(labels5)):
            A = labels5[i]
            name_label = Data_RTS[Data_RTS['Vendor Name'] == A]
            B = name_label['YTD Qty'].sum()
            values5.append(B)

        layout5 = go.Layout(title='SPENDING SUMMARY SUPPLIER(YTD Qty)',
                            hovermode='closest')
        fig5 = go.Figure(
            data=[go.Pie(labels=labels5, values=values5)], layout=layout5)

    return fig5


@app.callback(Output('Mygraph6', 'figure'),
              [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph6(contents, filename):
    fig6 = {
        'layout': go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"])
    }

    if contents:
        contents = contents[0]
        filename = filename[0]
        Data_RTS = parse_data(contents, filename)
        # CHART6 SPENDING SUMMARY SUPPLIER(MTD Value)
        x = Data_RTS.pivot_table(columns=['Vendor Name'], aggfunc='size')
        labels6 = x.index.tolist()
        values6 = []
        for i in range(0, len(labels6)):
            A = labels6[i]
            name_label = Data_RTS[Data_RTS['Vendor Name'] == A]
            B = name_label['MTD Value'].sum()
            values6.append(B)

        layout6 = go.Layout(title='SPENDING SUMMARY SUPPLIER(MTD Value)',
                            hovermode='closest')
        fig6 = go.Figure(
            data=[go.Pie(labels=labels6, values=values6)], layout=layout6)

    return fig6
