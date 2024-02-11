import streamlit as st


def create_a_container() -> None:
    """function to create a container which will encapsulate all the elements
    on this page"""
    with st.container():
        st.text(f"""
        Thodhi si sattki hui hai. 
        Bachpan mei gir gyi thi shayad, but baatein samjhti hai. 
        Thodhi ziddi hai par mujhe acha lgta hai uska zidd krna. 
        Kaafi mere jaisi hai, and mai uske jaise. 
        Gol gappe bht pasand hai usey, lgti thodhi si cartoon hai. 
        Over-eat kr leti hai toh stress krti hai, but isliye toh gym bhi krti hai.
        Kaafi ajeeb hai, Sunday ko bhi gym jaati hai. 
        Uth ti hai subah toh sun shine hai and mujhe rhym ni aa rha ab.
        Basundi bht pasand hai usey, lgti thodhi si cartoon hai !!""")
        variant_expander()
        word_cloud_expander()
        food_habits_expander()


def variant_expander() -> None:
    """function to create a expander which will keep the information on variants"""

    with st.expander(label="Tales of Riddhi -> 1"):

        st.write("### >> Riddhi & Her Variants")
        col1, _ = st.columns([0.99, 0.01])

        with col1:
            st.markdown("""
            <style>
            .font {
                font-size: 35px;
                font-family: 'Cooper Black';
                color: #FF9633;
                text-align: center; /* Center align the text */
            }
            </style>
            """, unsafe_allow_html=True)

            # Display centered text
            st.markdown('<p class="font">First Column</p>', unsafe_allow_html=True)

        col1_1, col1_2 = st.columns(2)
        with col1_1:
            st.markdown('<p class="font">First Column Second Row</p>', unsafe_allow_html=True)
        with col1_2:
            st.markdown('<p class="font">Second Column Second Row</p>', unsafe_allow_html=True)


def word_cloud_expander() -> None:
    """function to create a world cloud expander"""
    with st.expander(label="Tales of Riddhi -> 2"):
        st.write("### >> Words She Blurr All The Time")
        st.write("will put the word cloud here")


def food_habits_expander() -> None:
    """function to create the food habits expander"""
    with st.expander(label="Tales of Riddhi -> 3"):
        st.write("### >> Food Which Is Her Soul of Life")
        st.write("will put the food habits here")
