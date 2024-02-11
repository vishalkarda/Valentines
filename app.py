import streamlit as st

from streamlit_option_menu import option_menu
from src.utils import display_gif, play_music
from src.page_two_her import create_a_container
from src.page_four_poetry import create_the_tabs
from src.poetry_constant import page_2_intro


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
        st.write("Welcome to the Magical Streamlit World of Riddhi Joshi. She has superpowers songs play"
                 "automatically in the background when you visit her content. She's full of elegance and smartness but "
                 "will act dumb on purpose sometimes to make you feel normal !! "
                 "No mere human could match that, so let's dive into world.")
        st.text("")
        st.text("")
        st.text("")
        display_gif("her/gifs/riddhi_magic.gif")

    if choose == "Her":
        # play_music("her/Akhiyaan_Gulaab.mp3")
        st.text(page_2_intro)
        display_gif("her/gifs/Author_1.gif")
        create_a_container()

    if choose == "Tech Break":
        display_gif("her/gifs/technical_error.gif")

    elif choose == "The Poetry":
        st.write(f"""
        So now we are onto the poetry section and hopefully the background music is still working.
        Dumbledore said, 'Words are, in my not-so-humble opinion, our most inexhaustible source of magic, 
        capable of both inflicting injury and remedying it.
        Let's see these below words have magic.
        """)
        st.write("""
                 Like I always tell you its both the poet in me and the poetry in you.
                 I'm not really sure if the verses below will do the justice to the fact how amazing you are !!
        """)
        # play_music("her/Pehle_Bhi_Main.mp3")
        create_the_tabs()

    elif choose == "Author":
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">About the Author</p>', unsafe_allow_html=True)

        st.write(
            "Vishal Karda is a Data Science practitioner, "
            "enthusiast."
            "\n\nHe's also a writer. Who loves reading books, novels and writes excerpts and poems."
            "\n\nTo know more about Vishal, please visit him:"
            "\n\nLinkedIn @ https://www.linkedin.com/in/vishal-karda/")


if __name__ == "__main__":
    main()
