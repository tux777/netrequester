import os, json, colorama
from components.testing.test import test

settings = {}

if __name__ == '__main__':
    try:
        os.system("clear")
    except:
        os.system("cls")

    with open('./config/startup.json', 'r') as config:
        settings = json.load(config)

    if settings["auto_test"] == True:
        print(f"{colorama.Fore.CYAN}-----Starting Tests!-----{colorama.Fore.RESET}\n")
        test()