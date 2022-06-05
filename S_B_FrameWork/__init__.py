from typing import Any
from time import sleep
from .services import Main as Main_S_B_FrameWork
from .services import MainUnionCode
from .services import _debug_ as debug
from .services import _error_ as error
from .services import _info_ as info
from .services import _warning_ as warning
from .services.Notification.Windows.CreateNotification import (
    MainCode_CreaterNotificationForWindows, vbAbortRetryIgnore,
    vbApplicationModal, vbCritical, vbDefaultButton1, vbDefaultButton2,
    vbDefaultButton3, vbDefaultButton4, vbExclamation, vbInformation,
    vbMsgBoxHelpButton, vbMsgBoxRight, vbMsgBoxRtlReading,
    vbMsgBoxSetForeground, vbOKCancel, vbOKOnly, vbQuestion, vbRetryCancel,
    vbSystemModal, vbYesNo, vbYesNoCancel)
from .services.Notification.Windows.CreateNotification import MainCode_CreaterNotificationForWindows as NotificationWindows
from .services.Notification.Termux.CreateNotification import MainCode_CreaterNotificationForTermux as NotificationTermux
from .services import Main_One_Dot_Zero as Main_S_B_FrameWorkNew_ONE_DOT_ZERO
###
def Instruction(self):
    print('\t\t\tUnionCode\n')
    print('>>> from S_B_FrameWork import MainUnionCode')
    print('>>> MainUnionCode.UnionCode(HelpFile="YOUR NAME SECOND FILE, DO NOT BET ".py"", MainFile="YOUR NAME FIRST FILE, DO NOT BET ".py"", Log=False "or True", WayHelpFile="YOUR WAY TO SECOND FILE, DO NOT BET WITH NAME FILE", WayMainFile="YOUR WAY TO FIRST FILE, DO NOT BET WITH NAME FILE"')
    print()
    print()
    print('\t\tUnionCodeWithDirectories\n')
    print('>>> from S_B_FrameWork import MainUnionCode')
    print('>>> MainUnionCode.UnionCodeWithDirectories(HelpFile="YOUR NAME SECOND FILE, DO NOT BET ".py"", MainFile="YOUR NAME FIRST FILE, DO NOT BET ".py"", WayHelpFile="YOUR WAY TO SECOND FILE, DO NOT BET WITH NAME FILE", WayMainFile="YOUR WAY TO FIRST FILE, DO NOT BET WITH NAME FILE"')
    print()
    print()
    print('\t\t\tServices')
    print('>>> from S_B_FrameWork import Main_S_B_FrameWork')
    print('Get Info Number Phone')
    print('>>> Main_S_B_FrameWork.BreakNumber(Mode="str or txt", NumberPhone="YOUR NUMBER PHONE", TypeInfo="OnlyInfo or FullInfo", load_proxy=None"or YOUR PROXY")')
    print()
    print('Get Info IP')
    print('>>> Main_S_B_FrameWork.BreakIP(Mode="str or txt", IP="YOUR IP", load_proxy=None"or YOUR PROXY")')
    print()
    print('Get Info MAC-Address')
    print('>>> Main_S_B_FrameWork.BreakMAC(Mode="str or txt", MAC="YOUR MAC-Address", TypeInfo="OnlyInfo or FullInfo", load_proxy=None"or YOUR PROXY")')
    print()
    print('Get Info ISP')
    print('>>> Main_S_B_FrameWork.BreakISP(Mode="str or txt", IP="YOUR ISP", TypeInfo="OnlyInfo or FullInfo", load_proxy=None"or YOUR PROXY")')
    cont = input('> ')
    print()
    print()
    print()
    print('\t\t\tLOGer\n')
    print('>>> from S_B_FrameWork import info, debug, error, warning')
    print()
    print('Out Info')
    print('>>> info(View="str or txt", TEXT="YOUR TEXT", NickName="YOUR NICKNAME", WriteTime=True "or False"')
    print('Out Debug')
    print('>>> debug(View="str or txt", TEXT="YOUR TEXT", NickName="YOUR NICKNAME", Sender="YOUR NAME FILE OR NICKNAME", TypeMSG="YOUR TYPE", WriteTime=True "or False"')
    print('Out Error')
    print('>>> error(View="str or txt", TEXT="YOUR TEXT", NickName="YOUR NICKNAME", Sender="YOUR NAME FILE OR NICKNAME", TypeError="YOUR NAME TYPE ERROR" TypeMSG="YOUR TYPE", WriteTime=True "or False"')
    print('Out Warning')
    print('>>> warning(View="str or txt", TEXT="YOUR TEXT", NickName="YOUR NICKNAME", Sender="YOUR NAME FILE OR NICKNAME", TypeMSG="YOUR TYPE", WriteTime=True "or False"')
###
###
def CheckUpdate(self):
    import requests, json, os, sys, bs4
    from Config import WayConfig
    url = 'https://raw.githubusercontent.com/Sos1ska/Spider_Breaking_FrameWork/sos-utils/S_B_FrameWork/version.json'
    def load_path(filepath):

        path, fname = os.path.split(filepath)
        modulename, _ = os.path.splitext(fname)

        if path not in sys.path:    
            sys.path.insert(0, path)

        return __import__(modulename)
    with open(WayConfig) as file_j:
        data = json.load(file_j)
    way = data["WayVersion"]
    versioncloud = requests.get(url=url)
    answer = versioncloud
    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
    site_json = json.loads(soup_json)
    Handler = site_json
    versionlocal = load_path(way)
    if int(Handler["version"]) >> int(versionlocal.version):
        print('update available!')
    else:
        pass
    if 'b2' in Handler["typeversion"]:
        if 'b2' in versionlocal.typeversion:
            pass
        else:
            print('update available!')
    else:
        if 'b2' in versionlocal.typeversion:
            pass
        else:
            print('update available!')
###
if __name__ == '__main__':
    CheckUpdate(self=Any)
    print(Instruction(self=Any))
else:
    CheckUpdate()
    sleep(2)