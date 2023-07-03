import pandas as pd
#import io
import requests
import openpyxl
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image
import os

#url = "https://github.com/ZakariaNouioura/Projet_Streamlit_X_Assassins_Creed/raw/main/DataFrame/Les_jeux.xlsx"
#response = requests.get(url)
#df = pd.read_excel(url)
#st.write(df)

## l'histoire de Ubisoft
#git


st.set_page_config(
    page_title="Analyse ubisoft",
    page_icon="👋",
)

# recuperation du chemin relatif du fichier de répartition des salariés
lien = "../Images/Logo_Ubisoft.PNG"

#Affichage de l'image Logo Ubisoft
#image = Image.open(chemin_relatif_logo_ubisoft)
st.image(lien, caption='Logo Ubisoft')

st.header("Zakaria Nouioura, Massyl, Boubacar")

st.write("""Bonjour à tous, nous sommes une équipe de data analyst et aujourd'hui nous allons nous interesser à la saga Assassin's Creed. 
L'objectif sera ici d'analyser les commentaires des utilisateurs des différents jeux et voir commen Ubisoft à su se réinventer pour faire durer depuis maintenant 16 ans. Nous allons également vous expliquer pourquoi notre choix s'est porté sur cette suite de jeux et la maniere dont nous avons orienter nos recherches.
Ubisoft est une société francaise qui a connu un incroyable croissance, en l'espace de 30 ans elle est devenu un des leader mondiaux du jeux video. Parmis la longue liste de jeux à succès on peut citer :
- Assassin's Creed
- Just Dance
- Prince of Persia
- Lapins Crétins
- Tom Clancy
- Watchdos
- Farcry

Maintenant que vous connaissez Ubisoft, nous allons concentrer nos efforts sur la saga assassin's creed. 
C'est une série de jeux vidéo historique d'action-aventure et d'infiltration en monde ouvert. 
Le principe du jeu repose sur l'enlevement de Desmond Miles par multinationale Abstergo Industries, une entreprise pharmaceutique et forcé d'utiliser l'« Animus », une machine qui permet de décoder les mémoires génétiques 🧬 de son utilisateur stockées dans son ADN, offrant la possibilité de revivre les souvenirs de ses ancêtres sous forme de réalité virtuelle.
Abstergo cherche à localiser plusieurs artefacts, appelées « Fragments d'Éden », façonnés par une race de précurseurs. 
À l'intérieur de l'Animus, Desmond revit les souvenirs de plusieurs de ces ancêtres êtes vous pret à entamer votre premier voyage génétique ? """)

if st.button('Vous voulez en savoir plus ?'):
    st.write('Why hello there')
