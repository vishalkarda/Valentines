import base64
import streamlit as st


def play_music(file_path: str) -> None:
    """function to play music on streamlit page"""

    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


def display_gif(file_path: str) -> None:
    """function to display the gif"""
    with open(file_path, "rb") as file:
        contents = file.read()
        data_url = base64.b64encode(contents).decode("utf-8")

    st.markdown(
        f"""<div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
                <img align="center" src="data:image/gif;base64,{data_url}" alt="cat gif">
            </div>""",
        unsafe_allow_html=True,
    )
