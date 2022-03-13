# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska

import json
import os
import bs4
import requests

__version__ = '0.0.1 [ BETA ]'

from ImportLoad import (Back, Fore, Style, debug, debug_log, error,
                          error_log, info, info_log, warning, warning_log,
                          win32)

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

colorwin32 = win32
colorwin32()

MODE = 'html', 'json'
MODE_VIEW = 'str', 'txt'

def send_request(link, data, proxy):
    send = requests.get(f"{link}{data}", proxies=proxy)
    return send.text

def check_mode(load_mode):
    for MODE in load_mode:
        if MODE in load_mode:
            return True
            break
        else:
            return False
            break

def check_real_data(load_link, load_data,):
    soup_check = bs4.BeautifulSoup(send_request(link=load_link, data=load_data, proxy=None), 'html.parser')
    try:
        check = soup_check.find('div', class_='error')
        if check.text == 'IP address is not valid / IP-адрес не действительный':
            return False
        else:
            return True
    except AttributeError:
        return True
        pass

def check_real_number(load_link, load_data):
    soup_check = bs4.BeautifulSoup(send_request(link=load_link, data=load_data, proxy=None), 'html.parser').text
    Handler=soup_check
    example = '{"status":404,"error":"Очень короткий номер телефона","phone":""}'
    if example in Handler:
        return False
    else:
        return True

