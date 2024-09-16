import streamlit as st
import numpy as np
import pandas as pd 
import time
from random import randint

st.title("*Tech Challenge #3*")
st.write("Interface que interage com o modelo treinado para previsão de popularidade de uma música")

st.sidebar.header('Dados de entrada')
artist_name = st.sidebar.text_input('Digite o nome do artista')
album_name = st.sidebar.text_input('Digite o nome do álbum')
track_genre = st.sidebar.selectbox('Gênero musical',('a','b','c','d'))
loudness = st.sidebar.number_input('Loudness (valores tipicamente entre -50 e 5)')
duration_s = st.sidebar.number_input('Duração da música em segundos')
duration_ms = duration_s/1000

entrada_modelo = pd.DataFrame([np.array([artist_name,album_name,track_genre,loudness,duration_ms])],columns=['artists','album_name','track_genre','loudness','duration_ms'])

st.write('Dados de entrada')
st.write(entrada_modelo)

if (st.sidebar.button('Realizar previsão')):

    with st.spinner('Carregando modelo'):
        time.sleep(1)
        #carregar modelo aqui
        
    st.success('Modelo carregado')

    with st.spinner('Realizando previsão'):
        time.sleep(1)
        result = randint(0,1)
        #result = model.predict()
    
    st.success('Previsão realizada')

    if result == 0:
        st.subheader("Sua música não tem grande chance de sucesso, mas não desista!")
    if result == 1:
        st.subheader("Sua música pode ser um grande sucesso, parabéns!")

    st.write('Obrigada por usar nosso app!')
    
