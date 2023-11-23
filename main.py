import os, json
from components.testing.test import test

settings = {}

if __name__ == '__main__':
    with open('./config/startup.json', 'r') as config:
        settings = json.load(config)

    for i in settings:
        match i:

            case "auto_test":
                if settings[i] == True:
                    test()