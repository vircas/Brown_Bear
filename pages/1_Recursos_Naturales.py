# -*- coding: utf-8 -*-
'''
    MIARFID - Visualización de Datos - Proyecto

    RECURSOS NATURALES

    Virginia Casino Sánchez (vcassan@upv.eud.es)

    06/06/2024
'''
#############################################
#                 LIBRERÍAS                 #
#############################################
import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

#############################################
#                 CONSTANTES                #
#############################################
TITULO = 'Recursos Naturales en España'

DESC_1 = 'Los recursos naturales como bosques, montañas y ríos son \
    esenciales para la supervivencia de los osos pardos, proporcionándoles \
    refugio, áreas para la hibernación y la crianza, así como una variedad \
    de alimentos necesarios para su dieta omnívora. Estos espacios naturales \
    permiten a los osos acumular las reservas de grasa necesarias, especialmente \
    antes de la hibernación, y ofrecen corredores ecológicos esenciales para la \
    dispersión y la migración, que son cruciales para mantener la diversidad \
    genética y la salud de la población.'
DESC_2 = 'La protección de estos hábitats no solo beneficia a los osos, sino \
    que también es vital para la salud general del ecosistema, ya que los osos \
    actúan como especies indicadoras de su estado. Además, los entornos naturales \
    saludables fomentan el ecoturismo, generando ingresos y elevando la conciencia \
    ambiental, lo cual promueve una coexistencia sostenible entre las comunidades \
    humanas y la vida silvestre, asegurando así la conservación de estos espacios \
    para las futuras generaciones.'
DESC_3 = 'A continuación, encontrará un mapa interactivo que detalla la cantidad \
    de recursos naturales por provincias. En el panel de la izquierda, puede \
    seleccionar específicamente el tipo de recurso natural que deseas explorar. \
    Esta herramienta visual le permite comprender con precisión cómo están distribuidos \
    los recursos esenciales para la vida silvestre, como los osos pardos, y analizar \
    su importancia tanto ecológica como económica a nivel provincial.'

DESC_4 = 'Posteriormente, se presenta un análisis de los municipios que cuentan \
    con la mayor cantidad de recursos naturales dentro de una comunidad autónoma. \
    Este estudio destaca aquellos municipios que sobresalen por su riqueza natural, \
    lo cual es un indicador clave para el desarrollo sostenible y la conservación del \
    medio ambiente en la región.'

DESC_5 = 'Además, puede interactuar con el sistema indicando la comunidad autónoma \
    que desea visualizar, así como la cantidad de municipios que le gustaría ver en \
    un formato de TOP (por ejemplo, TOP 5, TOP 10, etc.). También puede especificar \
    si prefiere que la lista se muestre en orden ascendente o descendente.'

CENTRO_ESP = [40.0, -2.8] 

PROVINCIAS_FILE = './data/provincias.geojson'
MUNICIPIOS_FILE = './data/municipios.csv'
CCAA_FILE = './data/ccaa.csv'

#############################################
#                  MÉTODOS                  #
#############################################

def seleccionar_tipo_recurso(gdf):
    # Quitar las columnas que no se desean mostrar al usuario
    excluded_keys = {'NAMEUNIT', 'CODNUT2', 'geometry'} 
    variables = [key for key in gdf.columns if key not in excluded_keys]

    # Interfaz de usuario para seleccionar la variable 
    st.sidebar.subheader('Mapa')

    # Añadir un selectbox para seleccionar la variable
    valor_predeterminado = "Total Espacios Naturales"
    indice_predeterminado = variables.index(valor_predeterminado)

    variable = st.sidebar.selectbox('Tipo de recurso natural:',
                                    variables, index = indice_predeterminado)

    return variable

def pintar_mapa_recursos_naturales(gdf):
    # Variable seleccionada por el usuario
    variable = seleccionar_tipo_recurso(gdf)

    # Añadir 0 en lugar de valores nulos en la variable seleccionada
    gdf[variable] = gdf[variable].fillna(0)

    # Emplear solo las variables necesarias para el mapa
    gdf = gdf[['NAMEUNIT', variable, 'geometry']]

    # Color en base a que recurso natural es
    if variable == 'Extensión':
        color = "YlOrBr"
    elif variable == 'Reserva Fluvial' or \
            variable == 'Zonas Húmedas' or \
            variable == 'Humedal Protegido' or \
            variable == 'Área Marina Protegida':
        color = "Blues"
    else:
        color = "Greens"

    # Crear el mapa base
    mapa = folium.Map(location = CENTRO_ESP, 
                      scrollWheelZoom = False,
                      zoom_start = 6)  

    # Añadir el GeoJson y crear el mapa coroplético usando el GeoJSON limpio
    choropleth = folium.Choropleth(
        geo_data = gdf,
        data = gdf,
        columns = ['NAMEUNIT', variable],
        key_on = 'feature.properties.NAMEUNIT',
        fill_color = color,
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = variable
    )
    choropleth.geojson.add_to(mapa)

    # Formateo avanzado para tooltip usando HTML
    tooltip = folium.features.GeoJsonTooltip(
        fields=['NAMEUNIT', variable],
        aliases=['Provincia:', variable],
        style=('background-color: white; color: #333333; \
                font-family: Arial; font-size: 12px; padding: 10px;'),
        localize=True,
        labels=True,
        sticky=False
    )

    # Añadir tooltip al mapa
    choropleth.geojson.add_child(tooltip)

    # Mostrar el mapa en Streamlit indicando dimensiones
    st_folium(mapa, width=700, height=500)

