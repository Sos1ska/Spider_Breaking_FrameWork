# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
import datetime, requests, bs4, json, time, os, sys
from typing import Any
from .LOGer import _error_, _debug_, _info_, _warning_
from .unioncode import Main as MainUnionCode

Root = 'root'

Text = str

View_dict = {
        'View':{
            'txt':  [
                    'text', 'txt', 'log', 'TXT', 'LOG'
                    ],
            'str':  [
                    'str', 'STR', 'out'
                    ]
        }
    }
View_dict_Info = {
    'View':{
        'OnlyInfo': [
            'INFO', 'info', 'Info', 'Only info', 'Only_Info', 'OnlyInfo', 'only info'
        ],
        'FullInfo': [
            'Full', 'full', 'Full', 'Full Info', 'Full_Info', 'FullInfo', 'full info'
        ]
    }
}

TypeVersion = {
    'Version':{
        'Windows': [
            'Win32', 'Win64', 'Windows', 'WINDOWS', 'windows', 'win', 'WIN', 'Win'
        ],
        'Termux': [
            'Termux', 'termux', 'Ter', 'ter', 'TERMUX', 'android', 'Android'
        ]
    }
}

class Sos1skaKeyboardInterrupt(KeyboardInterrupt):
    
    pass
class Sos1skaFileNotFound(FileNotFoundError):
    
    pass
class Sos1skaError(Exception):

    pass

class UserCodeError():
    class Sos1skaSyntaxError(SyntaxError):
        
        pass
    class Sos1skaModuleNotFound(ModuleNotFoundError):
        
        pass
    class Sos1skaImportError(ImportError):
        
        pass
class HandlerError():
    class Basic():
        SKI = Sos1skaKeyboardInterrupt
        SFNF = Sos1skaFileNotFound
        Error = Sos1skaError
    class UsersCode():
        SSE = UserCodeError.Sos1skaSyntaxError
        SMNF = UserCodeError.Sos1skaModuleNotFound
        SIE = UserCodeError.Sos1skaImportError
        other = Exception

