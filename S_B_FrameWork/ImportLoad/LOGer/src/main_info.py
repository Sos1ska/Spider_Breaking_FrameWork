from ..__info__ import Root
from .Tools import *

def _info_(_TEXT_, _Name):
    if _Name == None or _Name == False:
        NN = False
    else:
        NN = True
    if NN == True:
        return f'[ {_Name} ] - [ {ForeGreen}{StyleBlod}INFO{StyleRESET} {_TEXT_} ]  '
    else:
        return f'[ {Root} ] - [ {ForeGreen}{StyleBlod}INFO{StyleRESET} {_TEXT_} ]  '
def _info_for_log_(_TEXT_, _Name):
    if _Name == None or _Name == False:
        NN = False
    else:
        NN = True
    if NN == True:
        return f'[ {_Name} ] - [ {_TEXT_} ]  '
    else:
        return f'[ {Root} ] - [ {_TEXT_} ]  '