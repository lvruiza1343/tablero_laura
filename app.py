
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Estilos coquette: pastel, elegante y dulce
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap');

    .main-title {
        font-family: 'Quicksand', sans-serif;
        font-size: 42px;
        color: #AF7AC5;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .sidebar .stSelectbox label,
    .sidebar .stSlider label,
    .sidebar .stColorPicker label {
        font-family: 'Quicksand', sans-serif;
        color: #7D5A8C;
        font-size: 17px;
    }

    .sidebar .stSelectbox,
    .sidebar .stSlider,
    .sidebar .stColorPicker {
        background-color: #FDEEF4;
        border-radius: 10px;
        padding: 8px;
    }

    .sidebar {
        background-color: #FFF5FB;
    }

    </style>
    <div class="main-title">🎀 Tablero de Dibujo</div>
    """,
    unsafe_allow_html=True
)

# Configuración del tablero en la barra lateral
with st.sidebar:
    st.markdown("### 🧁 Personaliza tu dibujo")
    drawing_mode = st.selectbox(
        "Herramienta de dibujo",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    stroke_width = st.slider('Ancho del trazo', 1, 30, 10)
    stroke_color = st.color_picker("Color del trazo", "#D291BC")
    bg_color = "#FFF5FB"  # rosado pastel claro

# Lienzo principal con tonos suaves
canvas_result = st_canvas(
    fill_color="rgba(242, 201, 251, 0.2)",  # relleno suave y adorable
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas",
)

