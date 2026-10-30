
import streamlit as st
from PIL import Image

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Aplicaciones de Machine Learning",
    page_icon="🤖",
    layout="wide"
)

st.title("Aplicaciones de Machine Learning")

# ============================================================
# BARRA LATERAL
# ============================================================

with st.sidebar:
    st.subheader("Aplicaciones de Machine Learning")

    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos "
        "para identificar patrones, hacer predicciones y clasificar "
        "información sin ser programados explícitamente para cada tarea."
    )

    st.write(parrafo)
    st.divider()
    st.write("Portafolio de sesiones prácticas de Machine Learning.")

# ============================================================
# ENLACE GENERAL
# ============================================================

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.subheader(
    "En el siguiente enlace puedes encontrar páginas y ejercicios prácticos"
)

st.markdown(f"[Páginas y ejercicios prácticos]({url_ml})")

st.divider()

# ============================================================
# PORTAFOLIO DE 15 SESIONES
# ============================================================
# ASIGNACIÓN MANUAL DE IMÁGENES:
# Cambia el nombre de cada archivo en la propiedad "imagen".
# Ejemplo: "mi_imagen_regresion.png"
# Las imágenes deben estar en el repositorio del proyecto.
# ============================================================

sesiones = [
    {
        "numero": 1,
        "titulo": "Regresión lineal vs. Machine Learning",
        "imagen": "Sesion1.png",
        "descripcion": (
            "Explora un predictor en vivo y compara la regresión lineal "
            "con otros enfoques de Machine Learning."
        ),
        "enlaces": [
            (
                "Sesión 1: Predictor",
                "https://regresionlinealvsmachinelearning-ux6khtkad5zv7kdpveqhqf.streamlit.app/"
            )
        ],
    },
    {
        "numero": 2,
        "titulo": "Regresión logística",
        "imagen": "Sesion2.png",
        "descripcion": (
            "Utiliza un modelo de clasificación para predecir "
            "la compra de un seguro."
        ),
        "enlaces": [
            (
                "Sesión 2: Predictor de seguro",
                "https://regresionlogisticamachinelearning-mysppcdp2few6h8ju6pjjw.streamlit.app/"
            )
        ],
    },
    {
        "numero": 3,
        "titulo": "Algoritmos de clasificación",
        "imagen": "Sesion3.png",
        "descripcion": (
            "Conoce los fundamentos de la clasificación supervisada "
            "y sus aplicaciones prácticas."
        ),
        "enlaces": [
            (
                "Sesión 3: Clasificación",
                "https://algoritmosdeclasificaci-nmachinelearning-nlwtera4y6tmvbnnqxx6f.streamlit.app/"
            )
        ],
    },
    {
        "numero": 4,
        "titulo": "Aplicación con datos reales",
        "imagen": "Sesion4.png",
        "descripcion": (
            "Analiza la relación entre el consumo total "
            "y las horas del día."
        ),
        "enlaces": [
            (
                "Sesión 5: Datos reales",
                "https://machinelearnings4-bun6dzsuxaugenjdlafju7.streamlit.app/"
            )
        ],
    },
    {
        "numero": 5,
        "titulo": "Árbol de decisión",
        "imagen": "Sesion5.png",
        "descripcion": (
            "Explora un árbol de decisión multivariable "
            "para comprender cómo se toman decisiones."
        ),
        "enlaces": [
            (
                "Sesión 6: Árbol de decisión",
                "https://arboldedecisionmachinelearning-7b5cfh4u6f5veywcjyfnet.streamlit.app/"
            )
        ],
    },
    {
        "numero": 6,
        "titulo": "Medidor de energía",
        "imagen": "Sesion6.png",
        "descripcion": (
            "Conoce una aplicación de Machine Learning "
            "relacionada con la medición de energía."
        ),
        "enlaces": [
            (
                "Sesión 7: Medidor de energía",
                "https://medidormachinelearning-qxjm9wjkahunrg2gamyxgw.streamlit.app/"
            )
        ],
    },
    {
        "numero": 7,
        "titulo": "Neurona artificial y redes neuronales",
        "imagen": "Sesion7.png",
        "descripcion": (
            "Aprende cómo funciona una neurona artificial "
            "y cómo se conectan las neuronas para formar redes."
        ),
        "enlaces": [
            (
                "Sesión 7: Neurona artificial",
                "https://neuronaartificialmachinelearning-nrxvratg2vnzcg3ly7k7zd.streamlit.app/"
            )
        ],
    },
    {
        "numero": 8,
        "titulo": "Aplicaciones de redes neuronales",
        "imagen": "Sesion8.png",
        "descripcion": (
            "Explora aplicaciones prácticas y arquitecturas "
            "de redes neuronales artificiales."
        ),
        "enlaces": [
            (
                "Sesión 8: Aplicaciones",
                "https://arquitecturadeneuronas-epgbm5sxkldhcmyyhkxgkj.streamlit.app/"
            )
        ],
    },
    {
        "numero": 9,
        "titulo": "Procesamiento de lenguaje natural",
        "imagen": "Sesion9.png",
        "descripcion": (
            "Explora el procesamiento de texto y las representaciones "
            "vectoriales utilizadas para trabajar con lenguaje."
        ),
        "enlaces": [
            (
                "Sesión 9: Procesamiento de lenguaje natural",
                "https://udi7kunaxeaqq48vchh5hz.streamlit.app/"
            ),
            (
                "Sesión 9: Embeddings",
                "https://embeddingsmachinelearning-jvcizaqtzoz37jmncraecv.streamlit.app/"
            ),
        ],
    },
    {
        "numero": 10,
        "titulo": "Conversores de texto a audio y audio a texto",
        "imagen": "Sesion10.png",
        "descripcion": (
            "Experimenta con la conversión de texto en voz "
            "y la transcripción automática de audio."
        ),
        "enlaces": [
            (
                "Sesión 10: Texto a audio",
                "https://conversortextoaudiomachinelearning-zok75qewrusjand6ncjmgf.streamlit.app/"
            ),
            (
                "Sesión 10: Audio a texto",
                "https://conversoraudiotexto-cq3a63cqvvhe3r2jvkbeud.streamlit.app/"
            ),
        ],
    },
    {
        "numero": 11,
        "titulo": "Redes neuronales recurrentes (RNN)",
        "imagen": "Sesion11.png",
        "descripcion": (
            "Conoce las redes neuronales recurrentes y su capacidad "
            "para procesar secuencias de datos."
        ),
        "enlaces": [
            (
                "Sesión 11: Redes neuronales recurrentes",
                "https://redesneuronalesrecurrentesmachinelearning-jqwsspzyyz725liazpbc.streamlit.app/"
            )
        ],
    },
    {
        "numero": 12,
        "titulo": "Redes recurrentes en procesamiento de lenguaje natural",
        "imagen": "Sesion12.png",
        "descripcion": (
            "Explora cómo las redes recurrentes pueden utilizarse "
            "en tareas de procesamiento del lenguaje natural."
        ),
        "enlaces": [
            (
                "Sesión 12: RNN y lenguaje natural",
                "https://redesneuronalesrecurrentesmachinelearning-jqwsspzyyz725liazpbc.streamlit.app/"
            )
        ],
    },
    {
        "numero": 13,
        "titulo": "Visión computacional",
        "imagen": "Sesion13.png",
        "descripcion": (
            "Explora cómo los sistemas de inteligencia artificial "
            "pueden analizar imágenes e identificar personas."
        ),
        "enlaces": [
            (
                "Sesión 13: Identificador de personas",
                "https://identificadorpersonasmachinelearning-fst84acpdurbsoprqwoaht.streamlit.app/"
            )
        ],
    },
    {
        "numero": 14,
        "titulo": "Inteligencia artificial generativa",
        "imagen": "Sesion14.png",
        "descripcion": (
            "Descubre aplicaciones de inteligencia artificial generativa "
            "y herramientas relacionadas con el análisis visual."
        ),
        "enlaces": [
            (
                "Sesión 14: IA generativa",
                "https://iagenerativamachinelearning-afec8ndwnkfglkfstfktjy.streamlit.app/"
            ),
            (
                "Sesión 14: Aplicación de visión artificial",
                "https://visionmachinelearning-lr8tjdfisdbq5rbsstyyvh.streamlit.app/"
            ),
        ],
    },
]

# ============================================================
# VISUALIZACIÓN AUTOMÁTICA EN TRES COLUMNAS
# ============================================================

columnas = st.columns(3)

for indice, sesion in enumerate(sesiones):

    with columnas[indice % 3]:

        st.subheader(
            f"Sesión {sesion['numero']}. {sesion['titulo']}"
        )

        # Cargar imagen asignada manualmente
        try:
            imagen = Image.open(sesion["imagen"])
            st.image(imagen, width=190)

        except FileNotFoundError:
            st.info(
                f"Imagen pendiente: {sesion['imagen']}"
            )

        except Exception as error:
            st.warning(
                f"No se pudo cargar {sesion['imagen']}: {error}"
            )

        # Descripción de la sesión
        st.write(sesion["descripcion"])

        # Mostrar todos los enlaces de la sesión
        for nombre, url in sesion["enlaces"]:
            st.markdown(f"[{nombre}]({url})")

        st.divider()

# ============================================================
# PIE DE PÁGINA
# ============================================================

st.caption(
    "Portafolio educativo de Aplicaciones de Machine Learning."
)