# embed streamlit docs in a streamlit app
    st.text("""

L’histoire d’Ubisoft commence dans les années 80 en Bretagne. Les cinq frères Guillemot (Claude, Michel, Yves, Gérard et Christian) veulent diversifier les activités de l’entreprise familiale spécialisée dans les produits agricoles. Ils se tournent alors vers la vente de petits ordinateurs. Lors d’un voyage en Angleterre, Michel Guillemot découvre que les jeux vidéo y sont moins chers qu’en France. De retour en France, il lance un service de distribution de jeux. Les ventes dépassant largement ses attentes,  il se rend compte de tout le potentiel de ce marché.

En 1986, les frères fondent Ubisoft : la société distribue les jeux des grandes sociétés américaines et européennes. En 1988, Yves Guillemot devient le PDG de la société en croissance exponentielle. En parallèle de son activité de distribution, Ubisoft se lance dans le développement de ses propres jeux vidéo. En 1990, la société sort son premier jeu, basique mais novateur, Zombi, sur Amstrad, premier succès commercial. Ubisoft connait une croissance rapide (notamment via l’acquisition de studios), enchaine les sorties de jeux et sait créer des marques très fortes qui pérennisent l’activité :

    Rayman en 1994 connait un succès mondial. En 10 ans, le jeu se vendra à 15 millions d’exemplaires
    Tom Clancy en 2002 connait un tel succès que les stocks européens sont épuisés en moins de 24h
    Prince of Persia : 1,1 millions de jeux vendus en trois mois
    Lapins Crétins en 2006
    Assassin’s Creed en 2007 est salué par la critique pour son ambition, son audace et son esthétique. Le jeu se vend à 3 millions d’exemplaires en moins de deux mois. Le jeu deviendra une des franchises les plus populaires de tous les temps, avec plus de 100 millions d’exemplaires vendus à ce jour.
    Just Dance en 2009 : plus de 40 millions de jeux vendus à ce jour
    Watch Dogs lancé en 2014 rencontre un succès commercial avec 4 millions d’exemplaires en une semaine, le jeu le plus vendu au monde à son lancement

La société ouvre des studios partout dans le monde, ce qui lui permet d’avoir une meilleure couverture de l’ensemble des comportements et des cultures. Autres faits marquants :

    En 1996 la société fait son entrée sur le second marché de la bourse de Paris et sur le premier marché en 2000.
    Acquisition de 20% du capital de Gameloft en 2000, développeur de jeux video mobiles.
    En 2003, Ubisoft célèbre ses 100 millions de jeux vendus

Ubisoft se diversifie et crée une stratégie de développement transmedia :

    En 2009, la société crée sa propre société d’édition de bande dessinée, Les Deux Royaumes, pour transposer les franchises de jeux vidéo dans l’univers de la BD (Lapins Crétins, Assassin’s Creed et Watch Dogs)
    En 2011, la société crée sa propre société de production, Ubisoft Motion Pictures, pour porter les franchises de jeux vidéos à la télévision (Lapins Crétins) et au cinéma (Assassin’s Creed)""")
else:
    st.write('')

from streamlit_timeline import st_timeline

items = [
    {"id": 1, "content": "Assasin's creed", "start": "2007","style": "color: white; background-color: #180391; border-color: #180391;box-shadow: none;"},
    {"id": 2, "content": "Assassin's Creed II", "start": "2009"},
    {"id": 3, "content": "Assassin's Creed: Brotherhood", "start": "2010"},
    {"id": 4, "content": "Assassin's Creed: Revelations", "start": "2011"},
    {"id": 5, "content": "Assassin's Creed III", "start": "2012"},
    {"id": 6, "content": "Assassin's Creed IV: Black Flag", "start": "2013"},
    {"id": 7, "content": "Assassin's Creed: Rogue", "start": "2014"},
    {"id": 8, "content": "Assassin's Creed: Unity", "start": "2014"},
    {"id": 9, "content": "Assassin's Creed: Syndicate", "start": "2015"},
    {"id": 10, "content": "Assassin's Creed Origins", "start": "2017"},
    {"id": 11, "content": "Assassin's Creed Odyssey", "start": "2018"},
    {"id": 12, "content": "Assassin's Creed Valhalla", "start": "2018"},
    {"id": 13, "content": "Assassin's Creed Odyssey", "start": "2020"},
    {"id": 14, "content": "Assassin's Creed: Mirage", "start": "2023"}]



timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
chemin_contenu="..\DataFrame\Les_jeux.xlsx"
df=pd.read_excel(chemin_contenu,index_col=None, header=1)

if timeline["id"]==1:    
    img_assassin1 = Image.open("..\Images\Assassin's creed 1.jpg")
    st.image(img_assassin1,width=200) 
    st.write(df.iloc[0,1])
    st.header("Les retours")
    st.write(df.iloc[0,3])
    st.header("Quelques chiffres")
    st.write("Le jeux à vendu :",df.iloc[0,4], "de copies et obtenu une note de",df.iloc[0,5],"sur Metactritic :sunglasses:")
    st.header("Analyse des sentiments")
elif timeline["id"]==2:    
    st.header("L'histoire du jeu")
    img_assassin2 = Image.open("..\Images\Assassin's Creed 2.jpg")
    st.image(img_assassin2,width=200) 
    st.write(df.iloc[1,1])
    st.header("Les retours")
    st.write(df.iloc[1,3])
    st.header("Analyse des sentiments 😭")



