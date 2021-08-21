import pandas as pd
import json
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from folium.features import GeoJsonPopup, GeoJsonTooltip


investments = pd.read_csv("../data/df_merged_final_vars.csv", usecols=['anio_corte','departamento','codigo_departamento','inversion','inversion_conectividad','inversion_transformacion'])

mapa_colombia = gpd.read_file("/Users/SebastianGuzman/Desktop/DS4A-Final_Project/MGN2020_DPTO_POLITICO/MGN_DPTO_POLITICO.shp")

mapa_colombia['DPTO_CCDGO'] = mapa_colombia['DPTO_CCDGO'].astype('int64')
mapa_colombia = mapa_colombia.sort_values('DPTO_CCDGO').reset_index().drop(columns='index')
dpto_nombres = investments[['codigo_departamento','departamento']].drop_duplicates().sort_values('codigo_departamento').reset_index()['departamento']
mapa_colombia['departamento'] = dpto_nombres

def get_aggr_invest_by_year(year):
    '''
    This function gets the investment aggregated data along departments for a specific year
    '''
    dff = gpd.GeoDataFrame(investments[investments['anio_corte']==year].\
        groupby(['codigo_departamento', 'departamento', 'anio_corte']).sum().reset_index().\
            merge(mapa_colombia[['DPTO_CCDGO', 'DPTO_CNMBR', 'geometry']], left_on='codigo_departamento', right_on='DPTO_CCDGO')).\
                drop(columns='DPTO_CCDGO')
    dff['inversion_total_millions'] = dff['inversion']/1000000
    dff['inversion_conectividad_millions'] = dff['inversion_conectividad']/1000000
    dff['inversion_transformacion_millions'] = dff['inversion_transformacion']/1000000
    return dff

# geo_map_col2 = json.loads(dff.to_json())

def create_map(df, json_obj, type_investment):
    if type_investment == 'inversion_total_millions':
        title_investment = 'Total'
    elif type_investment == 'inversion_conectividad_millions':
        title_investment = 'Conectividad'
    elif type_investment == 'inversion_transformacion_millions':
        title_investment = 'Transformación'

    m = folium.Map(location=[5, -72], zoom_start=5, tiles='CartoDB positron')

    tooltip = GeoJsonTooltip(
        fields=["DPTO_CNMBR", type_investment],
        aliases=["Departamento:", "Inversión (millones COP) " + title_investment + " MinTIC " + str(df['anio_corte'].unique()[0]) +":"],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=800,
    )

    choropleth = folium.Choropleth(
        geo_data=json_obj,
        name="choropleth",
        data=df,
        columns=["departamento", type_investment],
        key_on="properties.departamento",#"feature.id",
        fill_color="YlGnBu",
        fill_opacity=1.0,
        line_opacity=0.2,
        legend_name="Inversión (millions COP)",
    ).add_to(m)

    choropleth.geojson.add_child(tooltip)

    folium.LayerControl().add_to(m)

    m.save('../data/maps_html/map_folium' + title_investment + str(df['anio_corte'].unique()[0]) + '.html')

if __name__ == '__main__':
    # The dffs list will keep, for each year, a DataFrame of the Investment aggregated data:
    dffs = []
    for year in [2016,2017,2018,2019]:
        dffs.append(get_aggr_invest_by_year(year))

    geojson_maps = []
    for i in range(len(dffs)):
        geojson_maps.append(json.loads(dffs[i].to_json()))
    
    for i in range(len(dffs)):
        for type_of_investment in ['inversion_total_millions', 'inversion_conectividad_millions', 'inversion_transformacion_millions']:
            create_map(dffs[i], geojson_maps[i], type_of_investment)
