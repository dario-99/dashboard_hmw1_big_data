'''
Author: Dario Di Meo, Leonardo Alberto Anania
Language: Python
Description: dashboard in streamlit per l'homework 1 per il corso 2022-2023 di Big Data
'''

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
import glob
import plotly.express as px
import geopandas
import plotly.figure_factory as ff
from geopy.geocoders import Nominatim
import folium

# Funzione di loading dei dati
@st.cache_data()
def load_dataset():
    files = glob.glob('./dataset/*.txt')
    data = {x.removeprefix('./dataset/').removesuffix('.txt'): pd.read_csv(x, sep='\t') for x in files}

    # # Transform country to lat e long
    # geolocator = Nominatim(user_agent="my_application")
    # lat = []
    # lon = []
    # for idx, elem in data['4_partner'].iterrows():
    #     pos = geolocator.geocode(elem['partner'])
    #     if not pos:
    #         st.error(f"{elem['partner']} non trovato")
    #         lat.append(0)
    #         lon.append(0)
    #     else:
    #         lat.append(pos.latitude)
    #         lon.append(pos.longitude)
    # data['4_partner'].insert(0, 'lat', lat)
    # data['4_partner'].insert(0, 'lon', lon)

    # # Transform country to lat e long
    # lat = []
    # lon = []
    # for idx, elem in data['6_countries_coinvolti'].iterrows():
    #     pos = geolocator.geocode(elem['partner'])
    #     if not pos:
    #         st.error(f"{elem['country']} non trovato")
    #         lat.append(0)
    #         lon.append(0)
    #     else:
    #         lat.append(pos.latitude)
    #         lon.append(pos.longitude)
    # data['6_countries_coinvolti'].insert(0, 'lat', lat)
    # data['6_countries_coinvolti'].insert(0, 'lon', lon)
    return data

st.set_page_config(layout='wide')

# Dataset
data = load_dataset()

# Set widemode

st.title("Dashboard Fondi Federico II")

col1, col2 = st.columns(2)

# Colonna 1
with col1:
    st.title("Temi piu' studiati")
    # st.dataframe(data['1_temi_piu_studiati'], )
    num_temi = st.slider(min_value=2, max_value=len(data['1_temi_piu_studiati']), label='Numero di temi', step=1, value=10)
    temi_chart = px.bar(data['1_temi_piu_studiati'][:num_temi], x='count', y='tema', color='count')
    st.plotly_chart(temi_chart)

    # Numero progetti finanziati per anno
    st.title('Numero progetti finanziati per anno')
    count_anno_chart = px.bar(data['3_numero_progetti_finanziati_per_anno'], x='anno', y='count', color='count', color_continuous_scale='Inferno')
    st.plotly_chart(count_anno_chart)

    # 4 Partner
    st.title("Numero di collaborazioni con partner esterni")
    num_partner = st.slider(min_value=2, max_value=len(data['4_partner']), label='numero di partner', step=1, value=10)
    data['4_partner'] = data['4_partner'].where(data['4_partner']['partner'] != 'university of naples federico ii')
    partner_chart = px.bar(data['4_partner'][:num_partner], x='partner', y='count', color_continuous_scale='Viridis', color='count')
    st.plotly_chart(partner_chart)
    # st.map(data['4_partner'])

    # 7 campi con piu investimenti
    st.title("campi di ricerca con piu investimenti")
    num_campi = st.slider(min_value=2, max_value=len(data['7_campi_con_piu_investimenti']), label='numero di campi di ricerca', step=1, value=10)
    campi_chart = px.bar(data['7_campi_con_piu_investimenti'][:num_campi], x='campo', y='funds', color='funds')
    st.plotly_chart(campi_chart)

    # 11 sum fund per goal

    st.title("Somma dei fondi ricevuti per goal per il futuro")
    num_goal = st.slider(min_value=2, max_value=len(data['11_sum_fund_goals']), label='numero di goal', step=1, value=10)
    sum_chart = px.bar(data['11_sum_fund_goals'][:num_goal], x='code', y='goal', color='goal')
    st.plotly_chart(sum_chart)
    


with col2:
    st.title('Ricercatori della federico II con piu progetti')
    num_ricercatori = st.slider(min_value=2, max_value=len(data['2_analisi_ricercatori']), label='Numero di ricercatori', step=1, value=10)
    ricercatori_chart = px.bar(data['2_analisi_ricercatori'][:num_ricercatori], x='count', y='ricercatore', color='count')
    st.plotly_chart(ricercatori_chart)

    # fondi ricevuti per anno
    st.title('fondi ricevuti per anno')
    count_anno_chart = px.bar(data['5_fondi_ricevuti_per_anno'], x='anno', y='fondi', color='fondi', color_continuous_scale='Inferno')
    st.plotly_chart(count_anno_chart)

    # 6 paesi convolti
    st.title('Paesi con piu collaborazioni con la Federico II oltre l\'italia')
    num_paesi = st.slider(min_value=2, max_value=len(data['6_countries_coinvolti']), value=10, label='Numero di paesi')
    country_chart = px.bar(
        data['6_countries_coinvolti'],
        x='country',
        y='count',
        color='count',
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(country_chart)
    
    # 8 top finanziatori
    st.title("Top finanziatori")
    num_funders = st.slider(min_value=2, max_value=len(data['8_top_finanziatori']), label='numero di finanziatori', step=1, value=10)
    campi_chart = px.bar(data['8_top_finanziatori'][:num_funders], x='funder', y='funds', color='funds')
    st.plotly_chart(campi_chart)

    # 12 media
    st.title("Media dei fondi ricevuti per goal per il futuro")
    avg_chart = px.bar(data['12_avg_fund_goals'][:num_goal], x='code', y='goal', color='goal')
    st.plotly_chart(avg_chart)
