#Libreri­as
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cufflinks as cf
import plotly.offline as pyo
import altair as alt
from stqdm import stqdm
import plotly.graph_objects as go

# Configurar cufflinks para trabajar con plotly
cf.go_offline()

#----------------------------------------CARGA DE DATOS------------------------------------------

path = 'BDEx.xlsx'
dataKW = pd.read_excel(path)

dataORG = pd.read_excel(path,sheet_name='organic')

dataLSS = pd.read_excel(path,sheet_name='landingSS')
dataLUSR = pd.read_excel(path,sheet_name='landingUSR')

dataCDUSR = pd.read_excel(path,sheet_name='ciudadUSR')
dataCDNUSR = pd.read_excel(path,sheet_name='ciudadNUSR')

dataAGEUSR = pd.read_excel(path,sheet_name='edadUSR')
dataAGENUSR = pd.read_excel(path,sheet_name='edadNUSR')

dataGRUSR = pd.read_excel(path,sheet_name='generoUSR')
dataGRNUSR = pd.read_excel(path,sheet_name='generoNUSR')

dataDPS = pd.read_excel(path,sheet_name='dispositivos')

#----------------------------------- IMPRESIONES Y CLICS POR KEYWORD---------------------------------------------
# Crear el gráfico de barras para Impresiones
bar_chart = dataKW.iplot(
    x='Keyword', y='Impresiones',
    kind='bar',
    title=' ',
    linecolor='#003618',
    colors='#016730',
    yTitle='Impresiones',
    xTitle='Keyword',
    showlegend=False,
    asFigure=True
)

# Crear el gráfico de línea para Clics
line_chart = dataKW.iplot(
    x='Keyword', y='Clics',
    kind='line',
    mode='markers+lines',
    title='',
    linecolor='#D9042B',
    colors='#D9042B',
    yTitle='Clics',
    xTitle='Keyword',
    showlegend=True,
    asFigure=True
)

# Combinamos ambos gráficos
combined_chart = bar_chart
combined_chart.add_trace(line_chart.data[0])

# Agregar etiquetas de datos para los clics
for i, row in enumerate(dataKW.iterrows()):
    keyword = row[1]['Keyword']
    clics = row[1]['Clics']
    combined_chart.add_annotation(
        x=keyword,
        y=clics,
        text=str(clics),
        showarrow=False,  # Sin flechas
        font=dict(size=10),
        align='center',
        yshift=5
    )

# Actualizar diseño para eliminar bordes y ajustar etiquetas
combined_chart.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=dataKW['Keyword'],
        ticktext=[f'{kw}' for kw in dataKW['Keyword']],
        tickangle=45
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=True
    ),
    xaxis_title=None,
    yaxis_title=None,
    showlegend=True,
    plot_bgcolor='white',
    paper_bgcolor='white'
)


#---------------------------------------------- TRAFICO ORGANICO USUARIOS ------------------------------------------------
# Crear grafico de pastel basado en la columna 'Usuarios'
pie_chartORGU = dataORG.iplot(
    labels='Trafico',
    values='Total_de_usuarios',
    kind='pie',
    hole=0.3,  # AÃ±ade un agujero al centro para estilo donut si se desea
    colors=['#016730', '#548235', '#ABD66C', '#D9042B'],
    showlegend=True,
    asFigure=True
)

# Actualizar el diseno del grafico para eliminar li­neas y bordes innecesarios
pie_chartORGU.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    title_text='',
    plot_bgcolor='white',
    paper_bgcolor='white'
)
#---------------------------------------------- TRAFICO ORGANICO sesiones ------------------------------------------------
# Crear grafico de pastel basado en la columna 'Usuarios'
pie_chartORGS = dataORG.iplot(
    labels='Trafico',
    values='Sesiones',
    kind='pie',
    hole=0.3,  # AÃ±ade un agujero al centro para estilo donut si se desea
    colors=['#ABD66C','#02C259','#D9042B','#016730'],
    showlegend=True,
    asFigure=True
)

