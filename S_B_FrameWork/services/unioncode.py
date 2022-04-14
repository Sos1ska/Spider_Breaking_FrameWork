# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
import datetime, time, os, shutil
from .LOGer import _error_, _debug_, _info_, _warning_

path=bytes

File = '111.py'
File2 = '222.py'

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
        other = Exception

class Main:
    try:
        class UnionCode:
            def Check_Started(self, path=path):
                Started = 'if __name__ == \'__main__\':'
                f = open(f'{path}', 'r')
                if Started in f.read():
                    f.close()
                    return 'Started Exists'
                else:
                    f.close()
                    return 'Started Not Found'
            ###
            helpfile = bytes
            mainfile = bytes
            def __init__(self, HelpFile, MainFile, Log=None, WayHelpFile=path, WayMainFile=path):
                self.helpfile=HelpFile
                self.mainfile=MainFile
                if Log == True:
                    MainModule = input('Main Module HelpFile>>> ')
                    _debug_(View='str', TEXT='Conclusion "input"', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                    try:
                        with open(f'{WayHelpFile+HelpFile}.py', 'r') as file:
                            datahelpfile = file.read()
                        _debug_(View='str', TEXT=f'Opened File along the way {WayHelpFile+HelpFile}.py . Opening mod "r"', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                    except FileNotFoundError as FNFE:
                        _error_(View='str', TEXT=f'{FNFE}', Sender='UnionCode', TypeError='CRITICAL', TypeMSG='Message')
                        _debug_(View='str', TEXT=f'Conclusion Error', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        raise HandlerError.Basic.SFNF(f'{FNFE}')
                    if MainModule in datahelpfile:
                        MainModuleExists = True
                    else:
                        MainModuleExists = False
                    ExistsStarted = self.Check_Started(path=f'{WayMainFile+MainFile}.py')
                    _debug_(View='str', TEXT=f'Checking Started "if __name__ == \'__main__\':". And droped "{ExistsStarted}"', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                    if ExistsStarted == 'Started Exists':
                        CreateFile = open(f'{WayMainFile+File}', 'w')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'try:\n')
                        _debug_(View='str', TEXT=f'Start off record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\tfrom .{HelpFile} import {MainModule}\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'except ImportError:\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\tfrom {HelpFile} import {MainModule}\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\tpass\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        MainFileOpen = open(f'{WayMainFile+MainFile}.py', 'r')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.writelines(f'{MainFileOpen.read()}')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.close()
                        _debug_(View='str', TEXT=f'Close file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        MainFileOpen.close()
                        os.remove(f'{WayMainFile+MainFile}.py')
                        _debug_(View='str', TEXT=f'REMOVE file {MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{MainFile}.py')
                        os.rename(file_oldname, file_newname)
                        _debug_(View='str', TEXT='RENAME files', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile2 = open(f'{WayMainFile+File2}', 'w')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+File2}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        HelpFileOpen = open(f'{WayHelpFile+HelpFile}.py', 'r')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayHelpFile+HelpFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile2.writelines(f'{HelpFileOpen.read()}')
                        _debug_(View='str', TEXT=f'Record in file {File2}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile2.close()
                        _debug_(View='str', TEXT=f'Close file {File2}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File2}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{HelpFile}.py')
                        os.rename(file_oldname, file_newname)
                        _debug_(View='str', TEXT='RENAME files', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        FileMainOpen = open(f'{WayMainFile+MainFile}.py', 'a')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        FileMainOpen.write(f'\n    {MainModule}()')
                        _debug_(View='str', TEXT=f'Record in file {MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        _info_(View='str', TEXT='OK', NickName='UnionCode', WriteTime=False)
                    elif ExistsStarted == 'Started Not Found':
                        CreateFile = open(f'{WayMainFile+File}', 'w')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'try:\n')
                        _debug_(View='str', TEXT=f'Start off record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\tfrom .{HelpFile} import {MainModule}\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'except ImportError:\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\tfrom {HelpFile} import {MainModule}\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\tpass\n')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        MainFileOpen = open(f'{WayMainFile+MainFile}.py', 'r')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.writelines(f'{MainFileOpen.read()}')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.write(f'\nif __name__ == \'__main__\':')
                        _debug_(View='str', TEXT=f'Record in file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile.close()
                        _debug_(View='str', TEXT=f'Close file {File}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        MainFileOpen.close()
                        os.remove(f'{WayMainFile+MainFile}.py')
                        _debug_(View='str', TEXT=f'REMOVE file {MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{MainFile}.py')
                        os.rename(file_oldname, file_newname)
                        _debug_(View='str', TEXT='RENAME files', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile2 = open(f'{WayMainFile+File2}', 'w')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+File2}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        HelpFileOpen = open(f'{WayHelpFile+HelpFile}.py', 'r')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayHelpFile+HelpFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile2.writelines(f'{HelpFileOpen.read()}')
                        _debug_(View='str', TEXT=f'Record in file {File2}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        CreateFile2.close()
                        _debug_(View='str', TEXT=f'Close file {File2}', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File2}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{HelpFile}.py')
                        os.rename(file_oldname, file_newname)
                        _debug_(View='str', TEXT='RENAME files', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        FileMainOpen = open(f'{WayMainFile+MainFile}.py', 'a')
                        _debug_(View='str', TEXT=f'Opening file along the way {WayMainFile+MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        FileMainOpen.write(f'\n    {MainModule}()')
                        _debug_(View='str', TEXT=f'Record in file {MainFile}.py', Sender='UnionCode', TypeMSG='DEBUG MODE', WriteTime=False)
                        _info_(View='str', TEXT='OK', NickName='UnionCode', WriteTime=False)
                elif Log is not True:
                    MainModule = input('Main Module HelpFile>>> ')
                    try:
                        with open(f'{WayHelpFile+HelpFile}.py', 'r') as file:
                            datahelpfile = file.read()
                    except FileNotFoundError as FNFE:
                        _error_(View='str', TEXT=f'{FNFE}', Sender='UnionCode', TypeError='CRITICAL', TypeMSG='Message')
                        raise HandlerError.Basic.SFNF(f'{FNFE}')
                    if MainModule in datahelpfile:
                        MainModuleExists = True
                    else:
                        MainModuleExists = False
                    ExistsStarted = self.Check_Started(path=f'{WayMainFile+MainFile}.py')
                    if ExistsStarted == 'Started Exists':
                        CreateFile = open(f'{WayMainFile+File}', 'w')
                        CreateFile.write(f'try:\n')
                        CreateFile.write(f'\tfrom .{HelpFile} import {MainModule}\n')
                        CreateFile.write(f'except ImportError:\n')
                        CreateFile.write(f'\tfrom {HelpFile} import {MainModule}\n')
                        CreateFile.write(f'\tpass\n')
                        MainFileOpen = open(f'{WayMainFile+MainFile}.py', 'r')
                        CreateFile.writelines(f'{MainFileOpen.read()}')
                        CreateFile.close()
                        MainFileOpen.close()
                        os.remove(f'{WayMainFile+MainFile}.py')
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{MainFile}.py')
                        os.rename(file_oldname, file_newname)
                        CreateFile2 = open(f'{WayMainFile+File2}', 'w')
                        HelpFileOpen = open(f'{WayHelpFile+HelpFile}.py', 'r')
                        CreateFile2.writelines(f'{HelpFileOpen.read()}')
                        CreateFile2.close()
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File2}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{HelpFile}.py')
                        os.rename(file_oldname, file_newname)
                        FileMainOpen = open(f'{WayMainFile+MainFile}.py', 'a')
                        FileMainOpen.write(f'\n    {MainModule}()')
                        _info_(View='str', TEXT='OK', NickName='UnionCode', WriteTime=False)
                    elif ExistsStarted == 'Started Not Found':
                        CreateFile = open(f'{WayMainFile+File}', 'w')
                        CreateFile.write(f'try:\n')
                        CreateFile.write(f'\tfrom .{HelpFile} import {MainModule}\n')
                        CreateFile.write(f'except ImportError:\n')
                        CreateFile.write(f'\tfrom {HelpFile} import {MainModule}\n')
                        CreateFile.write(f'\tpass\n')
                        MainFileOpen = open(f'{WayMainFile+MainFile}.py', 'r')
                        CreateFile.writelines(f'{MainFileOpen.read()}')
                        CreateFile.write(f'\nif __name__ == \'__main__\':')
                        CreateFile.close()
                        MainFileOpen.close()
                        os.remove(f'{WayMainFile+MainFile}.py')
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{MainFile}.py')
                        os.rename(file_oldname, file_newname)
                        CreateFile2 = open(f'{WayMainFile+File2}', 'w')
                        HelpFileOpen = open(f'{WayHelpFile+HelpFile}.py', 'r')
                        CreateFile2.writelines(f'{HelpFileOpen.read()}')
                        CreateFile2.close()
                        file_oldname = os.path.join(f'{WayMainFile}', f'{File2}')
                        file_newname = os.path.join(f'{WayMainFile}', f'{HelpFile}.py')
                        os.rename(file_oldname, file_newname)
                        FileMainOpen = open(f'{WayMainFile+MainFile}.py', 'a')
                        FileMainOpen.write(f'\n    {MainModule}()')
                        _info_(View='str', TEXT='OK', NickName='UnionCode', WriteTime=False)
            ###
            ###
        class UnionCodeWithDirectories:
            def Check_Started(self, path=path):
                Started = 'if __name__ == \'__main__\':'
                f = open(f'{path}', 'r')
                if Started in f.read():
                    f.close()
                    return 'Started Exists'
                else:
                    f.close()
                    return 'Started Not Found'
            def copytree(self, src, dst, symlinks=False, ignore=None):
                for item in os.listdir(src):
                    s = os.path.join(src, item)
                    d = os.path.join(dst, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, symlinks, ignore)
                    else:
                        shutil.copy2(s, d)
            helpfile = bytes
            mainfile = bytes
            def __init__(self, HelpFile, MainFile, WayHelpFile=path, WayMainFile=path):
                self.helpfile=HelpFile
                self.mainfile=MainFile
                MainModule = input('Main Module HelpFile>>> ')
                HelpDir = input('Name Dir HelpFile>>> ')
                try:
                    with open(f'{WayHelpFile+HelpFile}.py', 'r') as file:
                        datahelpfile = file.read()
                except FileNotFoundError as FNFE:
                    _error_(View='str', TEXT=f'{FNFE}', Sender='UnionCode', TypeError='CRITICAL', TypeMSG='Message')
                    raise HandlerError.Basic.SFNF(f'{FNFE}')
                if MainModule in datahelpfile:
                    MainModuleExists = True
                else:
                    MainModuleExists = False
                ExistsStarted = self.Check_Started(path=f'{WayMainFile+MainFile}.py')
                if ExistsStarted == 'Started Exists':
                    CreateFile = open(f'{WayMainFile+File}', 'w')
                    CreateFile.write(f'try:\n')
                    CreateFile.write(f'\tfrom .{HelpFile} import {MainModule}\n')
                    CreateFile.write(f'except ImportError:\n')
                    CreateFile.write(f'\tfrom {HelpFile} import {MainModule}\n')
                    CreateFile.write(f'\tpass\n')
                    MainFileOpen = open(f'{WayMainFile+MainFile}.py', 'r')
                    CreateFile.writelines(f'{MainFileOpen.read()}')
                    CreateFile.close()
                    MainFileOpen.close()
                    os.remove(f'{WayMainFile+MainFile}.py')
                    file_oldname = os.path.join(f'{WayMainFile}', f'{File}')
                    file_newname = os.path.join(f'{WayMainFile}', f'{MainFile}.py')
                    os.rename(file_oldname, file_newname)
                    CreateFile2 = open(f'{WayMainFile+File2}', 'w')
                    HelpFileOpen = open(f'{WayHelpFile+HelpFile}.py', 'r')
                    CreateFile2.writelines(f'{HelpFileOpen.read()}')
                    CreateFile2.close()
                    file_oldname = os.path.join(f'{WayMainFile}', f'{File2}')
                    file_newname = os.path.join(f'{WayMainFile}', f'{HelpFile}.py')
                    os.rename(file_oldname, file_newname)
                    FileMainOpen = open(f'{WayMainFile+MainFile}.py', 'a')
                    FileMainOpen.write(f'\n    {MainModule}()')
                    self.copytree(src=f'{WayHelpFile+HelpDir}', dst=f'{WayMainFile+HelpDir}')
                    _info_(View='str', TEXT='OK', NickName='UnionCode', WriteTime=False)
                elif ExistsStarted == 'Started Not Found':
                    CreateFile = open(f'{WayMainFile+File}', 'w')
                    CreateFile.write(f'try:\n')
                    CreateFile.write(f'\tfrom .{HelpFile} import {MainModule}\n')
                    CreateFile.write(f'except ImportError:\n')
                    CreateFile.write(f'\tfrom {HelpFile} import {MainModule}\n')
                    CreateFile.write(f'\tpass\n')
                    MainFileOpen = open(f'{WayMainFile+MainFile}.py', 'r')
                    CreateFile.writelines(f'{MainFileOpen.read()}')
                    CreateFile.write(f'\nif __name__ == \'__main__\':')
                    CreateFile.close()
                    MainFileOpen.close()
                    os.remove(f'{WayMainFile+MainFile}.py')
                    file_oldname = os.path.join(f'{WayMainFile}', f'{File}')
                    file_newname = os.path.join(f'{WayMainFile}', f'{MainFile}.py')
                    os.rename(file_oldname, file_newname)
                    CreateFile2 = open(f'{WayMainFile+File2}', 'w')
                    HelpFileOpen = open(f'{WayHelpFile+HelpFile}.py', 'r')
                    CreateFile2.writelines(f'{HelpFileOpen.read()}')
                    CreateFile2.close()
                    file_oldname = os.path.join(f'{WayMainFile}', f'{File2}')
                    file_newname = os.path.join(f'{WayMainFile}', f'{HelpFile}.py')
                    os.rename(file_oldname, file_newname)
                    FileMainOpen = open(f'{WayMainFile+MainFile}.py', 'a')
                    FileMainOpen.write(f'\n    {MainModule}()')
                    self.copytree(src=f'{WayHelpFile+HelpDir}', dst=f'{WayMainFile+HelpDir}')
                    _info_(View='str', TEXT='OK', NickName='UnionCode', WriteTime=False)
            ###
    except KeyboardInterrupt as KI:
        _warning_(View='str', TEXT='KeyboardInterrupt', TypeMSG='Message')
        time.sleep(2)
        _error_(View='str', TEXT='KeyboardInterrupt', Sender='UnionCode', TypeError='WARNING', TypeMSG='Message')
        raise Sos1skaKeyboardInterrupt(f'KeyboardInterrupt -> {KI}')