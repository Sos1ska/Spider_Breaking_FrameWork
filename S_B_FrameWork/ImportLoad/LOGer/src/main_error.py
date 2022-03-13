from ..__error__ import Root
from .Tools import *
def _error_(_TEXT_, _Name, _Send, _MSG, _TypeError):
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
    if _TypeError == None or _TypeError == False:
        TE = False
    else:
        TE = True
    if NN == True:
        if send == True:
            if msg == True:
                if TE == True:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError} --- {_Send}  <--- {_MSG} '
                else:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_Send}  <--- {_MSG} '
            else:
                if TE == True:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError} --- {_Send} '
                else:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_Send} '
        else:
            if msg == True:
                if TE == True:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError}  <--- {_MSG} '
                else:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ]  <--- {_MSG} '
            else:
                if TE == True:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError} '
                else:
                    return f'[ {_Name} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] '
    else:
        if send == True:
            if msg == True:
                if TE == True:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError} --- {_Send}  <--- {_MSG} '
                else:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_Send}  <--- {_MSG} '
            else:
                if TE == True:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError} --- {_Send} '
                else:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_Send}'
        else:
            if msg == True:
                if TE == True:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError}  <--- {_MSG} '
                else:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ]  <--- {_MSG}'
            else:
                if TE == True:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] --- {_TypeError} '
                else:
                    return f'[ {Root} ] - [ {ForeRed}{StyleBlod}ERROR{StyleRESET} {_TEXT_} ] '
def _error_for_log_(_TEXT_, _Name, _Send, _MSG, _TypeError):
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
    if _TypeError == None or _TypeError == False:
        TE = False
    else:
        TE = True
    if NN == True:
        if send == True:
            if msg == True:
                if TE == True:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Send}  <--- {_MSG}  '
                else:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ] --- {_Send}  <--- {_MSG}  '
            else:
                if TE == True:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Send}  '
                else:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ] --- {_Send} '
        else:
            if msg == True:
                if TE == True:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ] --- {_TypeError}  <--- {_MSG}  '
                else:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ]  <--- {_MSG}  '
            else:
                if TE == True:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ] --- {_TypeError}  '
                else:
                    return f'[ {_Name} ] - [ ERROR {_TEXT_} ]  '
    else:
        if send == True:
            if msg == True:
                if TE == True:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Send}  <--- {_MSG}  '
                else:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ] --- {_Send}  <--- {_MSG}  '
            else:
                if TE == True:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Send}  '
                else:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ] --- {_Send}  '
        else:
            if msg == True:
                if TE == True:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ] --- {_TypeError}  <--- {_MSG}  '
                else:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ]  <--- {_MSG}  '
            else:
                if TE == True:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ] --- {_TypeError}  '
                else:
                    return f'[ {Root} ] - [ ERROR {_TEXT_} ]  '