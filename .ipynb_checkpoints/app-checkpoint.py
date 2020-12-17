import streamlit as st


def main():

    st.write('holaaaaaaajajajaja')
    st.title('Titulo')
    
    st.sidebar.write('miremos el sidebar')
    
    boton = st.button('label')
    
    st.write(f'El botón vale {boton}')
    
    sliders = st.slider('objeto slider', 0, 10)
    
    st.write(f'El valor del slider es {sliders}')
    
    st.balloons()
    
    
    
main()