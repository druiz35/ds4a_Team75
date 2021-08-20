"""
*****BASIC DASH DASHBOARD******
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    "background": "#111111",
    "text": "#7FDBFF"
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"]
)

app.layout = html.Div(
    style={"backgroundColor": colors["background"]}, 
    children=[
        html.H1(
            children="My First Dash App", 
            style={"textAlign": "center", "color": colors["text"]}),
        html.Div(
            children='''Dash: A web application framework for Python.''', 
            style={"textAlign": "center", "color": colors["text"]}),
        dcc.Graph(
            id="example-graph",
            figure=fig
    )
])
if __name__ == "__main__":
    app.run_server(debug=True)
"""

"""
******SIMPLE TABLE******
import dash
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
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

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H4(children="US Agriculture Exports (2011)"),
    generate_table(df)
])
if __name__ == "__main__":
    app.run_server(debug=True)
"""

"""
******INTERACTIVE SCATTER PLOT******
import dash
import dash_core_components as doc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
fig = px.scatter(
    df, 
    x="gdp per capita", 
    y="life expectancy",
    size="population",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)
app.layout = html.Div([
    doc.Graph(
        id="life-exp-vs-gdp",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
"""
"""
******DASH MARKDOWN******
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == "__main__":
    app.run_server(debug=True)
"""
"""
******INPUTS IN DASH******
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, externaly_stylesheets=external_stylesheets)
options_list = [
    {"label": "New York City"},
    {"label": u"Montréal", "value": "MTL"},
    {"label": "San Francisco", "value": "SF"}
]

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        options=options_list,
        value="MTL"
    ),
    html.Label("Multi-Select Dropdown"),
    dcc.Dropdown(
        options=options_list,
        value = ["MTL", "SF"],
        multi = True
    ),
    html.Label("Radio Items"),
    dcc.RadioItems(
        options=options_list,
        value = "MTL"
    ),
    html.Label("Checkboxes"),
    dcc.Checklist(
        options=options_list,
        value = ["MTL", "SF"]
    ),
    html.Label("Text Input"),
    dcc.Input(value="MTL", type="text"),
    html.Label("Slider"),
    dcc.Slider(
        min=0,
        max=9,
        marks = {i: "Label {}".format(i) if i == 1 else str(i) for i in range(1,6)},
        value = 5
    ),
], style = {"columnCount": 2})

if __name__ == "__main__":
    app.run_server(debug=True)
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

data = pd.read_csv('../data/df_merged_final_vars.csv')
investments = pd.melt(data, id_vars=['anio_corte','municipio'], value_vars=['inversion_transformacion','inversion_conectividad'])
municipalities = list(investments['municipio'].unique())

## Lineplot:
# fig = px.line(investments[investments['municipio']=='medellin'], x="anio_corte", y="value", color='variable', title='Inversión MinTC - Transformación en Medellín')
# fig.show()

app.layout = html.Div([
    dcc.Dropdown(
        id="fig_dropdown",
        options=[{"label": x, "value": x} 
                 for x in municipalities],
        placeholder='Select a municipality',
        searchable=True
    ),
    dcc.Graph(id="line-chart"),
])

@app.callback(
    Output("line-chart", "figure"), 
    [Input("fig_dropdown", "value")])
def update_line_chart(value):
    fig = px.line(investments[investments['municipio']==value], 
        x="anio_corte", y="value", color='variable')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)