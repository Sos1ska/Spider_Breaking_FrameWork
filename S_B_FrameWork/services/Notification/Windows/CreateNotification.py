# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
from .Form import FORM_CREATE_VBS
from .ListParametersMSG import *

class MainCode_CreaterNotificationForWindows():
    def Help(self):
        print('''
Argument: Text
    This argument passes text in any format to your msg
Argument: Title
    This argument passes the header in any format to your msg
Argument: ParametersMSG
    This argument passes the form msg, more on off. website https://docs.microsoft.com/ru-ru/office/vba/language/reference/user-interface-help/msgbox-function
                OR
    Open source file ListParametersMSG.py
Argument: Buffer 'Default False' 
    This argument creates a folder called Buffer, this folder will contain the source codes for running msg
    
    The True argument generates the source code to run and then removes it
''')
    def CreateNotification(self, Text, Title, ParametersMSG, Buffer = False):
        if Buffer == False:
            pass
        else:
            pass   
        import random
        import os
        import subprocess
        dir = os.path.abspath(os.curdir)
        name_file = random.randint(0, 2147483600)
        file = open(f'{dir}\\{name_file}.vbs', 'w', encoding='UTF-16 LE')
        file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
        file.close()
        subprocess.call(f'cscript {dir}\\{name_file}.vbs')
        os.remove(f'{dir}\\{name_file}.vbs')