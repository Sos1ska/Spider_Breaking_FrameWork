from ..__debug__ import Root
from .Tools import *
def _debug_(_TEXT_, _Name, _Send, _MSG):
    if _Name == None or _Name == False:
        NN = False
    else:
        NN = True
    if _Send == None or _Send == False:
        send = False
    else:
        send = True
    if _MSG == None or _MSG == False:
        msg = False
    else:
        msg = True
    if NN == True:
        if send == True:
            if msg == True:
                return f'[ {_Name} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ] --- {_Send}  <--- {_MSG}  '
            else:
                return f'[ {_Name} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ] --- {_Send}  '
        else:
            return f'[ {_Name} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ]  '
    else:
        if send == True:
            if msg == True:
                return f'[ {Root} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ] --- {_Send}  <--- {_MSG}  '
            else:
                return f'[ {Root} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ] --- {_Send}  '
        else:
            if msg == True:
                return f'[ {Root} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ]  <--- {_MSG}  '
            else:
                return f'[ {Root} ] - [ {ForeGreen}{StyleBlod}{StyleUnderline}INFO{StyleRESET} {_TEXT_} ]  '
def _debug_for_log_(_TEXT_, _Name, _Send, _MSG):
    if _Name == None or _Name == False:
        NN = False
    else:
        NN = True
    if _Send == None or _Send == False:
        send = False
    else:
        send = True
    if _MSG == None or _MSG == False:
        msg = False
    else:
        msg = True
    if NN == True:
        if send == True:
            if msg == True:
                return f'[ {_Name} ] - [ DEBUG {_TEXT_} ] --- {_Send}  <--- {_MSG}  '
            else:
                return f'[ {_Name} ] - [ DEBUG {_TEXT_} ] --- {_Send}  '
        else:
            return f'[ {_Name} ] - [ DEBUG {_TEXT_} ]  '
    else:
        if send == True:
            if msg == True:
                return f'[ {Root} ] - [ DEBUG {_TEXT_} ] --- {_Send}  <--- {_MSG}  '
            else:
                return f'[ {Root} ] - [ DEBUG {_TEXT_} ] --- {_Send}  '
        else:
            if msg == True:
                return f'[ {Root} ] - [ DEBUG {_TEXT_} ]  <--- {_MSG}  '
            else:
                return f'[ {Root} ] - [ DEBUG {_TEXT_} ]  '