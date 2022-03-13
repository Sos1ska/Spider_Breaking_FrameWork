from ..WARNINGLOCAL import Root
from .Tools import *

def __warning__(_TEXT_, _Name, _MSG):
    if _Name == None or _Name == False:
        NN = False
    else:
        NN = True
    if _MSG == None or _MSG == False:
        msg = False
    else:
        msg = True
    if NN == True:
        if msg == True:
            return f'[ {_Name} ] - [ {ForeYellow}{StyleBlod}WARNING{StyleRESET} {_TEXT_} ]  <--- {_MSG}  '
        else:
            return f'[ {_Name} ] - [ {ForeYellow}{StyleBlod}WARNING{StyleRESET} {_TEXT_} ]  '
    else:
        if msg == True:
            return f'[ {Root} ] - [ {ForeYellow}{StyleBlod}WARNING{StyleRESET} {_TEXT_} ]  <--- {_MSG}  '
        else:
            return f'[ {Root} ] - [ {ForeYellow}{StyleBlod}WARNING{StyleRESET} {_TEXT_} ]  '