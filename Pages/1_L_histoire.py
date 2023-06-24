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

st.markdown("""Pour notre projet nous avons décidé de nous focaliser sur l’éditeur UBISOFT. La raison :""" )

st.markdown( """Ubisoft est une entreprise française de développement, d’édition et de distribution de jeux video. En 30 ans, elle est devenue l’un des leaders mondiaux du jeu video en développant des jeux connus dans le monde entier et utilisés par des millions de joueurs, comme Just Dance, Prince of Persia, Assassin’s Creed ou encore Lapins Crétins.""")

st.markdown( 
"""
- UBISOFT développe des jeux multi plateformes (Playstation , Nintendo, Xbox, Mobile, …)
- UBISOFT est un developpeur ET éditeur qui utilise son propre moteur graphique
- 6 franchises à succès , 11 titres , avec pour chacun plus de 10 millions d’unités vendus dans le monde
- UBISOFT est un éditeur français à rayonnement internationale (analyse comparative avec d’autres boites mondiales ET  francaises , salariés, …)
"""

)


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
