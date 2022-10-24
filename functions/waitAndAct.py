# -*- coding: utf-8 -*-
"""
Module waitAndAct
--> contient une seule fonction qui va checker si l'image en entrée est visible sur l'écran, dès qu'il y a match,
l'action mise en argument 2 se réalise
"""

# Import libraries ========================================================
import pyautogui
import time
import pathlib
import re

# Fonction  ========================================================

def waitAndAct(path_img, nom_img, action='doubleClick', confidence=0.8, decalageX=0, decalageY=0, timer=200):
    """
    waitAndAct(path_img, nom_img, action='doubleClick', confidence=0.8)
    --> 4 parametres : 
        path_img = chemin où l'image se situe'
        nom_img = nom du fichier image avec extension
        action = mettre click ou doubleClick ou enter ou decalage
        confidence = niveau de similarité entre image et écran pc
        decalageX et Y = action click en décalage du centre de l'image
        timer = nombre de fois qu'on check l'image
    """
    path_final = str(pathlib.Path(path_img, nom_img))
    path_final = re.sub("\\\\", "/", path_final)
    
    img_coord = pyautogui.locateCenterOnScreen(path_final, confidence=0.8)
    
    count = 0
    while img_coord is None:
        print("Détection en cours \n")
        time.sleep(0.1)
        img_coord = pyautogui.locateCenterOnScreen(path_final, confidence=0.8)
        count+=1
        # continue
        if count >= timer:
            break
        
    if count < timer:
        if action == "doubleClick":
            pyautogui.doubleClick(img_coord)
        elif action == "click":
            pyautogui.click(img_coord)
        elif action == "enter":
            pyautogui.hotkey("enter")
        elif action == "decalage":
            coord_X = img_coord[0] + decalageX
            coord_Y = img_coord[1] + decalageY
            pyautogui.click(x=coord_X, y=coord_Y)
        elif action == "decalageAfterClick":
            pyautogui.click(img_coord)
            coord_X = img_coord[0] + decalageX
            coord_Y = img_coord[1] + decalageY
            time.sleep(0.2)
            pyautogui.click(x=coord_X, y=coord_Y)   
        elif action == "rien":
            print("ok")
        else:
            print("Action introuvable")
    
    # récupérer coord
    if img_coord is None:
        X=0
        Y=0
    else:
        X = img_coord[0]
        Y = img_coord[1]
    
    return X, Y
        
        
def allscreen_waitAndAct(path_img, nom_img, action='doubleClick', confidence=0.8, decalageX=0, decalageY=0, occurrence=1, timer=200):
    """
    waitAndAct(path_img, nom_img, action='doubleClick', confidence=0.8)
    --> 4 parametres : 
        path_img = chemin où l'image se situe'
        nom_img = nom du fichier image avec extension
        action = mettre click ou doubleClick ou enter ou decalage
       confidence = niveau de similarité entre image et écran pc
    """
    path_final = str(pathlib.Path(path_img, nom_img))
    path_final = re.sub("\\\\", "/", path_final)
    
    len_list = list(pyautogui.locateAllOnScreen(path_final, confidence=0.8))
    
    count = 0
    while not len_list:
        print("Détection en cours \n")
        time.sleep(0.1)
        len_list = list(pyautogui.locateAllOnScreen(path_final, confidence=0.8))
        count+=1
        # continue
        if count >= timer:
            break
    
    img_coord = list(pyautogui.locateAllOnScreen(path_final, confidence=0.8))[occurrence]
    
    if action == "doubleClick":
        pyautogui.doubleClick(x = img_coord.left+(img_coord.width/2), y = img_coord.top+(img_coord.height/2))
    elif action == "click":
        pyautogui.click(x = img_coord.left+(img_coord.width/2), y = img_coord.top+(img_coord.height/2))
    elif action == "enter":
        pyautogui.hotkey("enter")
    elif action == "decalage":
        coord_X = img_coord.left+(img_coord.width/2) + decalageX
        coord_Y = img_coord.top+(img_coord.height/2) + decalageY
        pyautogui.click(x=coord_X, y=coord_Y)
    elif action == "rien":
        print("ok")
    else:
        print("Action introuvable")        


if __name__ == '__main__': 
    # gestion des chemins =====================================================
    path_main = pathlib.Path("C:/Users/Antedis/Documents/APE_2022/python_projects/automatisation_souris")
    path_input = pathlib.Path(path_main, 'input')
    path_output = pathlib.Path(path_main, 'output')

    # chemins images et csv
    path_img = pathlib.Path(path_input, 'img')
    path_csv = pathlib.Path(path_input, 'csv')
    
    # nom image
    nom_img = "gmail_connexion.png"
    
    test = waitAndAct(path_img, nom_img, action='', confidence=0.8)
    print(test)
    allscreen_waitAndAct(path_img, nom_img, action='doubleClick', confidence=0.8, decalageX=0, decalageY=0, occurrence=1, timer=200)
    # waitAndAct(path_img, nom_img, action='doubleClick', confidence=0.8, occurrence=1)
    