def seleccionar_parametros_ccaa_mun(data):
    # Crear una selección de comunidad autónoma
    comunidades = data['NAMEUNIT_CCAA'].unique()
    st.sidebar.subheader('Gráfico de barras')

    selected_comunidad = st.sidebar.selectbox('Comunidad Autónoma:', 
                                              comunidades)

    # Filtrar los datos por la comunidad autónoma seleccionada
    filtered_data = data[data['NAMEUNIT_CCAA'] == selected_comunidad]

    # Seleccionar el número de municipios a mostrar
    num_municipios = st.sidebar.slider('Número de municipios:', 
                                        1, len(filtered_data), 10)

    # Seleccionar el orden
    order = st.sidebar.radio('Ordenar por', ('Ascendente', 'Descendente'), index = 1)

    # Ordenar y seleccionar los municipios
    if order == 'Ascendente':
        top_municipios = filtered_data.nsmallest(num_municipios, 'Total Espacios Naturales')
    else:
        top_municipios = filtered_data.nlargest(num_municipios, 'Total Espacios Naturales')

    return order, num_municipios, selected_comunidad, top_municipios

def pintar_grafica_ccaa_municipio(data):
    # Variables seleccionadas por el usuario
    order, num_municipios, selected_comunidad, top_municipios = seleccionar_parametros_ccaa_mun(data)

    # Crear el gráfico de barras
    fig = px.bar(top_municipios, 
                 x='NAMEUNIT', 
                 y='Total Espacios Naturales', 
                 title=f'Top {num_municipios} municipios en {selected_comunidad} (Orden {order})',
                 color_discrete_sequence=['green'])

    # Asegurar que el límite mínimo del eje Y sea 0
    fig.update_yaxes(rangemode="tozero")

    # Modificar los ejes
    fig.update_xaxes(title_text='Municipios')
    fig.update_yaxes(title_text='Total Espacios Naturales')

    # Personalizar hovertemplate
    fig.update_traces(hovertemplate='<b>Provincia</b>: %{x}<br>' +
                                    '<b>Cantidad</b>: %{y}<br>' +
                                    '<extra></extra>')

    # Mostrar el gráfico
    st.plotly_chart(fig)


def pagina_recursos_naturales(gdf, data_mun_ccaa):
    # Agregar título de la página
    st.title(TITULO)

    # Agregar descripción
    st.write(DESC_1)
    st.write(DESC_2)
    st.write(DESC_3)

    # Añadir mapa recursos naturales
    pintar_mapa_recursos_naturales(gdf)

    # Agregar descripción
    st.write(DESC_4)
    st.write(DESC_5)

    # Añadir gráfico recursos naturales por comunidad autónoma / municipio
    pintar_grafica_ccaa_municipio(data_mun_ccaa)

@st.cache_data
def cargar_datos():
    # Cargar GeoJSON con GeoPandas
    gdf = gpd.read_file(PROVINCIAS_FILE, driver='GeoJSON')

    # Cargar CSVs con Pandas (municipios y comunidades autónomas)
    data_municipios = pd.read_csv(MUNICIPIOS_FILE)
    data_ccaa = pd.read_csv(CCAA_FILE)

    # Combinar los datasets usando CODNUT2
    data_mun_ccaa = data_municipios.merge(data_ccaa[['CODNUT2', 'NAMEUNIT']], 
                                          on='CODNUT2', how='left', 
                                          suffixes=('', '_CCAA'))
    # Seleccionar solo variables necesarias
    data_mun_ccaa = data_mun_ccaa[['NAMEUNIT', 'Total Espacios Naturales', 'NAMEUNIT_CCAA']]
    
    # Filtrar solo los valores positivos
    data_mun_ccaa = data_mun_ccaa[data_mun_ccaa['Total Espacios Naturales'] >= 0]

    return gdf, data_mun_ccaa

#############################################
#                    MAIN                   #
#############################################

if __name__ == "__main__":
    gdf, data_mun_ccaa = cargar_datos()
    pagina_recursos_naturales(gdf, data_mun_ccaa)
