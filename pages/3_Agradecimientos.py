# -*- coding: utf-8 -*-
'''
    MIARFID - Visualización de Datos - Proyecto

    AGRADECIMIENTOS

    Virginia Casino Sánchez (vcassan@upv.eud.es)

    06/06/2024
'''
#############################################
#                 LIBRERÍAS                 #
#############################################
import streamlit as st

#############################################
#                 CONSTANTES                #
#############################################
TITULO = 'Agradecimientos'

DESC_1 = 'Agradecer a todos los organismos y entidades \
    involucradas en la conservación del oso pardo en España. Su labor \
    en la recopilación de datos y la ejecución de proyectos para proteger \
    a esta especie es fundamental para los esfuerzos de conservación a \
    nivel nacional.'
DESC_2 = 'La importancia de su trabajo en el estudio y protección de los \
    osos pardos no puede subestimarse, y es crucial para asegurar la \
    preservación de nuestra biodiversidad. Por último, apreciar el compromiso \
    continuo de todas las partes interesadas en abordar este preocupante tema.'

IMAGEN_OSOS = './sources/osos_felices.jpg'
IMAGEN_ICONOS = './sources/iconos.png'

#############################################
#                  MÉTODOS                  #
#############################################

@st.cache_data
def pagina_agradecimientos():
    # Agregar título de la página
    st.title(TITULO)

    # Agregar descripción
    st.write(DESC_1)
    st.write(DESC_2)

    # Agregar imagen de encabezado
    st.image(IMAGEN_OSOS, use_column_width=True)
    st.image(IMAGEN_ICONOS, use_column_width=True)

#############################################
#                    MAIN                   #
#############################################

if __name__ == "__main__":
    pagina_agradecimientos()
