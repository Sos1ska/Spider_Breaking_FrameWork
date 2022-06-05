import os, sys, getpass, time, shutil, ctypes
from typing import Any

def load_path(filepath):

    path, fname = os.path.split(filepath)
    modulename, _ = os.path.splitext(fname)

    if path not in sys.path:    
        sys.path.insert(0, path)

    return __import__(modulename)

class Ways:
    Config = 'S_B_FrameWork\\Config.py'
    ConfigJ = 'S_B_FrameWork\\Config.json'
    endpyc = 'S_B_FrameWork\\services\\end.pyc'
    versionpyc = 'S_B_FrameWork\\services\\version.pyc'

def reinstallation(self, path=bytes):
    systemdrive = os.getenv("SystemDrive")
    os.remove(path=path)
    shutil.copytree(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\Spider_Breaking_FrameWork-sos-utils\\', path+'\\Lib\\S_B_FrameWork')
    with open(f'{path}\\Lib\\{Ways.Config}', 'w') as createfile:
        createfile.write(f'WayConfig=r\'{path}\\Lib\\{Ways.ConfigJ}\'')
        createfile.close()
    with open(f'{path}\\Lib\\{Ways.ConfigJ}', 'w') as createfile:
        createfile.write('{\n')
        createfile.write(f'\t"Way":"{path}\\Lib\\{Ways.endpyc}", "WayVersion":"{path}\\Lib\\{Ways.versionpyc}"\n')
        createfile.write('}')
        createfile.close()
    module = load_path(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\Spider_Breaking_FrameWork-sos-utils\\endsetup.pyc')
    module.done(self=Any, text=None, error=False, name_programm='setup.py')
    time.sleep(10)
    quit()

def main(self):
    systemdrive = os.getenv("SystemDrive")
    check_python_folder_systemdrive = os.path.isdir(systemdrive+'Users\\'+getpass.getuser()+'\\AppData\\Local\\Programs\\Python\\Python39')
    if check_python_folder_systemdrive == False:
        check_python_folder_again = os.path.isdir(systemdrive+'Users\\'+getpass.getuser()+'\\AppData\\Local\\Programs\\Python\\Python310')
        if check_python_folder_again == False:
            print('The language is not installed or is not on the system drive')
            x = 60*60
            command = True
            while command:
                time.sleep(1)
                x = x - 1
                print(f'Time: {x}', end='\r')
                if x == 0:
                    pass
            quit()
        else:
            shutil.move(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\Spider_Breaking_FrameWork-sos-utils\\S_B_FrameWork', f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\S_B_FrameWork')
            try:
                shutil.copytree(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\S_B_FrameWork', systemdrive+'Users\\'+getpass.getuser()+'\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\')
            except FileExistsError:
                reinstallation(self=Any, path=check_python_folder_again)
            module = load_path(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\Spider_Breaking_FrameWork-sos-utils\\endsetup.pyc')
            module.done(self=Any, text=None, error=False, name_programm='setup.py')
            time.sleep(10)
            quit()
    else:
        shutil.move(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\Spider_Breaking_FrameWork-sos-utils\\S_B_FrameWork', f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\S_B_FrameWork')
        try:
            shutil.copytree(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\S_B_FrameWork', systemdrive+'Users\\'+getpass.getuser()+'\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\')
        except FileExistsError:
            reinstallation(self=Any, path=check_python_folder_again+'\\Lib\\S_B_FrameWork')
        module = load_path(f'{systemdrive}\\Users\\{getpass.getuser()}\\Downloads\\Spider_Breaking_FrameWork-sos-utils\\endsetup.pyc')
        module.done(self=Any, text=None, error=False, name_programm='setup.py')
        time.sleep(10)
        quit()
if ctypes.windll.shell32.IsUserAnAdmin():
    if __name__ == "__main__":
        main(self=Any)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)