class Main:
    class BreakHost:
        Domain = bytes
        mode = MODE
        view = MODE_VIEW
        def __init__(self, Mode, Domain, View = MODE_VIEW, load_proxy=bytes):
            """
            Structure for `txt` file
            >>> from S_B_FrameWork import BreakHost
            >>> Info = BreakHost(Domain="YOUR DOMAIN", View="txt")
            >>> f=open('YOUR WAY', 'a', encoding='utf-8')
            >>> f.write(Info)
            >>> f.close()

            Structure for `out` in `console`
            >>> from S_B_FrameWork import BreakHost
            >>> BreakHost(Domain="YOUR DOMAIN", View="str")
            """
            self.Domain = Domain
            self.mode = Mode
            self.view = View
            real_data = check_real_data(load_link='https://api.2ip.ua/hosting.json?site=', load_data=Domain)
            if real_data == False:
                if View == 'str':
                    error(TEXT='This domain does not exist', NickName=False, Sender='BreakHost', TypeMSG='INFORMATION', TypeError='Domain not exist')
                    raise Sos1skaError(f'Domain not exist, check the entered domain --> {Domain}')
                elif View == 'txt' or View == 'text':
                    error_log(TEXT='This domain does not exist', NickName=False, Sender='BreakHost', TypeMSG='INFORMATION', TypeError='Domain not exist')
                    return Sos1skaError(f'Domain not exist, check the entered domain --> {Domain}')
                else:
                    error_log(TEXT='This domain does not exist', NickName=False, Sender='BreakHost', TypeMSG='INFORMATION', TypeError='Domain not exist')
                    return Sos1skaError(f'Domain not exist, check the entered domain --> {Domain}')
            else:
                soup_json=bs4.BeautifulSoup(send_request(link='https://api.2ip.ua/hosting.json?site=', data=Domain, proxy=load_proxy), 'html.parser').text
                site_json=json.loads(soup_json)
                Handler=site_json
                if View == 'str':
                    try:
                        info(TEXT='%s' % (Handler["name_ripe"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["name_rus"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["site"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                elif View == 'txt' or View == 'text':
                    try:
                        info_log(TEXT='%s\n' % (Handler["name_ripe"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information\n', NickName=False)
                    try:
                        info_log(TEXT='%s\n' % (Handler["name_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information\n', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["site"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information\n', NickName=False)
                else:
                    try:
                        info_log(TEXT='%s\n' % (Handler["name_ripe"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information\n', NickName=False)
                    try:
                        info_log(TEXT='%s\n' % (Handler["name_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information\n', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["site"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information\n', NickName=False)
    class BreakIP:
        ip = bytes
        view = MODE_VIEW
        mode = MODE
        def __init__(self, Mode, IP, View=MODE_VIEW, load_proxy=bytes):
            """
            Structure for `txt` file
            >>> from S_B_FrameWork import BreakIP
            >>> Info = BreakIP(IP='YOUR IP', View='txt')
            >>> f=open('YOUR WAY', 'a', encoding='utf-8')
            >>> f.write(Info)
            >>> f.close()

            Structure for `out` in `console`
            >>> from S_B_FrameWork import BreakIP
            >>> BreakIP(IP='YOUR IP', View='str')
            """
            self.ip=IP
            self.view=View
            self.mode=Mode
            real_data = check_real_data(load_link='https://api.2ip.ua/geo.json?ip=', load_data=IP)
            if real_data == False:
                if View == 'str':
                    error(TEXT='This IP does not exist', NickName=False, Sender='BreakIP', TypeMSG='INFORMATION', TypeError='IP not exist')
                    raise Sos1skaError(f'IP not exist, check the entered IP --> {IP}')
                elif View == 'txt' or View == 'text':
                    error_log(TEXT='This IP does not exist', NickName=False, Sender='BreakIP', TypeMSG='INFORMATION', TypeError='IP not exist')
                    return Sos1skaError(f'IP not exist, check the entered IP --> {IP}')
                else:
                    error_log(TEXT='This IP does not exist', NickName=False, Sender='BreakIP', TypeMSG='INFORMATION', TypeError='IP not exist')
                    return Sos1skaError(f'IP not exist, check the entered IP --> {IP}')
            else:
                soup_json=bs4.BeautifulSoup(send_request(link='https://api.2ip.ua/geo.json?ip=', data=IP, proxy=load_proxy), 'html.parser').text
                site_json=json.loads(soup_json)
                Handler=site_json
                if View == 'str':
                    try:
                        info(TEXT='%s' % (Handler["country"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["country_rus"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["country_ua"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region_rus"]))
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region_ua"]))
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["city"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["city_rus"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["latitude"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["longitude"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["zip_code"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["time_zone"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                elif View == 'txt' or View == 'text':
                    try:
                        info_log(TEXT='%s' % (Handler["country"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["country_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["country_ua"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region_rus"]))
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region_ua"]))
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["city"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["city_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["latitude"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["longitude"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["zip_code"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["time_zone"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                else:
                    try:
                        info_log(TEXT='%s' % (Handler["country"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["country_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["country_ua"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region_rus"]))
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region_ua"]))
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["city"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["city_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["latitude"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["longitude"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["zip_code"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["time_zone"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
    class BreakISP:
        ip=bytes
        view=MODE_VIEW
        mode=MODE
        def __init__(self, Mode, IP, View=MODE_VIEW, load_proxy=bytes):
            """
            Structure `txt` file
            >>> from S_B_FrameWork import BreakISP
            >>> Info = BreakISP(IP='YOUR IP', View='txt')
            >>> f=open('YOUR WAY', 'a', encoding='utf-8')
            >>> f.write(Info)
            >>> f.close()
            
            Structure `out` in `console`
            >>> from S_B_FrameWork import BreakISP
            >>> BreakISP(IP='YOUR IP', View='str')
            """
            self.ip=IP
            self.view=View
            self.mode=Mode
            real_ip = check_real_data(load_link='https://api.2ip.ua/provider.json?ip=', load_data=IP)
            if real_ip == False:
                if View == 'str':
                    error(TEXT='This IP does not exist', NickName=False, Sender='BreakISP', TypeMSG='INFORMATION', TypeError='IP not exist')
                    raise Sos1skaError(f'IP not exist, check the entered IP --> {IP}')
                elif View == 'txt' or View == 'text':
                    error_log(TEXT='This IP does not exist', NickName=False, Sender='BreakISP', TypeMSG='INFORMATION', TypeError='IP not exist')
                    return Sos1skaError(f'IP not exist, check the entered IP --> {IP}')
                else:
                    error_log(TEXT='This IP does not exist', NickName=False, Sender='BreakISP', TypeMSG='INFORMATION', TypeError='IP not exist')
                    return Sos1skaError(f'IP not exist, check the entered IP --> {IP}')
            else:
                soup_json=bs4.BeautifulSoup(send_request(link='https://api.2ip.ua/provider.json?ip=', data=IP, proxy=load_proxy), 'html.parser').text
                site_json=json.loads(soup_json)
                Handler=site_json
                if View == 'str':
                    try:
                        info(TEXT='%s' % (Handler["name_ripe"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["name_rus"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["site"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["as"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["ip_range_start"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["ip_range_end"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["route"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["mask"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                elif View == 'txt' or View == 'text':
                    try:
                        info_log(TEXT='%s' % (Handler["name_ripe"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["name_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["site"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["as"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["ip_range_start"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["ip_range_end"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["route"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["mask"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                else:
                    try:
                        info_log(TEXT='%s' % (Handler["name_ripe"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["name_rus"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["site"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["as"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["ip_range_start"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["ip_range_end"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["route"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["mask"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
    class BreakMAC:
        mac=bytes
        view=MODE_VIEW
        mode=MODE
        def __init__(self, Mode, MAC, View=MODE_VIEW, load_proxy=bytes):
            """
            Structure `txt` file
            >>> from S_B_FrameWork import BreakMAC
            >>> Info = BreakMAC(MAC='YOUR MAC-ADDRESS', View='txt')
            >>> f=open('YOUR WAY', 'a', encoding='utf-8')
            >>> f.write(Info)
            >>> f.close()

            Structure `out` in `console`
            >>> from S_B_FrameWork import BreakMAC
            >>> BreakMAC(MAC='YOUR MAC-ADDRESS', View='str')
            """
            self.mac=MAC
            self.mode=Mode
            self.view=View
            real_data = check_real_data(load_link='https://api.2ip.ua/mac.json?mac=', load_data=MAC)
            if real_data == False:
                if View == 'str':
                    error(TEXT='This MAC-Address does not exist', NickName=False, Sender='BreakMAC', TypeMSG='INFORMATION', TypeError='MAC-Address not exist')
                    raise Sos1skaError(f'MAC-Address not exist, check the entered MAC-Address --> {MAC}')
                elif View == 'txt' or View == 'text':
                    error_log(TEXT='This MAC-Address does not exist', NickName=False, Sender='BreakMAC', TypeMSG='INFORMATION', TypeError='MAC-Address not exist')
                    return Sos1skaError(f'MAC-Address not exist, check the entered MAC-Address --> {MAC}')
                else:
                    error_log(TEXT='This MAC-Address does not exist', NickName=False, Sender='BreakMAC', TypeMSG='INFORMATION', TypeError='MAC-Address not exist')
                    return Sos1skaError(f'MAC-Address not exist, check the entered MAC-Address --> {MAC}')
            else:
                soup_json=bs4.BeautifulSoup(send_request(link='https://api.2ip.ua/mac.json?mac=', data=MAC, proxy=load_proxy), 'html.parser').text
                site_json=json.loads(soup_json)
                Handler=site_json
                if View == 'str':
                    try:
                        info(TEXT='%s' % (Handler["company"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["address"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["country"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["private"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["oui"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["block_size"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["data_created"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["data_updated"]))
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                elif View == 'txt' or View == 'text':
                    try:
                        info_log(TEXT='%s' % (Handler["company"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["address"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["country"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["private"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["oui"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["block_size"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["data_created"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["data_updated"]))
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)

# THIS MODULE IS UNDER TEST, WHEN CALLING IT MAY CAUSE FRAMEWORKA ERRORS AND CRASHES   
#         |
#         |
#         |
#         |
#         V
    class BreakNumCar:
        number=bytes
        view=MODE_VIEW
        mode=MODE
        result=str
        def __init__(self, Result, Mode, Number, View=MODE_VIEW, load_proxy=bytes):
            """
            `THIS MODULE IS UNDER TEST, WHEN CALLING IT MAY CAUSE FRAMEWORKA ERRORS AND CRASHES`

            If you have any suggestions for this `module`, write here ---> soshack00@gmail.com `or` https://vk.com/nikitasos1ska
            """
            self.number=Number
            self.mode=Mode
            self.view=View
            self.result=Result
            if Result == str(1):
                Mode = None
                View = None
                load_proxy = None
                import webbrowser
                webbrowser.open(url=f'https://avtocod.ru/proverkaavto/{Number}?rd=GRZ')
                webbrowser.open_new_tab(url=f'https://avtois.ru/num/{Number}/')
                debug(TEXT='The End', NickName=False, Sender='BreakNumCar', TypeMSG='INFORMATION')
            else:
                pass
            Mode = None
            View = None
            load_proxy = None
            import webbrowser
            webbrowser.open(url=f'https://avtocod.ru/proverkaavto/{Number}?rd=GRZ')
            webbrowser.open_new_tab(url=f'https://avtois.ru/num/{Number}/')
            debug(TEXT='The End', NickName=False, Sender='BreakNumCar', TypeMSG='INFORMATION')
    class BreakNumber:
        number=bytes
        view=MODE_VIEW
        mode=MODE
        def __init__(self, Mode, Number, View=MODE_VIEW, load_proxy=bytes):
            """
            Structure `txt` file
            >>> from S_B_FrameWork import BreakNumber
            >>> Info = BreakNumber(Number='YOUR NUMBER', View='txt')
            >>> f=open('YOUR WAY', 'a', encoding='utf-8')
            >>> f.write(Info)
            >>> f.close()

            Structure `out` in `console`
            >>> from S_B_FrameWork import BreakNumber
            >>> BreakNumber(Number='YOUR NUMBER', View='str')
            """
            self.number=Number
            self.mode=Mode
            self.view=View
            real_number = check_real_number(load_link='https://htmlweb.ru/json/mnp/phone/', load_data=Number)
            if real_number == False:
                if View == 'str':
                    error(TEXT='This Number Phone does not exist', NickName=False, Sender='BreakNumber', TypeMSG='INFORMATION', TypeError='Number Phone not exist')
                    raise Sos1skaError(f'Number Phone not exist, check the entered Number Phone --> {Number}')
                elif View == 'txt' or View == 'text':
                    error_log(TEXT='This Number Phone does not exist', NickName=False, Sender='BreakNumber', TypeMSG='INFORMATION', TypeError='Number Phone not exist')
                    return Sos1skaError(f'Number Phone not exist, check the entered Number Phone --> {Number}')
                else:
                    error_log(TEXT='This Number Phone does not exist', NickName=False, Sender='BreakNumber', TypeMSG='INFORMATION', TypeError='Number Phone not exist')
                    return Sos1skaError(f'Number Phone not exist, check the entered Number Phone --> {Number}')
            else:
                soup_json=bs4.BeautifulSoup(send_request(link='https://htmlweb.ru/json/mnp/phone/', data=Number, proxy=load_proxy), 'html.parser').text
                site_json=json.loads(soup_json)
                Handler=site_json
                if View == 'str':
                    try:
                        info(TEXT='%s' % (Handler["oper"]["id"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["oper"]["name"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["oper"]["country"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["oper"]["mnc"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["oper"]["brand"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["oper"]["url"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["route"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region"]["id"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region"]["name"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region"]["okrug"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["region"]["autocod"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                    try:
                        info(TEXT='%s' % (Handler["mobile"]), NickName=False)
                    except KeyError:
                        info(TEXT='No Information', NickName=False)
                elif View == 'txt' or View == 'text':
                    try:
                        info_log(TEXT='%s' % (Handler["oper"]["id"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["oper"]["name"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["oper"]["country"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["oper"]["mnc"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["oper"]["brand"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["oper"]["url"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["route"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region"]["id"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region"]["name"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region"]["okrug"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["region"]["autocod"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)
                    try:
                        info_log(TEXT='%s' % (Handler["mobile"]), NickName=False)
                    except KeyError:
                        info_log(TEXT='No Information', NickName=False)