class Main:
    # New 11:30 05.06.2022
    class CheckingPort:
        def scan_port(self, ip, port, DM, time=float):
            import socket
            if DM == True:
                send_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                send_request.timeout(time)
                try:
                    connect = send_request.connect((ip, port))
                    _info_(View='str', TEXT='Port open %s' % (port), NickName=Root, WriteTime=True)
                    send_request.close()
                except:
                    print(f'{ip}@ {port}')
                    pass
            elif DM == False:
                send_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                send_request.timeout(time)
                try:
                    connect = send_request.connect((ip, port))
                    print(f'Port open: {port}')
                    send_request.close()
                except:
                    print(f'{ip}@ {port}')
                    pass
        ip = bytes
        port = bytes
        flow = True or False
        dm = True or False
        start = int
        end = int
        startwithoutflow = int
        def __init__(self, IP, Flow, DM, start_if_Flow_equals_True, end_if_Flow_equals_True, check_port, timeout=float):
            self.ip = IP
            self.port = check_port
            self.flow = Flow
            self.dm = DM
            self.start = start_if_Flow_equals_True
            self.end = end_if_Flow_equals_True
            self.startwithoutflow = check_port
            if Flow == True:
                check_port = None
                for number_port in range(start_if_Flow_equals_True, end_if_Flow_equals_True):
                    if DM == True:
                        self.scan_port(ip=IP, port=number_port, DM=True, time=timeout)
                    elif DM == False:
                        self.scan_port(ip=IP, port=number_port, DM=False, time=timeout)
            elif Flow == False:
                start_if_Flow_equals_True = None
                end_if_Flow_equals_True = None
                if DM == True:
                    self.scan_port(ip=IP, port=check_port, DM=True, time=timeout)
                elif DM == False:
                    self.scan_port(ip=IP, port=check_port, DM=False, time=timeout)
            else:
                module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                module.EndWorkCode(self=Any, text=f'Not Found meaning -> DM={DM}', error=True, name_programm='CheckingPort{class}')
                raise HandlerError.UsersCode.other(f'Not Found meaning -> DM={DM}')
    #
    class BreakIP:
        ip = bytes
        mode = str
        def __init__(self, Mode, IP, load_proxy=None):
            self.ip = IP
            self.mode = Mode
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                if load_proxy == None:
                    
                    send_requests = requests.get(f'http://ip-api.com/json/{IP}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["status"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["country"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["countryCode"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["city"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["zip"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["timezone"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                    elif Mode == 'txt':
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["status"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["country"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["countryCode"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["city"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["zip"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["timezone"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                elif load_proxy is not None:
                    try:
                        
                        send_requests = requests.get(f'http://ip-api.com/json={IP}', proxies=load_proxy)
                        answer = send_requests.text
                        soup_json = bs4.BeautifulSoup(answer.json, 'html.parser').text
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["countryCode"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["city"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["zip"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["timezone"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif Mode == 'txt':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["countryCode"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["city"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["zip"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["timezone"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakIP', TypeError='CRITICAL', TypeMSG='Important')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakIP', TypeError='WARNING', TypeMSG='Message')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
    class BreakNumber:
        number = bytes
        mode = str
        typeinfo = str
        def __init__(self, Mode, NumberPhone, TypeInfo, load_proxy=None):
            self.number = NumberPhone
            self.mode = Mode
            self.typeinfo = TypeInfo
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                for k2, v2 in View_dict_Info["View"].items():
                    if TypeInfo in v2:
                        TypeInfo = k2
                if load_proxy == None:
                    send_requests = requests.get(f'https://htmlweb.ru/json/mnp/phone/{NumberPhone}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='str', TEXT='Satus>>> %s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                    if Mode == 'txt':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='txt', TEXT='Satus>>> %s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                if load_proxy is not None:
                    try:
                        send_requests = requests.get(f'https://htmlweb.ru/json/mnp/phone/{NumberPhone}', proxies=load_proxy)
                        answer = send_requests
                        soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='str', TEXT='Satus>>> %s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                        if Mode == 'txt':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='txt', TEXT='Satus>>> %s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakIP', TypeError='CRITICAL', TypeMSG='Important')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakNumber', TypeError='WARNING', TypeMSG='Message')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
    class BreakISP:
        ip=bytes
        mode=str
        typeinfo=str
        def __init__(self, Mode, IP, TypeInfo, load_proxy):
            self.ip=IP
            self.mode=Mode
            self.typeinfo=TypeInfo
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                for k2, v2, in View_dict_Info["View"].items():
                    if TypeInfo in v:
                        TypeInfo = k
                if load_proxy == None:
                    send_requests = requests.get(f'https://api.2ip.ua/provider.json?ip={IP}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='str', TEXT='IP>>> %s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Name AS>>> %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Mask>>> %s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                    elif Mode == 'txt':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='txt', TEXT='IP>>> %s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Name AS>>> %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Mask>>> %s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                elif load_proxy is not None:
                    try:
                        send_requests = requests.get(f'https://api.2ip.ua/provider.json?ip={IP}', proxies=load_proxy)
                        answer = send_requests
                        soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='str', TEXT='IP>>> %s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Name AS>>> %s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Mask>>> %s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                        elif Mode == 'txt':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='txt', TEXT='IP>>> %s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Name AS>>> %s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Mask>>> %s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakISP', TypeError='CRITICAL', TypeMSG='Important')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakISP', TypeError='WARNING', TypeMSG='Message')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
    class BreakMAC:
        mac=bytes
        mode=str
        typeinfo=str
        def __init__(self, Mode, MAC, TypeInfo, load_proxy):
            self.mac=MAC
            self.mode=Mode
            self.typeinfo=TypeInfo
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                for k2, v2 in View_dict_Info["View"].items():
                    if TypeInfo in v:
                        TypeInfo = k
                if load_proxy == None:
                    send_requests = requests.get(f'https://api.2ip.ua/mac.json?mac={MAC}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='str', TEXT='Name Company>>> %s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Address>>> %s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Private>>> %s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='OUI>>> %s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                    elif Mode == 'txt':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='txt', TEXT='Name Company>>> %s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Address>>> %s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Private>>> %s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='OUI>>> %s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                elif load_proxy is not None:
                    try:
                        send_requests = requests.get(f'https://api.2ip.ua/mac.json?mac={MAC}', proxies=load_proxy)
                        answer = send_requests
                        soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='str', TEXT='Name Company>>> %s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Address>>> %s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Private>>> %s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='OUI>>> %s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                        elif Mode == 'txt':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='txt', TEXT='Name Company>>> %s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Address>>> %s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Private>>> %s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='OUI>>> %s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakMAC', TypeError='CRITICAL', TypeMSG='Important')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakMAC', TypeError='WARNING', TypeMSG='Message')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')


def load_path(filepath):

    path, fname = os.path.split(filepath)
    modulename, _ = os.path.splitext(fname)

    if path not in sys.path:    
        sys.path.insert(0, path)

    return __import__(modulename)

with open(WayConfig, 'r') as file_j:
    data = json.load(file_j)
way = data["Way"]

View_DataBaseWork = {
    'View':{
        'PORT':  [
            'PORT', 'port', 'Port'
        ],
        'LOG':   [
            'LOG', 'Log', 'log'
        ],
        'SIMPLE': [
            'Simple DB', 'Simple DataBase', 'Simple', 'SIMPLE DB', 'SIMPLE DATABASE', 'SIMPLE'
        ]
    }
}

class Main_One_Dot_Zero:
    class CreateDataBaseBETA:
        _nametable = str 
        _way = str 
        _for = str
        def __init__(self, _NAMETABLE, _WAY, _FOR):
            """
            
            For `Spider-Breaking`
            
            """
            import sqlite3
            self._nametable = _NAMETABLE
            self._way = _WAY
            self._for = _FOR
            for k, v in View_DataBaseWork["View"].items():
                if _FOR in v:
                    _FOR = k
            if _FOR == 'LOG':
                x = 60*60
            #    if os.path.isfile(_WAY+'/DataBase/DataBaseLOG.db') == False:
            #        FileCreate = open(_WAY+'/DataBase/DataBaseLOG.db', 'w')
            #        FileCreate.close()
            #        pass
            #    elif os.path.isfile(_WAY+'/DataBase/DataBaseLOG.db') == True:
            #        pass
            #    connect_sqlite = sqlite3.connect(_WAY+'/DataBase/DataBaseLOG.db')
            #    cur = connect_sqlite.cursor()
            #    cur.execute(f"""CREATE TABLE {_NAMETABLE} (
            #        UserType TEXT,
            #        InfoType TEXT,
            #        Info TEXT,
            #        Time TEXT
            #        );
            #        """)
            #    connect_sqlite.commit()
            #    connect_sqlite.close()
                _info_(View='str', TEXT='You are trying to use restricted content!', NickName='DEVELOPER _{Sos1ska}_')
                command = True
                while command:
                    time.sleep(1)
                    x = x - 1
                    print(f'Time: {x}', end='\r')
                    if x == 0:
                        pass
                quit()
            elif _FOR == 'PORT':
                if os.path.isfile(_WAY+'/DataBase/DataBasePORT.db') == False:
                    FileCreate = open(_WAY+'/DataBase/DataBasePORT.db', 'w')
                    FileCreate.close()
                    pass
                elif os.path.isfile(_WAY+'/DataBase/DataBasePORT.db') == True:
                    pass
                connect_sqlite = sqlite3.connect(_WAY+'/DataBase/DataBasePORT.db')
                cur = connect_sqlite.cursor()
                cur.execute(f"""CREATE TABLE {_NAMETABLE} (
                    IP TEXT,
                    PORT INT
                    );
                    """)
                connect_sqlite.commit()
                connect_sqlite.close()
            elif _FOR == 'Simple':
                if os.path.isfile(_WAY+f'/DataBase/DataBase.db') == False:
                    FileCreate = open(_WAY+f'/DataBase/DataBase.db', 'w')
                    FileCreate.close()
                    pass
                elif os.path.isfile(_WAY+f'/DataBase/DataBase{_NAMETABLE}.db') == True:
                    pass
                connect_sqlite = sqlite3.connect(_WAY+f'/DataBase/DataBase.db')
                cur = connect_sqlite.cursor()
                cur.execute(f"""CREATE TABLE {_NAMETABLE} (
                    NumberPhone TEXT,
                    IP TEXT,
                    MAC TEXT,
                    ISP TEXT);
                    """)
                connect_sqlite.commit()
                connect_sqlite.close()
    class BreakIP:
        ip = bytes
        mode = str
        def __init__(self, Mode, IP, load_proxy=None):
            self.ip = IP
            self.mode = Mode
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                if load_proxy == None:
                    
                    send_requests = requests.get(f'http://ip-api.com/json/{IP}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["status"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["country"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["countryCode"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["city"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["zip"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["timezone"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                        try:
                            _info_(View='str', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                        except KeyError:
                            _info_(View='str', TEXT='Not Found Information')
                    elif Mode == 'txt':
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["status"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["country"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["countryCode"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["city"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["zip"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["timezone"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                        try:
                            _info_(View='txt', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                        except KeyError:
                            _info_(View='txt', TEXT='Not Found Information')
                elif load_proxy is not None:
                    try:
                        
                        send_requests = requests.get(f'http://ip-api.com/json={IP}', proxies=load_proxy)
                        answer = send_requests.text
                        soup_json = bs4.BeautifulSoup(answer.json, 'html.parser').text
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["countryCode"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["city"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["zip"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["timezone"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif Mode == 'txt':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["countryCode"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]) + ' %s' % (Handler["regionName"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["city"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["zip"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["lat"]) + ' %s' % (Handler["lon"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["timezone"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["isp"]) + ' %s' % (Handler["org"]) + ' %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakIP', TypeError='CRITICAL', TypeMSG='Important')
                        my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                        my_module.EndWorkCode(self=Any, text='Proxt server not working or no internet access', error=True, name_programm='BreakIP{class}')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt as ki:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakIP', TypeError='WARNING', TypeMSG='Message')
                my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                my_module.EndWorkCode(self=Any, text=ki, error=True, name_programm='BreakIP{class}')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
    class BreakNumber:
        number = bytes
        mode = str
        typeinfo = str
        def __init__(self, Mode, NumberPhone, TypeInfo, load_proxy=None):
            self.number = NumberPhone
            self.mode = Mode
            self.typeinfo = TypeInfo
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                for k2, v2 in View_dict_Info["View"].items():
                    if TypeInfo in v2:
                        TypeInfo = k2
                if load_proxy == None:
                    send_requests = requests.get(f'https://htmlweb.ru/json/mnp/phone/{NumberPhone}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='str', TEXT='Satus>>> %s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                    if Mode == 'txt':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='txt', TEXT='Satus>>> %s' % (Handler["status"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                if load_proxy is not None:
                    try:
                        send_requests = requests.get(f'https://htmlweb.ru/json/mnp/phone/{NumberPhone}', proxies=load_proxy)
                        answer = send_requests
                        soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='str', TEXT='Satus>>> %s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                        if Mode == 'txt':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='txt', TEXT='Satus>>> %s' % (Handler["status"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='ID Oper>>> %s' % (Handler["oper"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper Name>>> %s' % (Handler["oper"]["name"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper Country>>> %s' % (Handler["oper"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper MNC>>> %s' % (Handler["oper"]["mnc"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Oper Name Brand And URL>>> %s' % (Handler["oper"]["brand"]) + ' %s' % (Handler["oper"]["url"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='ID Number>>> %s' % (Handler["region"]["id"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Name Region>>> %s' % (Handler["region"]["name"]) + ' %s' % (Handler["region"]["okrug"]) + ' %s' % (Handler["region"]["english"]) + ' %s' % (Handler["region"]["iso"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='AUTOCOD Region>>> %s' % (Handler["region"]["autocod"]) + ' %s' % (Handler["region"]["capital"]) + ' %s' % (Handler["region"]["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Work Mobile>>> %s' % (Handler["mobile"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakNumber', TypeError='CRITICAL', TypeMSG='Important')
                        my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                        my_module.EndWorkCode(self=Any, text='Proxy server not working or no internet access', error=True, name_programm='BreakNumber{class}')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt as ki:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakNumber', TypeError='WARNING', TypeMSG='Message')
                my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                my_module.EndWorkCode(self=Any, text=ki, error=True, name_programm='BreakNumber{class}')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
    class BreakISP:
        ip=bytes
        mode=str
        typeinfo=str
        def __init__(self, Mode, IP, TypeInfo, load_proxy):
            self.ip=IP
            self.mode=Mode
            self.typeinfo=TypeInfo
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                for k2, v2, in View_dict_Info["View"].items():
                    if TypeInfo in v:
                        TypeInfo = k
                if load_proxy == None:
                    send_requests = requests.get(f'https://api.2ip.ua/provider.json?ip={IP}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='str', TEXT='IP>>> %s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Name AS>>> %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Mask>>> %s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                    elif Mode == 'txt':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='txt', TEXT='IP>>> %s' % (Handler["ip"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Name AS>>> %s' % (Handler["as"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Mask>>> %s' % (Handler["mask"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                elif load_proxy is not None:
                    try:
                        send_requests = requests.get(f'https://api.2ip.ua/provider.json?ip={IP}', proxies=load_proxy)
                        answer = send_requests
                        soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='str', TEXT='IP>>> %s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Name AS>>> %s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Mask>>> %s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                        elif Mode == 'txt':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='txt', TEXT='IP>>> %s' % (Handler["ip"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Name ISP And Name RUS And Site>>> %s' % (Handler["name_ripe"]) + ' %s' % (Handler["name_rus"]) + ' %s' % (Handler["site"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Name AS>>> %s' % (Handler["as"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='IP Range Start And IP Range End>>> %s' (Handler["ip_range_start"]) + ' %s' % (Handler["ip_range_end"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Route>>> %s' % (Handler["route"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Mask>>> %s' % (Handler["mask"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakISP', TypeError='CRITICAL', TypeMSG='Important')
                        my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                        my_module.EndWorkCode(self=Any, text='Proxy server not working or no internet access', error=True, name_programm='BreakISP{class}')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt as ki:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakISP', TypeError='WARNING', TypeMSG='Message')
                my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                my_module.EndWorkCode(self=Any, text=ki, error=True, name_programm='BreakISP{class}')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
    class BreakMAC:
        mac=bytes
        mode=str
        typeinfo=str
        def __init__(self, Mode, MAC, TypeInfo, load_proxy):
            self.mac=MAC
            self.mode=Mode
            self.typeinfo=TypeInfo
            try:
                for k, v in View_dict["View"].items():
                    if Mode in v:
                        Mode = k
                for k2, v2 in View_dict_Info["View"].items():
                    if TypeInfo in v:
                        TypeInfo = k
                if load_proxy == None:
                    send_requests = requests.get(f'https://api.2ip.ua/mac.json?mac={MAC}')
                    answer = send_requests
                    soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = json.loads(soup_json)
                    Handler = site_json
                    if Mode == 'str':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='str', TEXT='Name Company>>> %s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Address>>> %s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Private>>> %s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='OUI>>> %s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                            try:
                                _info_(View='str', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='str', TEXT='Not Found Information')
                    elif Mode == 'txt':
                        if TypeInfo == 'OnlyInfo':
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                        elif TypeInfo == 'FullInfo':
                            try:
                                _info_(View='txt', TEXT='Name Company>>> %s' % (Handler["company"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Address>>> %s' % (Handler["address"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Private>>> %s' % (Handler["private"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='OUI>>> %s' % (Handler["oui"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                            try:
                                _info_(View='txt', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                            except KeyError:
                                _info_(View='txt', TEXT='Not Found Information')
                elif load_proxy is not None:
                    try:
                        send_requests = requests.get(f'https://api.2ip.ua/mac.json?mac={MAC}', proxies=load_proxy)
                        answer = send_requests
                        soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                        site_json = json.loads(soup_json)
                        Handler = site_json
                        if Mode == 'str':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='str', TEXT='Name Company>>> %s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Address>>> %s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Private>>> %s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='OUI>>> %s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                                try:
                                    _info_(View='str', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='str', TEXT='Not Found Information')
                        elif Mode == 'txt':
                            if TypeInfo == 'OnlyInfo':
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='%s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                            elif TypeInfo == 'FullInfo':
                                try:
                                    _info_(View='txt', TEXT='Name Company>>> %s' % (Handler["company"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Address>>> %s' % (Handler["address"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Country>>> %s' % (Handler["country"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Private>>> %s' % (Handler["private"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='OUI>>> %s' % (Handler["oui"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Block Size>>> %s' % (Handler["block_size"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                                try:
                                    _info_(View='txt', TEXT='Date Created And Date Updated>>> %s' % (Handler["date_created"]) + ' %s' % (Handler["date_updated"]))
                                except KeyError:
                                    _info_(View='txt', TEXT='Not Found Information')
                    except requests.exceptions.ProxyError:
                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakMAC', TypeError='CRITICAL', TypeMSG='Important')
                        my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                        my_module.EndWorkCode(self=Any, text='Proxy server not working or no internet access', error=True, name_programm='BreakMAC{class}')
                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
            except KeyboardInterrupt as ki:
                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
                time.sleep(2)
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakMAC', TypeError='WARNING', TypeMSG='Message')
                my_module = load_path(r'S_B_FrameWork\services\endworkcode.pyc')
                my_module.EndWorkCode(self=Any, text=ki, error=True, name_programm='BreakMAC{class}')
                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')
