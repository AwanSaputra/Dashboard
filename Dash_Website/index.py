import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import PROC, RMPM, CLEARANCE, INMKT, RMPMSS, NONMKT


app.layout = html.Div(children=[
    html.H1(children='Welcome To Procurement', style={
        "color": "red",
        "text-align": "center",
        "background-color": "lightblue"
    }),
    html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div([
            dcc.Link('PROC |', href='/apps/PROC'),
            dcc.Link('RM/PM-SS |', href='/apps/RMPMSS'),
            dcc.Link('RM/PM |', href='/apps/RMPM'),
            dcc.Link('CLEARANCE |', href='/apps/CLEARANCE'),
            dcc.Link('INDIRECT MKT |', href='/apps/INMKT'),
            dcc.Link('INDIRECT NON MKT ', href='/apps/NONMKT'),
        ], className="row"),
        html.Div(id='page-content', children=[]),
    ])])


@ app.callback(Output('page-content', 'children'),
               [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/RMPM':
        return RMPM.layout
    if pathname == '/apps/PROC':
        return PROC.layout
    if pathname == '/apps/CLEARANCE':
        return CLEARANCE.layout
    if pathname == '/apps/INMKT':
        return INMKT.layout
    if pathname == '/apps/RMPMSS':
        return RMPMSS.layout
    if pathname == '/apps/NONMKT':
        return NONMKT.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)
