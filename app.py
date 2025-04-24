import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Estilos personalizados
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Raleway', sans-serif;
    }

    .main-title {
        font-size: 48px;
        color: #9B59B6;
        text-align: center;
        margin-bottom: 20px;
        animation: fadeIn 2s ease-in-out;
    }

    .sidebar .stSelectbox label,
    .sidebar .stSlider label,
    .sidebar .stColorPicker label {
        font-size: 16px;
        color: #6C3483;
    }

    .sidebar {
        background-color: #F8F0FB;
        border-radius: 10px;
        padding: 20px 10px;
    }

    .stSlider, .stSelectbox, .stColorPicker {
        background-color: #F4ECF7;
        border-radius: 8px;
        padding: 5px 10px;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    .canvas-container {
        display: flex;
        justify-content: center;
        padding: 20px;
        background-color: #FDF7FF;
        border-radius: 20px;
        animation: fadeIn 1.5s ease-in;
        box-shadow: 0 0 15px #e3d4f0;
    }
    </style>

    <div class="main-title">🎨✨ Tablero Mágico Morado ✨🎨</div>
    """,
    unsafe_allow_html=True
)

# Configuración del tablero en la barra lateral
with st.sidebar:
    st.markdown("### 💜 Personaliza tu experiencia")
    drawing_mode = st.selectbox(
        "Herramienta de dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )
    stroke_width = st.slider("Ancho del trazo", 1, 30, 10)
    stroke_color = st.color_picker("Color del trazo", "#A569BD")
    bg_color = "#FDF7FF"  # fondo suave y morado pastel

# Lienzo con espacio extra y configuración ideal
st.markdown('<div class="canvas-container">', unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="rgba(169,105,189,0.2)",  # morado pastel translúcido
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=700,
    width=1000,
    drawing_mode=drawing_mode,
    key="canvas"
)

st.markdown('</div>', unsafe_allow_html=True)

