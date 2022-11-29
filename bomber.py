import pyautogui as pg

with open ('bomber.txt', 'w', encoding = 'utf-8') as f:
    for _ in range (1000):
        f.write('STAS LOX\n')
with open ('bomber.txt', 'r', encoding = 'utf-8') as f1:
    for line in f1:
        pg.write(line)
        pg.press('Enter')
