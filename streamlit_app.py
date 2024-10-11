import pandas as pd 
import plotly.express as px 
import streamlit as st 
import folium 
from streamlit_folium import st_folium 

st.set_page_config(page_title="Sales Dashboard",
                   page_icon =":bar_chart:",
                   layout= "wide")

@st.cache_data # mettre les données en cache poue eviter d'aller la copier à chaque fois dans le fichier excel 

def get_data_from_excel():
    # Lire les données depuis le fichier Excel
    df = pd.read_excel(
        io="DATA.xlsx",          # Fichier Excel
        engine="openpyxl",        # Utilisation de l'engine 'openpyxl'
        sheet_name="Base_avec_formules",  # Nom de la feuille à lire
        usecols="A:M",            # Colonnes à utiliser
        nrows=1000                # Nombre de lignes à lire
    )
    return df


@st.cache_data

def get_data_from_excel2():
    df2= pd.read_excel(
        io= "DATA.xlsx",
        engine= "openpysxl",
        sheet_name= "Objectifs",
        usecols= "A:M",
        nrows = 10
    )
    return df2 

df = get_data_from_excel1()
df2 = get_data_from_excel2() 
df_merge = df.merge(df2, on="Produits", how="left") # join des 2 sheets (feuilles) 

