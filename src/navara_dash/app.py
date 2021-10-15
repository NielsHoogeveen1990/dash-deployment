import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from navara_dash.utils.utils_dash import print_message


df = pd.DataFrame({
    "Jaar": ["Jaar 1", "Jaar 1", "Jaar 2", "Jaar 2", "Jaar 3", "Jaar 3"],
    "Omzet": [1.5, 4, 3, 6, 5, 9],
    "Afdeling": ["AI", "ENG", "AI", "ENG", "AI", "ENG"]
})

fig = px.bar(df, x="Jaar", y="Omzet", color="Afdeling", barmode="group", color_discrete_sequence=px.colors.qualitative.D3)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                name='Navara_Dashboard',
                url_base_pathname="/navara/")

app.layout = html.Div([
    html.Img(
        src=app.get_asset_url("Navara_Logo.png"),
        style={'height': '10%', 'width': '10%'}
    ),
    html.H1('Hi Navarianen!'),
    html.H4(print_message()),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')

