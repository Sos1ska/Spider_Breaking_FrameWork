# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
from typing import Any
from .Form import FORM_CREATE_SH_NOTIFICATION, FORM_CREATE_SH_TOAST
from ....Config import WayConfig
import os, sys, json


def load_path(filepath):

    path, fname = os.path.split(filepath)
    modulename, _ = os.path.splitext(fname)

    if path not in sys.path:    
        sys.path.insert(0, path)

    return __import__(modulename)

with open(WayConfig, 'r') as file_j:
    data = json.load(file_j)
way = data["Way"]

class MainCode_CreaterNotificationForTermux:
    text=str
    type=str
    def __init__(self, TEXT, Type):
        import os, random, time
        self.text=TEXT
        self.type=Type
        dir = os.path.abspath(os.curdir)
        try:
            if Type == 'Notification':
                name_file = random.randint(0, 2147483600)
                file = open(f'{dir}/{name_file}.sh', 'w', encoding='utf-8')
                file.write(FORM_CREATE_SH_NOTIFICATION(f'{TEXT}'))
                file.close()
                os.system(f'sh {dir}/{name_file}.sh')
                time.sleep(10)
                os.remove(f'{dir}/{name_file}.sh')
            elif Type == 'Toast':
                name_file = random.randint(0, 2147483600)
                file = open(f'{dir}/{name_file}.sh', 'w', encoding='utf-8')
                file.write(FORM_CREATE_SH_TOAST(f'{TEXT}'))
                file.close()
                os.system(f'sh {dir}/{name_file}.sh')
                time.sleep(10)
                os.remove(f'sh {dir}/{name_file}.sh')
        except Exception as e:
            my_module = load_path(way)
            my_module.EndWorkCode(self=Any, text=e, error=True, name_programm='CreateNotification[S_B_FrameWork].py')