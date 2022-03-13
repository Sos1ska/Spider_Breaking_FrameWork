# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska

import datetime

try:
    from ImportLoad.ColorPython import win32 as colorwin32
    CP = True
except ImportError:
    CP = False
    pass

if CP == False:
    def out():
        return '[ root ] - [ ERROR ImportError ] --- ModuleNotFound \'ColorPython\', \'win32\' CRITICAL'
    print(out())
    quit()
else:
    pass

Root='root'

from .src.Tools import (BackBlack, BackBlue, BackCyan, BackGreen,
                        BackLightGrey, BackOrange, BackPurple, BackRed,
                        BackRESET, ForeBlack, ForeBlue, ForeCyan, ForeDarkGrey,
                        ForeGreen, ForeLightBlue, ForeLightCyan,
                        ForeLightGreen, ForeLightGrey, ForeLightRed,
                        ForeOrange, ForePing, ForePurple, ForeRed, ForeRESET,
                        ForeYellow, StyleBlod, StyleDisable, StyleInvisuble,
                        StyleRESET, StyleReverse, StyleStrikethrought,
                        StyleUnderline)

def _warning(TEXT, NickName=None, TypeMSG=None, WriteTime=True):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import warning
    Argument `NickName` - This argument displays a nickname, if you do not want to display a nickname, then skip or write
:Example with NickName
    >>> warning(TEXT="Hello World, I'm warning MSG", NickName='Sos1ska')
    [ Sos1ska ] - [ WARNING Hello World, I'm warning MSG ]

Argument `TypeMSG` - This argument outputs the message type, if you don't want to, you can skip it.

:Example with NickName
    >>> warning(TEXT="Hello World, I'm warning MSG", NickName='Sos1ska', TypeMSG='ATTENTION')
    [ Sos1ska ] - [ WARNING Hello World, I'm warning MSG ]  <--- ATTENTION
:Example without NickName
    >>> warning(TEXT="Hello World, I'm warning MSG", TypeMSG='ATTENTION')
    [ root ] - [ WARNING Hello World, I'm warning MSG ]  <--- ATTENTION
    """
    from .src.main_warning import __warning__
    colorwin32()
    if WriteTime == True:
        print(__warning__(
            _TEXT_=TEXT,
            _Name=NickName,
            _MSG=TypeMSG
        ) + str(datetime.datetime.now()))
    else:
        print(__warning__(
            _TEXT_=TEXT,
            _Name=NickName,
            _MSG=TypeMSG
        ))

def _warning_log(TEXT, NickName=None, TypeMSG=None, WriteTime=True):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import warning_log
    Write to your file
:Example
    >>> f=open('YOUR WAY', 'a', encoding='utf-8')
    >>> msg_for_write = warning_log(TEXT="Hello World, I'm warning MSG with log", TypeMSG="ATTENTION", WriteTime=True)
    >>> f.write('%s' % (msg_for_write))
    >>> f.close()
    >>> with open('YOUR WAY', 'r') as file_log:
    >>>     data = file_log.read()
    >>> print(data)
    [ Sos1ska ] - [ WARNING Hello World, I'm warning MSG ]  <--- ATTENTION  `Current Time`
    """