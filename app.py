import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título con estilo animado
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 40px;
        color: #00FFFF;
        text-align: center;
        animation: glow 2s ease-in-out infinite alternate;
        margin-bottom: 20px;
    }

    @keyframes glow {
        from {
            text-shadow: 0 0 10px #00FFFF, 0 0 20px #00FFFF;
        }
        to {
            text-shadow: 0 0 20px #FF00FF, 0 0 30px #FF00FF;
        }
    }

    .sidebar .stSlider, .sidebar .stColorPicker, .sidebar .stSelectbox {
        font-family: 'Arial', sans-serif;
        font-size: 16px;
    }
    </style>
    <div class="main-title">🎨 Tablero de Dibujo Interactivo</div>
    """,
    unsafe_allow_html=True
)

# Sidebar con estilo
with st.sidebar:
    st.markdown("## 🎛️ Propiedades del Tablero")
    drawing_mode = st.selectbox(
        "✏️ Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('📏 Ancho de Línea', 1, 30, 15)
    stroke_color = st.color_picker("🎨 Color de Trazo", "#00FFAA")
    bg_color = "#111111"  # fondo más moderno y elegante

# Lienzo de dibujo
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.2)",  # Color suave para relleno
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=600,
    drawing_mode=drawing_mode,
    key="canvas",
)
