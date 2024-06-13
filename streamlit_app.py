import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import base64

# Función para generar datos
def generar_datos(distribucion, size):
    if distribucion == 'Normal':
        return np.random.normal(size=size)
    elif distribucion == 'Uniforme':
        return np.random.uniform(size=size)
    elif distribucion == 'Poisson':
        return np.random.poisson(lam=5, size=size)

# Función para añadir fondo de pantalla
def set_background(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/jpg;base64,{bin_str}");
    background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Establecer fondo de pantalla
set_background('tu_imagen_de_fondo.jpg')

# Inicializar el estado de la sesión si no está definido
if 'data' not in st.session_state:
    st.session_state.data = generar_datos('Normal', 100)
    st.session_state.distribucion = 'Normal'
    st.session_state.size = 100

# Título de la aplicación
st.title("Visualización de Datos con Streamlit")

# Opciones de selección de distribución
distribuciones = ['Normal', 'Uniforme', 'Poisson']
distribucion_seleccionada = st.selectbox("Selecciona la distribución de datos", distribuciones, index=distribuciones.index(st.session_state.distribucion))

# Control deslizante para seleccionar el tamaño de los datos
size = st.slider("Selecciona el tamaño de los datos", min_value=50, max_value=500, value=st.session_state.size)

# Botón para recargar los datos
if st.button("Generar nuevos datos"):
    st.session_state.data = generar_datos(distribucion_seleccionada, size)
    st.session_state.distribucion = distribucion_seleccionada
    st.session_state.size = size

# Mostrar la distribución seleccionada
st.subheader(f"Gráfica de Distribución {st.session_state.distribucion}")
fig, ax = plt.subplots()
ax.hist(st.session_state.data, bins=20, color='skyblue', edgecolor='black')
ax.set_title(f'Distribución {st.session_state.distribucion}')
ax.set_xlabel('Valor')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)
