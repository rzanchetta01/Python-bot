import pandas as pd
import pyautogui as pag
import time

numbers = pd.read_csv('T:\Python Workspace\Etiquetas Algoritmo\codigos GRU.csv')
numbers_filter = numbers['codigos']
    

time.sleep(30)
count = 0
count2 = 0
#bot para gerar docs
for num in numbers_filter:
    
    pag.typewrite(num)
    pag.press("tab")


pag.hotkey("ctrl", "b")
pag.alert('Fim bot')