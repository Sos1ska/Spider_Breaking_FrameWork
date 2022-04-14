# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
import datetime, requests, bs4, json, time, os
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

__version__ = '0.9 [ BETA ]'

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
    class BreakIP:
        ip = bytes
        mode = str
        def __init__(self, Mode, IP, load_proxy=None):
            self.domain = IP
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
                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakHost', TypeError='WARNING', TypeMSG='Message')
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
#    class BreakNumCar:
#        numbercar = bytes
#        mode = str
#        typeinfo = str
#        def __init__(self, Mode, NumberCar, TypeInfo, load_proxy=None):
#            self.mode = Mode
#            self.numbercar = NumberCar
#            self.typeinfo = TypeInfo
#            try:
#                for k, v in View_dict["View"].items():
#                    if Mode in v:
#                        Mode = k
#               for k2, v2, in View_dict["View"].items():
#                    if TypeInfo in v2:
#                        TypeInfo = k2
#                if load_proxy == None:
#                    pass
#                elif load_proxy is not None:
#                    try:
#                        pass
#                    except requests.exceptions.ProxyError:
#                        _error_(View='str', TEXT='Proxy server not working or no internet access', NickName=Root, Sender='BreakNumCar', TypeError='CRITICAL', TypeMSG='Important')
#                        raise HandlerError.UsersCode.other('Proxy server not working or no internet access')
#            except KeyboardInterrupt:
#                _warning_(View='str', TEXT='KeyboardInterrupt', NickName=Root, TypeMSG='Message')
#                time.sleep(2)
#                _error_(View='str', TEXT='KeyboardInterrupt', NickName=Root, Sender='BreakISP', TypeError='WARNING', TypeMSG='Message')
#                raise Sos1skaKeyboardInterrupt('KeyboardInterrupt, pressed "CTRL+C"')