# Actualizar el diseno del grafico para eliminar li­neas y bordes innecesarios
pie_chartORGS.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    title_text='',
    plot_bgcolor='white',
    paper_bgcolor='white'
)


#---------------------------------------------- LANDING PAGES (SESIONES) ------------------------------------------------
# Crear grafico de pastel basado en la columna 'Sesiones'
pie_chartLSS = dataLSS.iplot(
    labels='Landing_page',
    values='Sesiones',
    kind='pie',
    title=' ',
    hole=0.3,  # AÃ±ade un agujero al centro para estilo donut, puede eliminarse si no se desea
    colors=['#003618', '#016730', '#02C259', '#55FDA1', '#548235', '#88BF36', '#ABD66C', '#686868', '#C7C7C9', '#D9042B'],
    showlegend=True,
    asFigure=True
)

# Actualizar el diseno del grafico para eliminar li­neas y bordes innecesarios
pie_chartLSS.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)



#---------------------------------------------- LANDING PAGES (USUARIOS) ------------------------------------------------
# Crear grafico de pastel basado en la columna 'Usuarios'
pie_chartLUSR = dataLUSR.iplot(
    labels='Landing_page1',
    values='Usuarios',
    kind='pie',
    title=' ',
    hole=0.3,  # AÃ±ade un agujero al centro para estilo donut, puede eliminarse si no se desea
    colors = ['#D9042B', '#C7C7C9', '#686868', '#ABD66C', '#88BF36', '#548235', '#55FDA1', '#02C259', '#016730', '#003618'],
    showlegend=True,
    asFigure=True
)

# Actualizar el diseno del grafico para eliminar li­neas y bordes innecesarios
pie_chartLUSR.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)


#---------------------------------------------- CIUDADES PRINCIPALES (USUARIOS) ------------------------------------------
dataCDUSR=dataCDUSR[dataCDUSR['Ciudad'] != 'Otros']
# Crear grafico de barras basado en la columna 'Usuarios totales'
bar_chartCDUSR = dataCDUSR.iplot(
    x='Ciudad',
    y='Usuarios totales',
    kind='bar',
    title=' ',
    colors=['#88BF36'],
    showlegend=False,
    asFigure=True
)

