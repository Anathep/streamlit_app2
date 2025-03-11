import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# Titre de l'application
st.title('Analyse des données des voitures')

# Ajouter des boutons de filtre pour la région
region = st.selectbox("Sélectionner la région", ["US", "Europe", "Japon", "Tout"])

if region != "Tout":
    df = df[df['continent'] == region]

# Afficher quelques statistiques de base
st.subheader("Statistiques des données")
st.write(df.describe())

# Afficher la corrélation entre les variables
st.subheader("Analyse de Corrélation")
corr = df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Afficher la distribution des variables
st.subheader("Distribution des variables")
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df[column], kde=True, ax=ax)
    ax.set_title(f'Distribution de {column}')
    st.pyplot(fig)

# Option pour afficher la distribution des différentes régions
if region == "Tout":
    st.subheader("Distribution par région")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='continent', data=df, ax=ax)
    st.pyplot(fig)

# Exécution de l'application
if __name__ == '__main__':
    st.write("Application terminée.")