import streamlit as st
import plotly.graph_objects as go
from utils import *

with st.sidebar:
    st.title('Observatorio de Estadisiticas Delictivas Colombia 2021 👮',anchor='#')
    st.markdown(' ## Esta App permite explorar mapas interactivos con información estadísticas de los delitos reportador por la Policía Nacional de Colombia durante el año 2021')
    st.markdown('---')
    st.markdown('# Autor 👇')
    st.markdown("""
    <style>
    .aligncenter {
    text-align: center;
    
    }
    </style>
    <p class="aligncenter">
    <img src="https://raw.githubusercontent.com/BautistaDavid/Portal_Estadistica_Delictiva_Colombia/main/alien.JPG" style="width: 150px;"/>
    </p>
    """, unsafe_allow_html=True)
    st.markdown('''
    # David Felipe Bautista Bernal
    # [GitHub: BautistaDavid](https://github.com/BautistaDavid)
    # [Twitter: @PipeBau_](https://twitter.com/PipeBau_)
    ''')
    st.markdown('')


titulo = '''
<div><span style="font-family: Helvetica; font-size: 36px;"><strong>Observatorio de Estadisiticas Delictivas  Colombia 2021 &#x1f46e;  &#x1f7e1; &#x1f535; &#x1f534;  </strong></span></div><Br>
'''
st.markdown(titulo,unsafe_allow_html=True)
texto1 = """<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-size: 24px; line-height: 107%; color: black; font-family: Helvetica;">Seleccione el delito del cual quiere visualizar el mapa de frecuencias por departamento durante el a&ntilde;o 2021</span></p>"""

st.markdown(texto1,unsafe_allow_html=True)
delito = st.selectbox('',options=['Abigeato','Amenazas','Delitos Sexuales','Extorsión','Homcicidios en Accidentes de Transito',
                                'Homicidios','Hurto a Comercio','Hurto a Motocicletas','Hurto a Personas','Hurto a Pirateria Terrestre',
                                'Hurto a Residencias','Hurto a Automotores','Hurto a Entidades Financieras','Lesiones en Accidentes de Transito',
                                'Lesiones Personales','Secuestro','Terrorismo','Violencia Intrafamiliar'],)

st.markdown( f'''### Reportes de {delito} Por Departamentos 2021''')
df = data_compiler(delitos(delito))
counties = geo_data_compiler()

locs = df.index
for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']

fig = go.Figure(go.Choroplethmapbox(
                     geojson=counties,
                      locations=locs,
                      z=df.values,
                      colorscale='deep',
                      colorbar_title='Reportes'),)

fig.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=5,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                        width=800, height=1000,
                        margin=dict(l=0,r=50,b=100,t=40,pad=4
    ),)

st.plotly_chart(fig)

