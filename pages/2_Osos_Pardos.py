# -*- coding: utf-8 -*-
'''
    MIARFID - Visualización de Datos - Proyecto

    OSOS PARDOS

    Virginia Casino Sánchez (vcassan@upv.eud.es)

    06/06/2024
'''
#############################################
#                 LIBRERÍAS                 #
#############################################
import streamlit as st
import pandas as pd
import plotly.express as px


#############################################
#                 CONSTANTES                #
#############################################
TITULO = 'Situación de los Osos Pardos en España'

DESC_1 = 'La historia del oso pardo en España es un testimonio de declive y \
    esfuerzos de conservación. Durante la Edad Media, los osos eran comunes \
    en muchas regiones, pero la expansión agrícola, la deforestación y la caza \
    intensiva llevaron a una drástica reducción de su población. Para mediados \
    del siglo XX, la especie estaba al borde de la extinción, con solo unos pocos \
    ejemplares en los Pirineos y la Cordillera Cantábrica. La falta de datos \
    detallados y registros históricos hace difícil trazar una imagen precisa \
    de su evolución en ese periodo.'
DESC_2 = 'Desde finales del siglo XX, los esfuerzos de conservación han permitido \
    una lenta recuperación del oso pardo en España. Programas de protección, la \
    creación de reservas naturales y la reducción de la caza furtiva han \
    contribuido a aumentar su número, aunque la especie sigue siendo vulnerable. \
    A continuación se presenta un gráfico sobre la cantidad de osos que han existido \
    en la Cordillera Cantábrica Oriental, Occidental y Pirineos, evidenciando que \
    los datos disponibles no son muchos. La información sobre su evolución proviene \
    principalmente de estudios recientes, subrayando la necesidad de una vigilancia \
    y protección continuas para asegurar la supervivencia del oso pardo en la península \
    ibérica.'
DESC_3 = 'La información disponible sobre la población de osos pardos en la Cordillera \
    Cantábrica Oriental, Occidental y los Pirineos es limitada. En el gráfico siguiente \
    se muestra la evolución de estas poblaciones, aunque los datos han sido generados \
    sintéticamente para proporcionar una mejor visualización de su tendencia a lo largo \
    del tiempo. Es importante tener en cuenta que estos datos no son completamente \
    precisos, pero sirven para ilustrar el impacto de los esfuerzos de conservación \
    y los desafíos que enfrentan los osos pardos en estas regiones.'

OSOS_DIST = "./data/osos.csv"
OSOS_COMP = './data/osos_datos_sinteticos.csv'

COLORES = ['blueviolet', 'royalblue', 'forestgreen'] 

#############################################
#                  MÉTODOS                  #
#############################################

def grafica_distribucion_osos_pardos(osos_cant, years):
    # Filtrar el DataFrame según el rango de años seleccionado
    filtered_df = osos_cant[(osos_cant['Anyo'] >= years[0]) & 
                            (osos_cant['Anyo'] <= years[1])]

    # Transformar los datos para que sean aptos para plotly.express
    df_melted = filtered_df.melt(id_vars=['Anyo'], 
                                 value_vars=['Cordillera Cantabrica Occidente', 
                                              'Cordillera Cantabrica Oriente', 
                                              'Pirineos'], 
                                 var_name='region', 
                                 value_name='value')

    # Especificar los colores para cada región
    color_discrete_map = {
        'Cordillera Cantabrica Oriente': COLORES[0],
        'Cordillera Cantabrica Occidente': COLORES[1],
        'Pirineos': COLORES[2]
    }

    # Personalizar las etiquetas de hover
    df_melted['Año'] = df_melted['Anyo']
    df_melted['Cantidad'] = df_melted['value']
    df_melted['Región'] = df_melted['region']

    # Crear el gráfico de dispersión con hover_data personalizado
    fig = px.scatter(df_melted, x='Año', y='value', color='region',
                    title='Dispersión de los datos sobre Osos Pardos en España',
                    labels={
                        'year': 'Año',
                        'value': 'Cantidad',
                        'region': 'Región'
                    },
                    category_orders={'region': ['Cordillera Cantabrica Oriente', 
                                                'Cordillera Cantabrica Occidente', 
                                                'Pirineos']},
                    color_discrete_map=color_discrete_map,
                    hover_data={
                        'Año': True,
                        'Cantidad': True,
                        'Región': True
                    }
        )
    
    # Personalizar hovertemplate
    fig.update_traces(hovertemplate='<b>Año</b>: %{x}<br>' +
                              '<b>Cantidad</b>: %{y}<br>' +
                              '<extra></extra>')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

