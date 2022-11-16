import pandas as pd
import pyautogui as pag
import time

numbers = pd.read_csv('T:\Python Workspace\Etiquetas Algoritmo\codigos GRU.csv')
numbers_filter = numbers['codigos']
    

time.sleep(30) # For opening word

#Typing
for num in numbers_filter:
    
    pag.typewrite(num)
    pag.press("tab")


pag.hotkey("ctrl", "b") # saving
pag.alert('Fim bot')