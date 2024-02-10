import base64
import streamlit as st

from streamlit_option_menu import option_menu


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


def main():
    """Main function to run the file"""
    st.title("HaaaaaaaaVeeee you met Riddhi ?!! ")

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
        st.write("Welcome to the Streamlit world of Riddhi Joshi. She has superpowers songs play"
                 "automatically in the background when you visit her content. She's full of elegance and smartness but "
                 "will act dumb on purpose sometimes to make you feel normal !!"
                 "No mere human could match that, so let's dive into world.")

    if choose == "Her":
        st.write("Page 1")
        play_music("her/Akhiyaan_Gulaab.mp3")

    if choose == "Tech Break":
        st.write("Page 3")

    elif choose == "The Poetry":
        st.write("Page 2")
        play_music("her/Pehle_Bhi_Main.mp3")

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
