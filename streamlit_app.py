import pandas as pd 
import plotly.express as px 
import streamlit as st 
import folium 
from streamlit_folium import st_folium 

# Configuration de la page Streamlit
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

@st.cache_data
def get_data_from_excel1():
    # Lire les données depuis le fichier Excel
    df = pd.read_excel(
        io="DATA.xlsx",          # Fichier Excel
        engine="openpyxl",      # Utilisation de l'engine 'openpyxl'
        sheet_name="Base_avec_formules",  # Nom de la feuille à lire
        usecols="A:M",          # Colonnes à utiliser
        nrows=1000              # Nombre de lignes à lire
    )
    return df


@st.cache_data
def get_data_from_excel2():
    df2 = pd.read_excel(
        io="DATA.xlsx",
        engine="openpyxl",      # Correction de l'orthographe
        sheet_name="Objectifs",
        usecols="A:M",
        nrows=10
    )
    return df2 

# Chargement des données
df = get_data_from_excel1()
df2 = get_data_from_excel2() 

# Fusionner les deux DataFrames
df_merge = df.merge(df2, on="Produits", how="left")  # join des 2 sheets (feuilles) 

# Extraire les villes et produits
villes = sorted(df_merge["Villes"].unique())  # Correction de df_merged à df_merge
produits = sorted(df_merge["Produits"].unique())

# Sidebar pour filtrer les données
st.sidebar.header("Filtrer les données ici :")
produit = st.sidebar.multiselect(
    "Choisissez le produit :",
    options=produits,
    default=produits
)

ville = st.sidebar.multiselect(
    "Choisissez la ville :",
    options=villes,
    default=villes
)

# Sélection des données selon les filtres
df_selection = df_merge.query(
    "Villes == @ville & Produits == @produit"  # Correction pour respecter la casse
)

# Vérifions si le DataFrame est vide
if df_selection.empty:
    st.warning("Aucune donnée disponible sur la base des paramètres de filtre actuels !")
    st.stop()

# Titre du dashboard
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")


# KPIs 
chiffre_daffaire_totale = int(df_selection["Chiffre_d'affaire"].sum())
cout_total_de_production = int(df_selection["Cout_total"].sum())
marge_brute = chiffre_daffaire_totale - cout_total_de_production 

left_column, middle_column, right_column = st.columns(3) 
with left_column:
    st.subheader("Chiffre d'affaire:")
    st.subheader(f"EURO € {chiffre_daffaire_total:,}")

with middle_column:
    st.subheader("Coût production:")
    st.subheader(f"EURO € {cout_total_de_production:,}")

with right_column:
    st.subheader("Marge brute:")
    st.subheader(f"EURO € {marge_brute:,}")
    
st.markdown("""___""") 