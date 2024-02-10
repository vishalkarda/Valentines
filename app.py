import streamlit as st


def main():
    st.title("Background Music Streamlit App")
    st.write("Welcome to my Streamlit app with background music!")

    # Embedding HTML5 audio tag
    audio_html = """
    <audio autoplay loop>
        <source src="her/Pehle_Bhi_Main.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
