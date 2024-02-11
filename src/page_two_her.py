import base64
import streamlit as st


def load_image(file_path: str) -> str:
    """function to load the images"""
    st.markdown("""
                <style>
                .centered-image {
                    display: block;
                    margin: auto;
                }
                </style>
                """, unsafe_allow_html=True)

    # Read the image file as bytes
    with open(file_path, "rb") as f:
        image_bytes = f.read()

    # Convert image bytes to base64
    image_base64 = base64.b64encode(image_bytes).decode()

    return image_base64


def create_a_container() -> None:
    """function to create a container which will encapsulate all the elements
    on this page"""
    with st.container():
        variant_expander()
        word_cloud_expander()
        food_habits_expander()


def variant_expander() -> None:
    """function to create a expander which will keep the information on variants"""

    with st.expander(label="Tales of Riddhi -> 1"):
        st.write("### >> Riddhi & Her Variants")
        col1, _ = st.columns([0.99, 0.01])

        with col1:
            image = load_image("her/images/Riddhi.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
            class="centered-image" 
            height="350" 
            width="650">''',
                        unsafe_allow_html=True)

        col1_1, col1_2 = st.columns(2)
        with col1_1:
            image = load_image("her/images/reddi.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
                        class="centered-image" 
                        height="300" 
                        width="330">''',
                        unsafe_allow_html=True)
        with col1_2:
            image = load_image("her/images/reddy.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
                        class="centered-image" 
                        height="300" 
                        width="300">''',
                        unsafe_allow_html=True)


def word_cloud_expander() -> None:
    """function to create a world cloud expander"""
    with st.expander(label="Tales of Riddhi -> 2"):
        st.write("### >> Words She Blurr All The Time")
        image = load_image("her/images/things_she_say.png")
        st.markdown(f'''<img src="data:image/png;base64,{image}" 
                                class="centered-image" 
                                height="300" 
                                width="650">''',
                    unsafe_allow_html=True)


def food_habits_expander() -> None:
    """function to create the food habits expander"""
    with st.expander(label="Tales of Riddhi -> 3"):
        st.write("### >> Food Which Is Her Soul of Life")
        col1, col2 = st.columns(2)
        with col1:
            image = load_image("her/images/r_basundi.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
                                class="centered-image" 
                                height="300" 
                                width="330">''',
                        unsafe_allow_html=True)
        with col2:
            image = load_image("her/images/r_maggi.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
                                class="centered-image" 
                                height="300" 
                                width="300">''',
                        unsafe_allow_html=True)

        col3, col4 = st.columns(2)
        with col3:
            image = load_image("her/images/r_golgappe.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
                                class="centered-image" 
                                height="300" 
                                width="330">''',
                        unsafe_allow_html=True)
        with col4:
            image = load_image("her/images/r_pavbhaji.png")
            st.markdown(f'''<img src="data:image/png;base64,{image}" 
                                class="centered-image" 
                                height="300" 
                                width="300">''',
                        unsafe_allow_html=True)

