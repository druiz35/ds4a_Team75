import dash
import folium
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
request_path_prefix = None
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

app = dash.Dash(__name__,
                requests_pathname_prefix=request_path_prefix,
                external_stylesheets=external_stylesheets)

# HTML CONTROLS - START

dropdown=dcc.Dropdown(id="dropdown",
             options=[
                 {"label": 2016, "value": 2016},
                 {"label": 2017, "value": 2017},
                 {"label": 2018, "value": 2018},
                 {"label": 2019, "value": 2019}
               ],
             value="YEAR",
          )

init_map=open('data/zones.html','r').read()

plot = html.Iframe(
                   id='geo-graph',
                   srcDoc=init_map,
                   width='100%',
                   height='600')

# HTML CONTROLS - END

# HTML LAYOUT - START
app.layout = dbc.Container(
       [
        html.H1("MinTIC Investments"),
        html.Div(children=[dropdown, plot]),
        html.Div(id='my-output'),
    ],
    fluid=True,
)

# HTML LAYOUT - END

# APP CALLBACK - BEGIN
@app.callback(
    Output(component_id='geo-graph', component_property='srcDoc'),
    [
        Input(component_id='dropdown', component_property='value'),      
    ],
)
# APP CALLBACK - END
# FUNCTION - BEGIN
def make_graph(value):
    if(value==2016):
        return open('data/zones.html','r').read()
    else:
        return open('data/zones2.html','r').read()
# FUNCTION - END


# APP CALLBACK FUNCTIONALITY - BEGIN

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='dropdown', component_property='value')
)
def update_output_div(input_value):
        return 'Output: {}'.format(input_value)

# APP CALLBACK FUNCTIONALITY - END

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)