# Actualizar el diseÃ±o del grÃ¡fico para mejorar la visualizaciÃ³n
bar_chartCDUSR.update_layout(
    xaxis=dict(
        tickangle=45,  # Inclinar las etiquetas para mejor lectura
        showgrid=False, 
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    yaxis=dict(
        showgrid=True,  # Mantener la cuadrÃ­cula en el eje Y para referencia
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)

#---------------------------------------------- CIUDADES PRINCIPALES (NUEVOS USUARIOS) ------------------------------------------
# Crear grafico de barras basado en la columna 'Usuarios totales'
bar_chartCDNUSR = dataCDNUSR.iplot(
    x='Ciudad',
    y='Nuevos_usuarios',
    kind='bar',
    title=' ',
    colors=['#548235'],
    showlegend=False,
    asFigure=True
)

# Actualizar el diseno del grafico para mejorar la visualizacion
bar_chartCDNUSR.update_layout(
    xaxis=dict(
        tickangle=45,  # Inclinar las etiquetas para mejor lectura
        showgrid=False, 
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    yaxis=dict(
        showgrid=True,  # Mantener la cuadri­cula en el eje Y para referencia
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)

#---------------------------------------------- EDAD USUARIOS ------------------------------------------

# Crear grafico de barras basado en la columna 'Usuarios_totales'
bar_chartAGEUSR = dataAGEUSR.iplot(
    x='Edad',
    y='Usuarios_totales',
    kind='bar',
    title=' ',
    colors=['#016730'],
    showlegend=False,
    asFigure=True
)

# Actualizar el diseno del grafico para mejorar la visualizacion
bar_chartAGEUSR.update_layout(
    xaxis=dict(
        tickangle=45,  # Inclinar las etiquetas para mejor lectura
        showgrid=False, 
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    yaxis=dict(
        showgrid=True,  # Mantener la cuadricula en el eje Y para referencia
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)
#---------------------------------------------- EDAD NUEVOS USUARIOS ------------------------------------------


bar_chartAGENUSR = dataAGENUSR.iplot(
    x='Edad',
    y='Nuevos_usuarios',
    kind='bar',
    title=' ',
    colors=['#D9042B'],
    showlegend=False,
    asFigure=True
)


bar_chartAGENUSR.update_layout(
    xaxis=dict(
        tickangle=45,  # Inclinar las etiquetas para mejor lectura
        showgrid=False, 
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    yaxis=dict(
        showgrid=True,  # Mantener la cuadrÃ­cula en el eje Y para referencia
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)

#---------------------------------------------- GENERO USUARIOS------------------------------------------

# Crear grafico de barras basado en la columna 'Usuarios_totales'
bar_chartGRUSR = dataGRUSR.iplot(
    x='Genero',
    y='Usuarios_totales',
    kind='bar',
    title=' ',
    colors=['#D9042B'],
    showlegend=False,
    asFigure=True
)

# Actualizar el diseÃ±o del grÃ¡fico para mejorar la visualizaciÃ³n
bar_chartGRUSR.update_layout(
    xaxis=dict(
        tickangle=0,  # Ãngulo de las etiquetas en el eje X
        showgrid=False, 
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    yaxis=dict(
        showgrid=True,  # Mantener la cuadrÃ­cula en el eje Y para referencia
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)
#---------------------------------------------- GENERO NUEVOS USUARIOS------------------------------------------

# Crear grafico de barras basado en la columna 'Usuarios_totales'
bar_chartGRNUSR = dataGRNUSR.iplot(
    x='Genero',
    y='Nuevos_usuarios',
    kind='bar',
    title=' ',
    colors=['#ABD66C'],
    showlegend=False,
    asFigure=True
)

# Actualizar el diseño del grafico para mejorar la visualizacion
bar_chartGRNUSR.update_layout(
    xaxis=dict(
        tickangle=0,  # Ãngulo de las etiquetas en el eje X
        showgrid=False,
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    yaxis=dict(
        showgrid=True,  # Mantener la cuadrÃ­cula en el eje Y para referencia
        zeroline=False, 
        showline=False, 
        showticklabels=True
    ),
    title_text=' ',
    plot_bgcolor='white',
    paper_bgcolor='white'
)


#-----------------------------------------Dashboard-----------------------------------------------

# Configuración de la página
st.set_page_config(
    page_title="HDI SEGUROS Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS para el color de fondo de la página, la barra lateral, centrar los contenedores y los títulos de los gráficos
st.markdown("""
    <style>
    body {
        background-color: #d4f1c2; /* Color de fondo de la página (verde claro) */
    }
    .css-18e3th9 {
        background-color: #2a7f2e; /* Color de fondo de la barra lateral (verde fuerte) */
    }
    .centered-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    .centered-container > div {
        width: 100%;
        max-width: 1200px; /* Ajusta este valor según el ancho máximo deseado */
    }
    .logo {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 1000; /* Asegura que el logo esté por encima de otros elementos */
    }
    .chart-title {
        border: 2px solid #2a7f2e; /* Borde verde alrededor del título */
        border-radius: 5px; /* Bordes redondeados del recuadro */
        padding: 10px; /* Espacio alrededor del texto dentro del recuadro */
        background-color: #2a7f2e; /* Fondo verde para el recuadro */
        color: #ffffff; /* Color del texto (blanco) */
        text-align: center; /* Centrar el texto */
        font-size: 18px; /* Tamaño de la fuente del título */
        font-weight: bold; /* Hacer el texto en negrita */
        margin-bottom: 10px; /* Espacio debajo del recuadro */
    }
    .header-image {
        display: flex;
        justify-content: center;
        margin: 20px 0; /* Espacio arriba y abajo de la imagen */
    }
    .footer-text {
    position: absolute;
    bottom: 10px;
    left: 0;
    right: 0;
    text-align: center;
    color: #FFFFFF;
    font-size: 14px;
}
    </style>
""", unsafe_allow_html=True)

# Agregar la imagen centrada con un tamaño mayor
st.markdown("""
    <div class="header-image">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT53FrKyyITXSUoDOeeJmzFTA2M3twHgULp2Q&s" alt="Encabezado" width="800"/>
    </div>
""", unsafe_allow_html=True)

# Contenedor para la gráfica combinada centrado
container1 = st.container()

with container1:
    st.markdown('<div class="chart-title">Impresiones y Clics por Keyword</div>', unsafe_allow_html=True)
    st.plotly_chart(combined_chart, use_container_width=True)

# Agregar una barra lateral
st.sidebar.markdown('<h1 style="color: #ffffff;">Filtros</h1>', unsafe_allow_html=True)
filtro = st.sidebar.selectbox("Filtrar por:", ["Usuarios", "Sesiones"])
st.sidebar.markdown("""
    <div class="footer-text">
        Fuente: Google Analytics & Google Search Consoles
    </div>
""", unsafe_allow_html=True)

# Contenedor para las gráficas inferiores
container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        if filtro == "Usuarios":
            st.markdown('<div class="chart-title">Tráfico Orgánico - Usuarios</div>', unsafe_allow_html=True)
            st.plotly_chart(pie_chartORGU, use_container_width=True)
        elif filtro == "Sesiones":
            st.markdown('<div class="chart-title">Tráfico Orgánico - Sesiones</div>', unsafe_allow_html=True)
            st.plotly_chart(pie_chartORGS, use_container_width=True)
    with col4:
        if filtro == "Usuarios":
            st.markdown('<div class="chart-title">Landing Page - Usuarios</div>', unsafe_allow_html=True)
            st.plotly_chart(pie_chartLUSR, use_container_width=True)
        elif filtro == "Sesiones":
            st.markdown('<div class="chart-title">Landing Page - Sesiones</div>', unsafe_allow_html=True)
            st.plotly_chart(pie_chartLSS, use_container_width=True)

# Tercer contenedor con las nuevas gráficas
container3 = st.container()
col5, col6 = st.columns(2)

# Agregar el segundo filtro
filtro_contenedor3 = st.sidebar.selectbox("Filtrar por:", ["Usuarios Totales", "Nuevos Usuarios"])

with container3:
    with col5:
        if filtro_contenedor3 == "Usuarios Totales":
            st.markdown('<div class="chart-title">Género - Usuarios Totales</div>', unsafe_allow_html=True)
            st.plotly_chart(bar_chartGRUSR, use_container_width=True)
        elif filtro_contenedor3 == "Nuevos Usuarios":
            st.markdown('<div class="chart-title">Género - Nuevos Usuarios</div>', unsafe_allow_html=True)
            st.plotly_chart(bar_chartGRNUSR, use_container_width=True)
    with col6:
        if filtro_contenedor3 == "Usuarios Totales":
            st.markdown('<div class="chart-title">Edad - Usuarios Totales</div>', unsafe_allow_html=True)
            st.plotly_chart(bar_chartAGEUSR, use_container_width=True)
        elif filtro_contenedor3 == "Nuevos Usuarios":
            st.markdown('<div class="chart-title">Edad - Nuevos Usuarios</div>', unsafe_allow_html=True)
            st.plotly_chart(bar_chartAGENUSR, use_container_width=True)

# Cuarto contenedor con la última gráfica centrado
container4 = st.container()

with container4:
    if filtro_contenedor3 == "Usuarios Totales":
        st.markdown('<div class="chart-title">Principales Ciudades - Usuarios Totales </div>', unsafe_allow_html=True)
        st.plotly_chart(bar_chartCDUSR, use_container_width=True)
    elif filtro_contenedor3 == "Nuevos Usuarios":
        st.markdown('<div class="chart-title">Principales Ciudades- Nuevos Usuarios</div>', unsafe_allow_html=True)
        st.plotly_chart(bar_chartCDNUSR, use_container_width=True)

