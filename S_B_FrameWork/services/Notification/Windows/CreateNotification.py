# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
from typing import Any
from .Form import FORM_CREATE_VBS
from ...LOGer import _info_, _debug_
from .ListParametersMSG import *
from ....Config import WayConfig
import random, os, subprocess, sys, json

root = 'root'

def load_path(filepath):

    path, fname = os.path.split(filepath)
    modulename, _ = os.path.splitext(fname)

    if path not in sys.path:    
        sys.path.insert(0, path)

    return __import__(modulename)

with open(WayConfig, 'r') as file_j:
    data = json.load(file_j)
way = data["Way"]

class MainCode_CreaterNotificationForWindows:
    text = bytes
    title = bytes
    parameter = str
    buffer = True or False
    dm = True or False
    def _NotificationWithoutBuffer(self, Text, Title, ParametersMSG, DM):
        if DM == False:
            dir = os.path.abspath(os.curdir)
            name_file = random.randint(0, 2147483600)
            file = open(f'{dir}\\{name_file}.vbs', 'a', encoding='UTF-16 LE')
            file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
            file.close()
            try:
                subprocess.call(f'cscript {dir}\\{name_file}.vbs')
            except FileNotFoundError as fnfe:
                my_module = load_path(way)
                my_module.EndWorkCode(self=Any, text=fnfe, error=True, name_programm='CreateNotification[S_B_FrameWork].py')
                quit()
            os.remove(f'{dir}/{name_file}.vbs')
        elif DM == True:
            _debug_(View='str', TEXT='Debug Mode turn on', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            dir = os.path.abspath(os.curdir)
            name_file = random.randint(0, 2147483600)
            file = open(f'{dir}\\{name_file}.vbs', 'w', encoding='UTF-16 LE')
            _debug_(View='str', TEXT='Create File', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
            _debug_(View='str', TEXT='Record in File', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            file.close()
            _debug_(View='str', TEXT='Performance File in Virtualization-Based Security')
            try:
                subprocess.call(f'cscript {dir}\\{name_file}.vbs')
            except FileNotFoundError as fnfe:
                my_module = load_path(way)
                my_module.EndWorkCode(self=Any, text=fnfe, error=True, name_programm='CreateNotification[S_B_FrameWork].py')
                quit()
            _debug_(View='str', TEXT='Performance Delete File', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            os.remove(f'{dir}/{name_file}.vbs')
            my_module = load_path(way)
            my_module.EndWorkCode(self=Any, text=None, error=False, name_programm='CreateNotification[S_B_FrameWork].py')
    def _NotificationWithBuffer(self, Text, Title, ParametersMSG, Buffer, DM):
        if DM == False:
            dir = Buffer
            name_file = random.randint(0, 2147483600)
            file = open(f'{dir}\\{name_file}.vbs', 'w', encoding='UTF-16 LE')
            file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
            file.close()
            try:
                subprocess.call(f'cscript {dir}\\{name_file}.vbs')
            except FileNotFoundError as fnfe:
                my_module = load_path(way)
                my_module.EndWorkCode(self=Any, text=fnfe, error=True, name_programm='CreateNotification[S_B_FrameWork].py')
                quit()
        elif DM == True:
            _debug_(View='str', TEXT='Debug Mode turn on', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            dir = os.path.abspath(os.curdir)
            name_file = random.randint(0, 2147483600)
            file = open(f'{dir}\\{name_file}.vbs', 'a', encoding='UTF-16 LE')
            _debug_(View='str', TEXT='Create File', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
            _debug_(View='str', TEXT='Record in File', NickName=root, Sender=None, TypeMSG='{DM}', WriteTime=True)
            file.close()
            _debug_(View='str', TEXT='Performance File in Virtualization-Based Security')
            try:
                subprocess.call(f'cscript {dir}\\{name_file}.vbs')
            except FileNotFoundError as fnfe:
                my_module = load_path(way)
                my_module.EndWorkCode(self=Any, text=fnfe, error=True, name_programm='CreateNotification[S_B_FrameWork].py')
                quit()
            my_module = load_path(way)
            my_module.EndWorkCode(self=Any, text=None, error=False, name_programm='CreateNotification[S_B_FrameWork].py')
    def __init__(self, Text, Title, ParametersMSG, Buffer=False, DM=True):
        self.text=Text
        self.title=Title
        self.parameter=ParametersMSG
        self.buffer=Buffer
        self.dm = DM
        if DM == True:
            if not Buffer == False:
                self._NotificationWithBuffer(Text=Text, Title=Title, ParametersMSG=ParametersMSG, Buffer=Buffer, DM=DM)
            else:
                self._NotificationWithoutBuffer(Text=Text, Title=Title, ParametersMSG=ParametersMSG, DM=DM)
        elif DM == False:
            if not Buffer == False:
                self._NotificationWithBuffer(Text=Text, Title=Title, ParametersMSG=ParametersMSG, Buffer=Buffer, DM=DM)
            else:
                self._NotificationWithoutBuffer(Text=Text, Title=Title, ParametersMSG=ParametersMSG, DM=DM)
        else:
            my_module = load_path(filepath=way)
            my_module.EndWorkCode(self=Any, text='Not Found meaning', error=True, name_programm='CreateNotification[S_B_FrameWork].py')