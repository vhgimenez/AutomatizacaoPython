import pyperclip
from time import sleep
import pyautogui

pyautogui.PAUSE = 1
pyautogui.hotkey('win')
pyautogui.write("chrome")
pyautogui.press("enter")
link = "youtube.com"
pyperclip.copy(link)
sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.hotkey("ctrl", "t")
sleep(1)
link2 = r'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
pyperclip.copy(link2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=115, y=255)
sleep(3)
pyautogui.write("impressaogimenez@gmail.com")
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write("Produto Entregue!")
pyautogui.press("tab")
texto = """"
    Olá Victor Espero que tenha apreciado a sua compra recente de produto.
    Se o achou útil, gostaríamos que nos ajudasse e a outras pessoas que também gostariam de comprá-lo. Para tal, você poderia visitar esta página [inserir link] e deixar um comentário? Deve demorar menos de três minutos.
    Nós realmente apreciamos a sua ajuda.
    Obrigado,

    Victor Gimenez
"""
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=1360, y=978)
sleep(1)
pyautogui.write('download.png')
pyautogui.press('enter')
sleep(5)
pyautogui.hotkey('ctrl', 'enter')