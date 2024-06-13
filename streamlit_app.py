import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Visualización de Datos con Streamlit")

# Generación de datos falsos
np.random.seed(42)
data1 = np.random.normal(size=100)
data2 = np.random.uniform(size=100)
data3 = np.random.poisson(lam=5, size=100)

# Gráfica 1: Distribución Normal
st.subheader("Gráfica 1: Distribución Normal")
fig1, ax1 = plt.subplots()
ax1.hist(data1, bins=20, color='skyblue', edgecolor='black')
ax1.set_title('Distribución Normal')
ax1.set_xlabel('Valor')
ax1.set_ylabel('Frecuencia')
st.pyplot(fig1)

# Gráfica 2: Distribución Uniforme
st.subheader("Gráfica 2: Distribución Uniforme")
fig2, ax2 = plt.subplots()
ax2.hist(data2, bins=20, color='salmon', edgecolor='black')
ax2.set_title('Distribución Uniforme')
ax2.set_xlabel('Valor')
ax2.set_ylabel('Frecuencia')
st.pyplot(fig2)

# Gráfica 3: Distribución de Poisson
st.subheader("Gráfica 3: Distribución de Poisson")
fig3, ax3 = plt.subplots()
ax3.hist(data3, bins=20, color='lightgreen', edgecolor='black')
ax3.set_title('Distribución de Poisson')
ax3.set_xlabel('Valor')
ax3.set_ylabel('Frecuencia')
st.pyplot(fig3)
