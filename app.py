import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado obligatorio de la aplicación
st.header('Cuadro de Mandos de Anuncios de Autos')
st.write('Selecciona los gráficos que deseas visualizar para analizar el conjunto de datos:')

# --- SECCIÓN DE CASILLAS DE VERIFICACIÓN ---

# Casilla para el histograma
build_histogram = st.checkbox('Construir un histograma')

# Casilla para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# --- LÓGICA DE VISUALIZACIÓN ---

# 1. Si el usuario selecciona el Histograma
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear histograma del odómetro
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro (Kilometraje)')
    
    # Mostrar en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# 2. Si el usuario selecciona el Gráfico de Dispersión
if build_scatter:
    st.write('Creación de un gráfico de dispersión para comparar el Odómetro vs Precio')
    
    # Crear gráfico de dispersión (usando modo 'markers' para puntos sueltos)
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'], 
        y=car_data['price'], 
        mode='markers',
        marker=dict(opacity=0.5) # Opacidad para ver mejor la concentración de datos
    )])
    
    fig_scatter.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro (Millas)',
        yaxis_title='Precio (USD)'
    )
    
    # Mostrar en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)