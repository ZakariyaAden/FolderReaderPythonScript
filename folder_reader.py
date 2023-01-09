import os
import time
from colorama import Fore,Style

path = input(Fore.CYAN + 'What is the directory would you like to scan\nIf you like to scan this folder, Press ENTER\n')

if path == '':
    pass
else:
    os.chdir(path)

def loading ():
    arr = 3
    for i in reversed(range(arr + 1)):
        msg = str(i)
        print(Fore.GREEN + msg + 's...')
        print(Style.RESET_ALL + '\n')
        time.sleep(1)
loading()

print(Fore.CYAN + 'Here is your CWD: ' + os.getcwd() + '\n' + 'The Contents: ' + str(os.listdir()))