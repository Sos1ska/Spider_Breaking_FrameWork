# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
import datetime

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

def _main_debug_(_TEXT_, _NickName, _Sender, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if msg == True:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] --- {_Sender} '
    else:
        if msg == True:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ]'

def _main_info_(_TEXT_, _NickName):
    return f'[ {_NickName} ] - [ INFO {_TEXT_} ] '

def _main_error_(_TEXT_, _NickName, _Sender, _TypeError, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeError == False or _TypeError == None:
        _TE = False
    else:
        _TE = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Sender} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_Sender}'
    else:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ]'
    
def _main_warning_(_TEXT_, _NickName, _TypeMSG):
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if msg == True:
        return f'[ {_NickName} ] - [ WARNING {_TEXT_} ] <--- {_TypeMSG} '
    else:
        return f'[ {_NickName} ] - [ WARNING {_TEXT_} ]'

def _debug_(View, TEXT=Text, NickName=Root, Sender=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View =='str':
        if WriteTime == True:
            print(
                _main_debug_(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_debug_(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_debug_(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
        else:
            return _main_debug_(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                )
def _info_(View, TEXT=Text, NickName=Root, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) 
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
        else:
            return _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                )
def _error_(View, TEXT=Text, NickName=Root, Sender=None, TypeError=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_error_(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now()))
        else:
            print(
                _main_error_(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_error_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now())
        else:
            return _main_error_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                )

def _warning_(View, TEXT=Text, NickName=Root, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_warning_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_warning_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_warning_(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            ) + str(datetime.datetime.now())
        else:
            return _main_warning_(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            )

if __name__ == '__main__':
    _debug_(View='str', TEXT='This is "str" `View`', NickName=Root, Sender=Root, TypeMSG='TEST')
    print(_debug_(View='txt', TEXT='This is "txt" `View`', NickName=Root, Sender=Root, TypeMSG='TEST'))
    print("1. _debug_(View='str', TEXT='This is \"str\" `View`', NickName=Root, Sender=Root, TypeMSG='TEST')")
    print("2. print(_debug(View='txt', TEXT='This is \"txt\" `View`', NickName=Root, Sender=Root, TypeMSG='TEST'))")
    _error_(View='str', TEXT='This is "str" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST')
    print(_error_(View='txt', TEXT='This is "txt" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST'))
    print("""1. _error_(View='str', TEXT='This is "str" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST')""")
    print("""2. print(_error_(View='txt', TEXT='This is "txt" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST'))""")
    _info_(View='str', TEXT='This is "str" `View`', NickName=Root)
    print(_info_(View='txt', TEXT='This is "txt" `View`', NickName=Root))
    print("""1. _info_(View='str', TEXT='This is "str" `View`', NickName=Root)""")
    print("""2. print(_info_(View='txt', TEXT='This is "txt" `View`', NickName=Root))""")
    _warning_(View='str', TEXT='This is "str" `View`', NickName=Root, TypeMSG='TEST')
    print(_warning_(View='txt', TEXT='This is "txt" `View`', NickName=Root, TypeMSG='TEST'))
    print("""1. _warning_(View='str', TEXT='This is "str" `View`', NickName=Root, TypeMSG='TEST')""")
    print("""2. print(_warning_(View='txt', TEXT='This is "txt" `View`', NickName=Root, TypeMSG='TEST'))""")