def grafica_evolucion_osos_pardos(df, years):
    # Filtrar el DataFrame según el rango de años seleccionado
    filtered_df = df[(df['Anyo'] >= years[0]) & 
                     (df['Anyo'] <= years[1])]

    # Transformar los datos para que sean aptos para plotly.express
    df_melted = filtered_df.melt(id_vars=['Anyo'], 
                                 value_vars=['Cordillera Cantabrica Occidente', 
                                             'Cordillera Cantabrica Oriente', 
                                             'Pirineos'], 
                                 var_name='region', 
                                 value_name='value')

    # Especificar los colores para cada región
    color_discrete_map = {
        'Cordillera Cantabrica Oriente': COLORES[0],
        'Cordillera Cantabrica Occidente': COLORES[1],
        'Pirineos': COLORES[2]
    }

    # Crear el gráfico de líneas con hovertemplate personalizado
    fig = px.line(df_melted, x='Anyo', y='value', color='region',
                title='Evolución de los Osos Pardos en España',
                labels={
                    'year': 'Año',
                    'value': 'Cantidad de Osos',
                    'region': 'Región'
                },
                category_orders={'region': ['Cordillera Cantabrica Oriente', 
                                            'Cordillera Cantabrica Occidente', 
                                            'Pirineos']},
                color_discrete_map=color_discrete_map
                )

    # Personalizar hovertemplate
    fig.update_traces(hovertemplate='<b>Año</b>: %{x}<br>' +
                                    '<b>Cantidad</b>: %{y}<br>' +
                                    '<extra></extra>')

    # Actualizar el layout para cambiar el título de los ejes
    fig.update_layout(
        xaxis_title='Año',
        yaxis_title='Cantidad',
        legend_title='Región'
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

def seleccion_intervalo_anyos(osos_cant):
    # Añadir un subencabezado a la barra lateral
    st.sidebar.subheader('Gráficas')

    # Crear un control deslizante para seleccionar el rango de años
    anyos = st.sidebar.slider('Selecciona el rango de años', 
                            min_value=int(osos_cant['Anyo'].min()), 
                            max_value=int(osos_cant['Anyo'].max()), 
                            value=(int(osos_cant['Anyo'].min()), 
                                    int(osos_cant['Anyo'].max())))
    
    return anyos

def pagina_osos_pardos(osos_cant, osos_completo):
    # Agregar título de la página
    st.title(TITULO)

    # Agregar descripción
    st.write(DESC_1)
    st.write(DESC_2)

    # Obtener intervalo de años indicado por el usuario
    anyos = seleccion_intervalo_anyos(osos_cant)

    # Añadir gráfica distribución datos
    grafica_distribucion_osos_pardos(osos_cant, anyos)

    # Agregar descripción
    st.write(DESC_3)

    # Añadir gráfica evolución datos
    grafica_evolucion_osos_pardos(osos_completo, anyos)

@st.cache_data
def cargar_datos():
    # Cargar los datos sobre los osos
    osos_cant = pd.read_csv(OSOS_DIST, sep=";")
    osos_completo = pd.read_csv(OSOS_COMP, sep=';')

    return osos_cant, osos_completo

#############################################
#                    MAIN                   #
#############################################

if __name__ == "__main__":
    osos_cant, osos_completo = cargar_datos()
    pagina_osos_pardos(osos_cant, osos_completo)
