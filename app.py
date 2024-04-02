import pandas as pd
import streamlit as st
from PIL import Image


st.title('Análisis de datos de Cbas')
image = Image.open('Panel Control.png')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   st.subheader('Estadísticos básicos de los sensores')
   st.dataframe(df1["humedad ESP32"].describe())
else:
 st.warning('Necesitas cargar un archivo csv excel.')
