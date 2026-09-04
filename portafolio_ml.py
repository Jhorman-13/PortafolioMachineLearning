import streamlit as st
from PIL import Image

st.title("Aplicaciones de Machine Learning.")

with st.sidebar:
    st.subheader("Aplicaciones de Machine Learning.")
    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.write(parrafo)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ml})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Regresión Linear vs Machine Learning")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("Sesion1.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un predictor en vivo")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://regresionlinealvsmachinelearning-ux6khtkad5zv7kdpveqhqf.streamlit.app/"
    st.write(f"Sesión 1: [Enlace]({url})")

    

with col2:
    st.subheader("Regresión lógistica")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("Sesion2.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un predictor de compra de seguro.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://regresionlogisticamachinelearning-mysppcdp2few6h8ju6pjjw.streamlit.app/"
    st.write(f"Sesión 2: [Enlace]({url})")

with col3:
    st.subheader("Algoritmos de clasificación.")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("Sesion3.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos la clasificación supervisada.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://algoritmosdeclasificaci-nmachinelearning-nlwtera4y6tmvbnnqxx6f.streamlit.app/"
    st.write(f"Sesión 4: [Enlace]({url})")
