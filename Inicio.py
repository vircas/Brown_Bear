# -*- coding: utf-8 -*-
'''
    MIARFID - Visualización de Datos - Proyecto

    PÁGINA DE INICIO

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
IMAGEN = './sources/camino_osos.jpg'
VIDEO = './sources/oseznos_jugando.mp4'

TITULO = 'Situación de los Osos Pardos en España'

DESC_1 = 'Los osos pardos tienen una historia larga y compleja en España, \
    donde han sido parte del ecosistema y la cultura desde tiempos prehistóricos. \
    Tradicionalmente, estos animales estaban distribuidos por gran parte de la \
    Península Ibérica, pero con el paso de los siglos, su población ha disminuido \
    drásticamente debido a la caza, la pérdida de hábitat y el conflicto con actividades humanas.'
DESC_2 = 'Hasta mediados del siglo XX, los osos pardos estaban al borde de la extinción en \
    España. Sin embargo, a partir de los años 80 y 90, se iniciaron varios programas de \
    conservación y protección que han logrado revertir parcialmente esta tendencia. Estos \
    esfuerzos incluyen la creación de reservas naturales, programas de reproducción en \
    cautividad y proyectos para mejorar la coexistencia entre osos y humanos.'
DESC_3 = 'Actualmente, la población de osos pardos en España se concentra principalmente \
    en la Cordillera Cantábrica y, en menor medida, en los Pirineos. Según estimaciones \
    recientes, hay aproximadamente 330 osos en la Cordillera Cantábrica, divididos en dos \
    poblaciones principales: la occidental y la oriental. La población de los Pirineos es \
    mucho más pequeña, con unos pocos individuos procedentes de reintroducciones y \
    movimientos naturales desde la población francesa.'
DESC_4 = 'Aunque la situación de los osos pardos en España ha mejorado, aún enfrentan \
    numerosos desafíos, como la fragmentación del hábitat, la mortalidad por atropellos \
    y el envenenamiento ilegal. La conservación del oso pardo sigue siendo un tema crucial \
    para mantener la biodiversidad y el equilibrio ecológico en los ecosistemas españoles.'

#############################################
#                  MÉTODOS                  #
#############################################

@st.cache_data
def pagina_inicio():
    # Agregar imagen de encabezado
    st.image(IMAGEN, use_column_width=True)

    # Agregar título de la página
    st.title(TITULO)

    # Agregar descripción
    st.write(DESC_1)
    st.write(DESC_2)
    st.write(DESC_3)
    st.write(DESC_4)

    st.video(VIDEO)

#############################################
#                    MAIN                   #
#############################################

if __name__ == '__main__':
    pagina_inicio()