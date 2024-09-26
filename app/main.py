import streamlit as st
import numpy as np
import pandas as pd 
import time
import sklearn
from config import track_list
import pickle
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure Pandas
sklearn.set_config(transform_output="pandas")

# Streamlit Page Configuration
st.set_page_config(
    page_title="Tech Challenge #3",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/raianeli25/tech_challenge_3",
        "Report a bug": "https://github.com/raianeli25/tech_challenge_3",
        "About": """
            ## FIAP Tech Challenge

            **Readme**: https://github.com/raianeli25/tech_challenge_3/blob/main/README.md
        """
    }
)

def show_app():
    # Streamlit Title
    st.title("Tech Challenge #3")
    st.write("Interface que interage com o modelo treinado para previsão de popularidade de músicas")

    st.sidebar.header('Dados de entrada')
    st.sidebar.markdown("---")

def sidebar_input():

    artist_name = st.sidebar.text_input('Artista', placeholder='Digite o nome do artista')
    album_name = st.sidebar.text_input('Álbum',  placeholder='Digite o nome do álbum')
    track_genre = st.sidebar.selectbox('Gênero', track_list, index=None, placeholder='Selecione o gênero da música')
    loudness = st.sidebar.number_input('Loudness', min_value=-50, max_value=5, value=None, placeholder='Valores entre -50 e 5')
    duration_s = st.sidebar.number_input('Duração', min_value=0, max_value=1000, value=None, placeholder='Duração da música em segundos')

    if duration_s is None:
        duration_ms = 0
    else:
        duration_ms = duration_s/1000


    input_values = {
        'Artista': artist_name,
        'Album': album_name,
        'Genero': track_genre,
        'Loud': loudness,
        'Duracao': duration_ms

    }
    
    return input_values

def get_data(input_values):

    return pd.DataFrame(
        [
        np.array(
            [input_values['Artista'],
             input_values['Album'],
             input_values['Genero'],
             input_values['Loud'],
             input_values['Duracao']
            ])
        ],  columns=['artists','album_name','track_genre','loudness','duration_ms']
    )


@st.cache_data
def read_model():
    """ Read pick file """
    try:
        with open('data/model_svc_classifier', 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        logging.error(f"Erro em abrir o arquivo: {str(e)}")
        return None
    
def progress():

    carregando_text = 'Carregando Modelo. Aguarde'
    realizando_text = 'Realizando Previsão.'
    my_bar = st.progress(0 , text=carregando_text)
    my_bar2 = st.progress(0 , text=realizando_text)

    for percent_progress in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_progress + 1, text=carregando_text)

    time.sleep(1)
    my_bar.empty()

    for percent_progress2 in range(100):
        time.sleep(0.01)
        my_bar2.progress(percent_progress2 + 1, text=realizando_text)

    time.sleep(1)
    my_bar2.empty()
    
def main():
    
    show_app()
    output_values = sidebar_input()

    if (st.sidebar.button('Realizar previsão')):
        data = get_data(output_values)
        
        with st.spinner('Carregando modelo'):
            model = read_model()
            time.sleep(1)
        
        with st.spinner('Realizando previsão'):
            result = model.predict(data)
            predict_result = model.predict_proba(data)
            time.sleep(1)

        st.markdown("---")
        st.success('Previsão realizada')

        if result == 0:
            st.subheader("Música com pouca chance de sucesso, mas não desista!")
            st.write(f'Chance de  sucesso: {round(predict_result[0][1] * 100, 2)}%')
        if result == 1:
            st.subheader("Música com grande chance de sucesso, parabéns!")
            st.write(f'Chance de  sucesso: {round(predict_result[0][1] * 100, 2)}%')

        st.markdown("---")
        st.write('Obrigado por utilizar o App.')


if __name__ == '__main__':
    main()
    