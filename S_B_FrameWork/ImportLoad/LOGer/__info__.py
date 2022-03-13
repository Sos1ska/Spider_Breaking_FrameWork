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

def _info_(TEXT, NickName=None, WriteTime=True):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import info
    Argument `NickName` - This argument displays a nickname, if you do not want to display a nickname, then skip or write
:Example with NickName
    >>> info(TEXT="Hello World, I'm info MSG", NickName='Sos1ska')
    [ Sos1ska ] - [ INFO Hello World, I'm info MSG ]
    """
    from .src.main_info import _info_
    colorwin32()
    if WriteTime == True:
        print(_info_(
            _TEXT_=TEXT,
            _Name=NickName
        ) + str(datetime.datetime.now()))
    else:
        print(_info_(
            _TEXT_=TEXT,
            _Name=NickName
        ))
def _info_log(TEXT, NickName=None, WriteTime=True):
    """
    >>> from Spider_Breaking_API.ImportLoad.LOGer import info_log
    Write to your file
:Example
    >>> f=open('YOUR WAY', 'a', encoding='utf-8')
    >>> msg_for_write = info_log(TEXT="Hello World, WriteTime=True)
    >>> f.write('%s' % (msg_for_write))
    >>> f.close()
    >>> with open('YOUR WAY', 'r') as file_log:
    >>>     data = file_log.read()
    >>> print(data)
    [ Sos1ska ] - [ INFO Hello World ]  `Current Time`
    """
    from .src.main_info import _info_for_log_
    if WriteTime == True:
        return _info_for_log_(
            _TEXT_=TEXT,
            _Name=NickName
        ) + str(datetime.datetime.now())
    else:
        return _info_for_log_(
            _TEXT_=TEXT,
            _Name=NickName
        )