import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import chart_studio.plotly as py
import pandas as pd

from CombinedScrapper.generator import pokedex_df

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/alpha_shape.csv')
df.head()
df = pokedex_df()

print(df)

scatter = dict(
    mode="markers",
    name="y",
    type="scatter3d",
    x=df['atk'], y=df['spa'], z=df['spe'],
    marker=dict(size=2, color="rgb(23, 190, 207)")
)
clusters = dict(
    alphahull=7,
    name="y",
    opacity=0.1,
    type="mesh3d",
    x=df['atk'], y=df['spa'], z=df['spe']
)
layout = dict(
    title='3d point clustering',
    scene=dict(
        xaxis=dict(zeroline=False),
        yaxis=dict(zeroline=False),
        zaxis=dict(zeroline=False),
    )
)

fig = dict(data=[scatter, clusters], layout=layout)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])

app.run_server(debug=True)
