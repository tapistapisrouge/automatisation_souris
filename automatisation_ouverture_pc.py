# -*- coding: utf-8 -*-
"""
fait le  juillet
Amaury Paget
"""

# Import libraries ========================================================
import pyautogui
import pyperclip as pc
import time
import pathlib
import pandas as pd
import re
import numpy as np
import cv2
import datetime

# packages perso
# from functions.waitAndAct import waitAndAct

path_main = pathlib.Path(__file__).parent
print(path_main)

# en attente 
import sys
sys.path.append(path_main)
from functions.waitAndAct import waitAndAct
from functions.waitAndAct import allscreen_waitAndAct
# pyautogui.FAILSAFE = False

# gestion des chemins =====================================================
path_input = pathlib.Path(path_main, 'input')
path_output = pathlib.Path(path_main, 'output')

# chemins images et csv
path_img = pathlib.Path(path_input, 'img')
path_csv = pathlib.Path(path_input, 'csv')

#ouverture csv
path_csv = pathlib.Path(path_csv, 'onglet_firefox.csv')
df_onglet_firefox = pd.read_csv(path_csv, sep=';', decimal='.', encoding='latin-1')

# basics =================================================================
# taille écran
print(pyautogui.size())

# utile pour voir quelle position mettre
print(pyautogui.position())




# ==========================================================================================
# mettre partage de co telephone =====================================
# ==========================================================================================

# afficher le bureau windows
pyautogui.hotkey("win","d")

# aller sur parametre
waitAndAct(path_img, 'fenetre_windows.png', action='click', confidence=0.8)
waitAndAct(path_img, 'barre_recherche.png', action='doublelick', confidence=0.8)
pc.copy("Paramètres")
pyautogui.hotkey("ctrl","v", interval=0.1)
pyautogui.hotkey("enter")
waitAndAct(path_img, 'parametre.png', action='click', confidence=0.8)
# activer point acces sans fil
waitAndAct(path_img, 'reseau_internet.png', action='click', confidence=0.8)
allscreen_waitAndAct(path_img, 'activate.png', action='click', confidence=0.8, occurrence=5)
waitAndAct(path_img, 'croix_parametre.png', action='click', confidence=0.8)


# ==========================================================================================
# Firefox =====================================
# ==========================================================================================
# ouvrir Firefox
waitAndAct(path_img, 'firefox.png', action='doubleClick', confidence=0.8)

# premier onglet
waitAndAct(path_img, 'recherche_google_good.png', action='click', confidence=0.8)
pc.copy("https://www.antedis.com/")
pyautogui.hotkey("ctrl","v", interval=0.1)
pyautogui.hotkey("enter")

# boucle sur les onglets
for line in df_onglet_firefox.index :
    pyautogui.hotkey("ctrl","t")
    site_web = df_onglet_firefox["adresse_web"][line]
    waitAndAct(path_img, 'recherche_google_good.png', action='click', confidence=0.8)
    pc.copy(site_web)
    pyautogui.hotkey("ctrl","v", interval=0.1)
    pyautogui.hotkey("enter")
    
    # pour gmail
    if site_web=="https://www.google.com/intl/fr/gmail/about/":
        print("gmail detecte")
        waitAndAct(path_img, 'gmail_connexion_2.png', action='click', confidence=0.7)
        waitAndAct(path_img, 'A.png', action='click', confidence=0.7)
    

    






















