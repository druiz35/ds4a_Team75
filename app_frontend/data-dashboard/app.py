
from re import M
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_graphs

# OJO: Los paths cambiarán en un futuro. Se cambiarán una vez se haga la conexión con el backend.
datasets_folder_path = "../../../datasets/"

<<<<<<< HEAD
#Data loading and processing
data = pd.read_csv(datasets_folder_path + 'data_tables/df_vars_modelamiento.csv')
investments = pd.melt(data, id_vars=['anio_corte','municipio'], value_vars=['inversion_transformacion','inversion_conectividad', 'inversion'])
maps_path = "../../../datasets/maps_html"
=======
app = dash.Dash(__name__)

data = pd.read_csv('../../../data/df_vars_modelamiento.csv')
investments = pd.melt(data, id_vars=['anio_corte','municipio_fixed_name'], value_vars=['inversion_transformacion','inversion_conectividad', 'inversion'])
municipalities = list(investments['municipio_fixed_name'].unique())

init_map = open('../../../data/maps_html/map_foliumTotal2016.html','r').read()
>>>>>>> ac31afd41df9a8d67d345d347c5b68ed0b12339e

#Graph counter for dynamically adding graphs to the dashboard
graph_counter_dict = {
    "stripplot": 1,
    "geograph": 1,
    "linechart": 1,
    "bargraph": 1,
    "treemap": 1,
    "piegraph": 1,
    "distplot": 1
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
graphs = [
    dash_graphs.Linechart(0, data), 
    dash_graphs.Stripplot(0, data), 
    dash_graphs.Geograph(0, maps_path),
    dash_graphs.Bargraph(0, data),
    dash_graphs.Treemap(0, data),
    dash_graphs.Piechart(0, data),
    dash_graphs.Distplot(0, data)]

#children_graphs_list = [html.Div(graph.create_graph()) for graph in graphs]    
children_left_graphs_list, children_right_graphs_list = [], []
div_flag = True
for graph in graphs:
    if div_flag:
        item = html.Div(graph.create_graph(), className="graph")
        children_left_graphs_list.append(item)
    elif not div_flag:
        item = html.Div(graph.create_graph(), className="graph")
        children_right_graphs_list.append(item)
    div_flag = not div_flag


modal_body_list = [dash_graphs.create_modal_button(i) for i in ["linechart", "stripplot", "geograph", "bargraph", "treemap", "piechart", "distplot"]]
modal_list = [dbc.ModalHeader("Añadir Nuevo Gráfico"), dbc.ModalBody(modal_body_list), dbc.ModalFooter(dash_graphs.create_modal_button("close-modal"))]

app.layout = html.Div(
    id="content",
    children=[
        dbc.Modal(modal_list, id="modal-body-scroll", scrollable=True, is_open=False),
        html.Div(id="left-graphs", children=children_left_graphs_list),
        html.Div(id="right-graphs", children=children_right_graphs_list),
        #dbc.Button("+", id="open-body-scroll", className="add-graph-button", n_clicks=0),
        ]
    )
<<<<<<< HEAD
#Callbacks for initial graphs
for graph in graphs:
    graph.update_graph(app)
=======
    return fig
# Callback for maps:
@app.callback(
    Output("geo-graph", "srcDoc"), 
    Input("year", "value"),
    Input("type_of_investment", "value"))
def update_geo_graph(year, type_of_investment):
    if type_of_investment == 'Inversión Total':
        if(year==2016):
            return open('../../../data/maps_html/map_foliumTotal2016.html','r').read()
        elif(year==2017):
            return open('../../../data/maps_html/map_foliumTotal2017.html','r').read()
        elif(year==2018):
            return open('../../../data/maps_html/map_foliumTotal2018.html','r').read()
        elif(year==2019):
            return open('../../../data/maps_html/map_foliumTotal2019.html','r').read()
    elif type_of_investment == 'Inversión en Conectividad':
        if(year==2016):
            return open('../../../data/maps_html/map_foliumConectividad2016.html','r').read()
        elif(year==2017):
            return open('../../../data/maps_html/map_foliumConectividad2017.html','r').read()
        elif(year==2018):
            return open('../../../data/maps_html/map_foliumConectividad2018.html','r').read()
        elif(year==2019):
            return open('../../../data/maps_html/map_foliumConectividad2019.html','r').read()
    elif type_of_investment == 'Inversión en Transformación':
        if(year==2016):
            return open('../../../data/maps_html/map_foliumTransformación2016.html','r').read()
        elif(year==2017):
            return open('../../../data/maps_html/map_foliumTransformación2017.html','r').read()
        elif(year==2018):
            return open('../../../data/maps_html/map_foliumTransformación2018.html','r').read()
        elif(year==2019):
            return open('../../../data/maps_html/map_foliumTransformación2019.html','r').read()
>>>>>>> ac31afd41df9a8d67d345d347c5b68ed0b12339e

#Callback for modal
""""
@app.callback(
    Output("modal-body-scroll", "is_open"),
    [Input("open-body-scroll", "n_clicks"), Input("close-body-scroll", "n_clicks")],
    [State("modal-body-scroll", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
"""

if __name__ == '__main__':
    app.run_server(debug=True)
