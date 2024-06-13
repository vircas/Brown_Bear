import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para generar datos
def generar_datos(distribucion, size):
    if distribucion == 'Normal':
        return np.random.normal(size=size)
    elif distribucion == 'Uniforme':
        return np.random.uniform(size=size)
    elif distribucion == 'Poisson':
        return np.random.poisson(lam=5, size=size)

# Título de la aplicación
st.title("Visualización de Datos con Streamlit")

# Opciones de selección de distribución
distribuciones = ['Normal', 'Uniforme', 'Poisson']
distribucion_seleccionada = st.selectbox("Selecciona la distribución de datos", distribuciones)

# Control deslizante para seleccionar el tamaño de los datos
size = st.slider("Selecciona el tamaño de los datos", min_value=50, max_value=500, value=100)

# Botón para recargar los datos
if st.button("Generar nuevos datos"):
    data = generar_datos(distribucion_seleccionada, size)
else:
    data = generar_datos(distribucion_seleccionada, size)

# Mostrar la distribución seleccionada
st.subheader(f"Gráfica de Distribución {distribucion_seleccionada}")
fig, ax = plt.subplots()
ax.hist(data, bins=20, color='skyblue', edgecolor='black')
ax.set_title(f'Distribución {distribucion_seleccionada}')
ax.set_xlabel('Valor')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)
