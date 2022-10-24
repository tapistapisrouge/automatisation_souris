import time
from threading import Thread
from pynput import keyboard


def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            user_input = input('Program paused, would you like to continue? (y/n) ')

            while user_input != 'y' and user_input != 'n':
                user_input = input('Incorrect input, try either "y" or "n" ')

            if user_input == 'y':
                main.status = 'run'
            elif user_input == 'n':
                main.status = 'exit'
                exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'run'

    while True:
        print('running')
        time.sleep(1)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


Thread(target=main).start()
Thread(target=exit_program).start()




pyautogui.moveTo(1919, 1080, duration = 1)
pyautogui.moveTo(1, 1, duration = 1)

# cliquer sur un endroit à partir d'une image
path_img = pathlib.Path(path_input, 'var_explorer.png')
path_img_bis = str(path_img)
c = pyautogui.locateCenterOnScreen('C:/Users/Antedis/Documents/APE_2022\TEST/python_mouvement_souris/input/var_explorer.png')
pyautogui.click(c.x, c.y)
# c ==> Point(x=1450, y=508)

box = pyautogui.locateOnScreen('C:/Users/Antedis/Documents/APE_2022\TEST/python_mouvement_souris/input/var_explorer.png')  
# returns (left, top, width, height) of first place it is found
# Box(left=1398, top=497, width=105, height=23)
pyautogui.moveTo()

import random
random.randint(239, 1536) 