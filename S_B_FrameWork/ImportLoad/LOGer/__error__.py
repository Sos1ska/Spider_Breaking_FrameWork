# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska

import datetime

try:
    from ..ColorPython import win32 as colorwin32
    CP = True
except:
    CP = False
    pass

if CP == False:
    def out():
        return '[ root ] - [ ERROR ImportError ] --- ModuleNotFound \'ColorPython\', \'win32\' CRITICAL'
    print(out())
    quit()
else:
    pass

Root = 'root'

from .src.Tools import (BackBlack, BackBlue, BackCyan, BackGreen,
                        BackLightGrey, BackOrange, BackPurple, BackRed,
                        BackRESET, ForeBlack, ForeBlue, ForeCyan, ForeDarkGrey,
                        ForeGreen, ForeLightBlue, ForeLightCyan,
                        ForeLightGreen, ForeLightGrey, ForeLightRed,
                        ForeOrange, ForePing, ForePurple, ForeRed, ForeRESET,
                        ForeYellow, StyleBlod, StyleDisable, StyleInvisuble,
                        StyleRESET, StyleReverse, StyleStrikethrought,
                        StyleUnderline)
Text = str
def _error_(TEXT=Text, NickName=None, Sender=None, TypeMSG=None, WriteTime=True, TypeError=None):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import error
    Argument `NickName` - This argument displays a nickname, if you do not want to display a nickname, then skip or write
:Example with NickName
    >>> error(TEXT="Hello World, I'm error MSG", NickName="Sos1ska")
    [ Sos1ska ] - [ ERROR Hello World, I'm error MSG ]

:Example without
    
    >>> error(TEXT="Hello World, I'm error MSG", NickName=None # or False)
    [ root ] - [ ERROR Hello World, I'm error MSG ]
... OR
    >>> error(TEXT="Hello World, I'm error MSG"))
    [ root ] - [ ERROR Hello World, I'm error MSG ]

Argument `Sender` - This argument displays where this message was sent from, if you do not want to display, you can skip

:Example with NickName, Sender
    >>> error(TEXT="Hello World, I'm error MSG", NickName="Sos1ska", Sender="System")
    [ Sos1ska ] - [ ERROR Hello World, I'm error MSG ] --- System
:Example with Sender
    >>> error(TEXT="Hello World, I'm error MSG", Sender="System")
    [ root ] - [ ERROR Hello World, I'm error MSG ] --- System

Argument `Sender` - This argument displays where this message was sent from, if you do not want to display, you can skip

:Example with NickName, Sender
    >>> error(TEXT="Hello World, I'm error MSG", NickName="Sos1ska", Sender="System")
    [ Sos1ska ] - [ ERROR Hello World, I'm error MSG ] --- System
:Example with Sender
    >>> error(TEXT="Hello World, I'm error MSG", Sender="System")
    [ root ] - [ ERROR Hello World, I'm error MSG ] --- System

Argument `TypeMSG` - This argument outputs the message type, if you don't want to, you can skip it.

:Example with NickName, Sender, TypeMSG
    >>> error(TEXT="Hello World, I'm error MSG", NickName="Sos1ska", Sender="System", TypeMSG="ATTENTION")
    [ Sos1ska ] - [ ERROR Hello World, I'm error MSG ] --- System  <--- ATTENTION
:Example with Sender, TypeMSG
    >>> error(TEXT="Hello World, I'm error MSG", Sender="System", TypeMSG="ATTENTION")
    [ root ] - [ ERROR Hello World, I'm error MSG ] --- System  <--- ATTENTION
:Example with TypeMSG
    >>> error(TEXT="Hello World, I'm error MSG", TypeMSG="ATTENTION")
    [ root ] - [ ERROR Hello World, I'm error MSG ]  <--- ATTENTION

Argument `TypeError` - This argument gives the error type, if you don't want to, you can skip it.

:Example with NickName, Sender, TypeMSG, TypeError
    >>> error(TEXT="Hello World, I'm error MSG", NickName="Sos1ska", Sender="System", TypeMSG="ATTENTION", TypeError='TEST')
    [ Sos1ska ] - [ ERROR Hello World, I'm error MSG ] --- TEST --- System  <--- ATTENTION

Argument `WriteTime` - This argument will print the current time along with the message.

:Example
    >>> error(TEXT="Hello World, I'm error MSG", WriteTime=True))
    [ root ] - [ ERROR Hello World, I'm error MSG ]  `Current time`
    """
    from .src.main_error import _error_
    colorwin32()
    if WriteTime == True:
        print(_error_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG,
            _TypeError=TypeError
        ) + str(datetime.datetime.now()))
    else:
        return _error_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG,
            _TypeError=TypeError
        )
def _error_log(TEXT=Text, NickName=None, Sender=None, TypeMSG=None, WriteTime=None, TypeError=None):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import error_log
    Write to your file
:Example
    >>> f=open('YOUR WAY', 'a', encoding='utf-8')
    >>> msg_for_write = error_log(TEXT="Hello World, I'm error MSG with log", NickName="Sos1ska", Sender="System", TypeMSG="ATTENTION", WriteTime=True)
    >>> f.write('%s' % (msg_for_write))
    >>> f.close()
    >>> with open('YOUR WAY', 'r') as file_log:
    >>>     data = file_log.read()
    >>> print(data)
    [ Sos1ska ] - [ ERROR Hello World, I'm error MSG with log ] --- System  <--- ATTENTION  `Current Time`
    """
    from .src.main_error import _error_for_log_
    if WriteTime==True:
        return _error_for_log_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG,
            _TypeError=TypeError
        ) + str(datetime.datetime.now())
    else:
        return _error_for_log_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG,
            _TypeError=TypeError
        )