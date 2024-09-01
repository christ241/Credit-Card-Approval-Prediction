import streamlit as st
import eda
import pred
from PIL import Image

image = Image.open('neoventure.png')

# Display the sidebar content
st.sidebar.header('Neoventure')
st.sidebar.image(image, use_column_width=True)

# Page selection in the sidebar
page = st.sidebar.selectbox('Pilih Halaman', ('EDA', 'Prediction'))

# Render the selected page
if page == 'EDA':
    eda.run()
else:
    pred.run()
