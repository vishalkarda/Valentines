import streamlit as st

from src.poetry_constant import verse_1, verse_2, verse_3


def create_the_tabs() -> None:
    """function to create the tabs which will have the poetry"""
    tab_one, tab_two, tab_three = st.tabs(["Verse 1", "Verse 2", "Verse 3"])

    with tab_one:
        st.text(verse_1)

    with tab_two:
        st.text(verse_2)

    with tab_three:
        st.text(verse_3)
