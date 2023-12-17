import os, json, colorama
from components.testing.test import test
from components.menu import start

settings = {}

def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")

if __name__ == '__main__':
    clear()

    with open('./config/startup.json', 'r') as config:
        settings = json.load(config)

    if settings["auto_test"] == True:
        print(f"{colorama.Fore.CYAN}-----Starting Tests!-----{colorama.Fore.RESET}\n")
        test()
    
    clear()
    start()