import streamlit as st
import time

def main():
    st.write('wena cabros jajajaja')
    
    slider = st.slider('texto slider', 0, 10, 2)
    
    st.write(f'Este es el valor del slider {slider}')
    
    st.sidebar.title('jajaja')
    

    
    
    
main()