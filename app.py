import streamlit as st

from streamlit_option_menu import option_menu
from src.utils import display_gif, play_music
from src.page_two_her import create_a_container
from src.page_four_poetry import create_the_tabs
from src.poetry_constant import page_2_intro, page_1_intro, page_4_intro


def main():
    """Main function to run the file"""
    st.title("HaaaaaaaaVeeee you met Riddhi ?!! ")
    st.text("")

    with st.sidebar:
        choose = option_menu("Main Menu", ["Getting Started", "Her", "Tech Break", "The Poetry", "Author"],
                             icons=['house', 'cloud', "break", 'list-task', "gear"],
                             menu_icon="cast", default_index=0,
                             styles={
                                 "container": {"padding": "2!important", "background-color": "#000000"},
                                 "icon": {"color": "orange", "font-size": "14px"},
                                 "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px",
                                              "--hover-color": "#eee"},
                                 "nav-link-selected": {"background-color": "#24A608"},
                             }
                             )

    if choose == "Getting Started":
        st.write(page_1_intro)
        st.text("")
        st.text("")
        st.text("")
        display_gif("her/gifs/riddhi_magic.gif")

    if choose == "Her":
        st.text(page_2_intro)
        play_music("her/music/Akhiyaan_Gulaab.mp3")
        display_gif("her/gifs/Author_1.gif")
        create_a_container()

    if choose == "Tech Break":
        display_gif("her/gifs/technical_error.gif")

    elif choose == "The Poetry":
        st.write(page_4_intro)
        st.write("""
                 Like I always tell you its both the poet in me and the poetry in you.
                 I'm not really sure if the verses below will do the justice to the fact how amazing you are !!
        """)
        play_music("her/music/Pehle_Bhi_Main.mp3")
        create_the_tabs()

    elif choose == "Author":
        st.text("")
        display_gif("her/gifs/getting_started.gif")
        st.text("")
        st.text("")
        col1, col2 = st.columns([0.8, 0.2])

        play_music("her/music/Feelings.mp3")
        with col1:
            st.markdown(""" <style> .font {
            font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;
            } 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">About the Author</p>', unsafe_allow_html=True)

        st.write(
            "Vishal Karda is a Data Science practitioner, "
            "enthusiast."
            "\n\nHe's also a writer. Who loves reading books, novels and writes excerpts and poems."
            "\n\nTo know more about Vishal, please call or visit him:"
            "\n\nLinkedIn @ https://www.linkedin.com/in/vishal-karda/")


if __name__ == "__main__":
    main()
