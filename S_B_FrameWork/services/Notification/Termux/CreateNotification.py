# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
from .Form import FORM_CREATE_SH_NOTIFICATION, FORM_CREATE_SH_TOAST


class MainCode_CreaterNotificationForTermux:
    text=str
    type=str
    def __init__(self, TEXT, Type):
        import os, random, time
        self.text=TEXT
        self.type=Type
        dir = os.path.abspath(os.curdir)
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