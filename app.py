from re import M
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# OJO: Los paths cambiarán en un futuro. Se cambiarán una vez se haga la conexión con el backend.

app = dash.Dash(__name__)

data = pd.read_csv('df_vars_modelamiento.csv')
investments = pd.melt(data, id_vars=['anio_corte','municipio'], value_vars=['inversion_transformacion','inversion_conectividad', 'inversion'])
municipalities = list(investments['municipio'].unique())

init_map = open('../data/maps_html/map_foliumTotal2016.html','r').read()

# ***** START OF STRIPPLOT *****
x_options_stripplot = [
    {"label": u"Año Corte", "value": "anio_corte"},
    {"label": "Municipio", "value": "municipio"},
    {"label": "Departamento", "value": "departamento"},
    {"label": "Grupo Dotaciones", "value": "grupo_dotaciones"},
    {"label": "Categoria de Ruralidad", "value": "categoria_de_ruralidad"}
]
y_options_stripplot = []
for column_name in list(data.columns)[6:]:
    cleaned_column_name = column_name.replace("_", " ")
    label_dict = {"label": cleaned_column_name.title(),"value": column_name}
    y_options.append(label_dict)

stripplot = [
    html.Label("X Axis"),
    dcc.Dropdown(
        id = "x_options_menu_stripplot",
        options= x_options_stripplot,
        value="anio_corte",
    ),
    dcc.Dropdown(
        id = "y_options_menu_stripplot",
        options = y_options_stripplot,
        value="cobertura_media_neta"
    ),
    dcc.Graph(id="stripplot")]
# ***** END OF STRIPPLOT *****



app.layout = html.Div(children=[
    # Linechart:
    html.Div([
        dcc.Dropdown(
            id="fig_dropdown",
            options=[{"label": x, "value": x} for x in municipalities],
            placeholder='Select a municipality',
            searchable=True
        ),
        dcc.Graph(id="line-chart"),
    ]),
    # Stripplot
    html.Div(stripplot),
    # Maps:
    html.Div(children=[
        dcc.Dropdown(
            id="year",
            options=[{"label": x, "value": x} for x in [2016,2017,2018,2019]],
            placeholder="Select a year",
        ),
        dcc.Dropdown(
            id="type_of_investment",
            options=[{"label": x, "value": x} for x in ['Inversión Total', 'Inversión en Conectividad', 'Inversión en Transformación']],
            placeholder="Select a type of investment",
        ),
        html.Iframe(
                   id='geo-graph',
                   srcDoc=init_map,
                   width='100%',
                   height='600'),
    ])
])

# Callback for lineplot:
@app.callback(
    Output("line-chart", "figure"), 
    [Input("fig_dropdown", "value")])
def update_line_chart(value):
    # fig = px.line(investments[investments['municipio']==value], 
    #     x="anio_corte", y="value", color='variable')
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=data[data['municipio']==value]["anio_corte"], y=data[data['municipio']==value]["inversion_transformacion"], name="Inversión MinTC - Transformación"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=data[data['municipio']==value]["anio_corte"], y=data[data['municipio']==value]["inversion_conectividad"], name="Inversión MinTC - Conectividad"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=data[data['municipio']==value]["anio_corte"], y=data[data['municipio']==value]["inversion"], name="Inversión MinTC - Total"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=data[data['municipio']==value]["anio_corte"], y=data[data['municipio']==value]["componente_de_resultados"], name="Índice Calidad de Vida"),
        secondary_y=True,
    )
    return fig
# Callback for maps:
@app.callback(
    Output("geo-graph", "srcDoc"), 
    Input("year", "value"),
    Input("type_of_investment", "value"))
def update_geo_graph(year, type_of_investment):
    if type_of_investment == 'Inversión Total':
        if(year==2016):
            return open('../data/maps_html/map_foliumTotal2016.html','r').read()
        elif(year==2017):
            return open('../data/maps_html/map_foliumTotal2017.html','r').read()
        elif(year==2018):
            return open('../data/maps_html/map_foliumTotal2018.html','r').read()
        elif(year==2019):
            return open('../data/maps_html/map_foliumTotal2019.html','r').read()
    elif type_of_investment == 'Inversión en Conectividad':
        if(year==2016):
            return open('../data/maps_html/map_foliumConectividad2016.html','r').read()
        elif(year==2017):
            return open('../data/maps_html/map_foliumConectividad2017.html','r').read()
        elif(year==2018):
            return open('../data/maps_html/map_foliumConectividad2018.html','r').read()
        elif(year==2019):
            return open('../data/maps_html/map_foliumConectividad2019.html','r').read()
    elif type_of_investment == 'Inversión en Transformación':
        if(year==2016):
            return open('../data/maps_html/map_foliumTransformación2016.html','r').read()
        elif(year==2017):
            return open('../data/maps_html/map_foliumTransformación2017.html','r').read()
        elif(year==2018):
            return open('../data/maps_html/map_foliumTransformación2018.html','r').read()
        elif(year==2019):
            return open('../data/maps_html/map_foliumTransformación2019.html','r').read()

# callback for stripplot
@app.callback(
    Output("stripplot", "figure"),
    Input("x_options_menu_stripplot", "value"),
    Input("y_options_menu_stripplot", "value"))
def update_stripplot(x_option_name="anio_corte", y_option_name="cobertura_media_neta"):
    fig = px.strip(df, x=x_option_name, y=y_option_name)
    fig.update_xaxes(title=x_option_name)
    fig.update_yaxes(title=y_option_name)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)