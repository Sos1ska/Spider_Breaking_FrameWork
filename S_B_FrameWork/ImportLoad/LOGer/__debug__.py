# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska

import datetime

try:
    from ..ColorPython import win32 as colorwin32
    CP = True
except ModuleNotFoundError:
    CP = False
    pass

if CP == False or None:
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
def _debug_(TEXT, NickName=None, Sender=None, TypeMSG=None, WriteTime=True):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import debug
    Argument `NickName` - This argument displays a nickname, if you do not want to display a nickname, then skip or write
:Example with NickName
    >>> debug(TEXT="Hello World, I'm debug MSG", NickName='Sos1ska')
    [ Sos1ska ] - [ INFO Hello World, I'm debug MSG ]

:Example without

    >>> debug(TEXT="Hello World, I'm debug MSG", NickName=None # or False)
    [ root ] - [ INFO Hello World, I'm debug MSG ]
... OR
    >>> debug(TEXT="Hello World, I'm debug MSG")
    [ root ] - [ INFO Hello World, I'm debug MSG ]
    
Argument `Sender` - This argument displays where this message was sent from, if you do not want to display, you can skip

:Example with NickName, Sender
    >>> debug(TEXT="Hello World, I'm debug MSG", NickName="Sos1ska", Sender="System")
    [ Sos1ska ] - [ INFO Hello World, I'm debug MSG ] --- System
:Example with Sender
    >>> debug(TEXT="Hello World, I'm debug MSG", Sender="System")
    [ root ] - [ INFO Hello World, I'm debug MSG ] --- System

Argument `TypeMSG` - This argument outputs the message type, if you don't want to, you can skip it.

:Example with NickName, Sender, TypeMSG
    >>> debug(TEXT="Hello World, I'm debug MSG", NickName="Sos1ska", Sender="System", TypeMSG="ATTENTION")
    [ Sos1ska ] - [ INFO Hello World, I'm debug MSG ] --- System  <--- ATTENTION
:Example with Sender, TypeMSG
    >>> debug(TEXT="Hello World, I'm debug MSG", Sender="System", TypeMSG="ATTENTION")
    [ root ] - [ INFO Hello World, I'm debug MSG ] --- System  <--- ATTENTION
:Example with TypeMSG
    >>> debug(TEXT="Hello World, I'm debug MSG", TypeMSG="ATTENTION")
    [ root ] - [ INFO Hello World, I'm debug MSG ]  <--- ATTENTION

Argument `WriteTime` - This argument will print the current time along with the message.

:Example
    >>> debug(TEXT="Hello World, I'm debug MSG", WriteTime=True)
    [ root ] - [ INFO Hello World, I'm debug MSG ]  `Current time`
    """
    from .src.main_debug import _debug_
    colorwin32()
    if WriteTime==True:
        print(_debug_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG
        ) + str(datetime.datetime.now()))
    else:
        print(_debug_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG
        ))
def _debug_log(TEXT, NickName=None, Sender=None, TypeMSG=None, WriteTime=True):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import debug_log
    Write to your file
:Example
    >>> f=open('YOUR WAY', 'a', encoding='utf-8')
    >>> msg_for_write = debug_log(TEXT="Hello World, I'm debug MSG with log", NickName="Sos1ska", Sender="System", TypeMSG="ATTENTION", WriteTime=True)
    >>> f.write('%s' % (msg_for_write))
    >>> f.close()
    >>> with open('YOUR WAY', 'r') as file_log:
    >>>     data = file_log.read()
    >>> print(data)
    [ Sos1ska ] - [ DEBUG Hello World, I'm debug MSG with log ] --- System  <--- ATTENTION  `Current Time`
    """
    from .src.main_debug import _debug_for_log_
    if WriteTime==True:
        print(_debug_for_log_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG
        ) + str(datetime.datetime.now()))
    else:
        return _debug_for_log_(
            _TEXT_=TEXT,
            _Name=NickName,
            _Send=Sender,
            _MSG=TypeMSG
        )