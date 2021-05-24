import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from pandas_datareader import data as web
from datetime import datetime as dt

from pokedexGenerator.generator import pokedex_df

app = dash.Dash('Hello World')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pokedex_df()

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app.layout = html.Div(style={'marginTop':100, 'marginRight':100, 'marginLeft':100}, children=[
    html.Div([
        html.H2("Stock App")
    ], className="banner"),

    generate_table(df)
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'google',
        dt(2017, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

if __name__ == '__main__':
    app.run_server()