#                             |----=== Sos1ska ===----|                                                                               #
# |----=== https://vk.com/nikitasos1ska <----> https://github.com/Sos1ska ===----                                                     #

class _Fore(object):
    BLACK='\033[30m'
    RED='\033[31m'
    GREEN='\033[32m'
    ORANGE='\033[33m'
    BLUE='\033[34m'
    PURPLE='\033[35m'
    CYAN='\033[36m'
    LIGHTGREY='\033[37m'
    DARKGREY='\033[90m'
    LIGHTRED='\033[91m'
    LIGHTGREEN='\033[92m'
    YELLOW='\033[93m'
    LIGHTBLUE='\033[94m'
    PINK='\033[95m'
    LIGHTCYAN='\033[96m'
    RESET='\033[39m'

class _BackGround(object):
    BLACK='\033[40m'
    RED='\033[41m'
    GREEN='\033[42m'
    ORANGE='\033[43m'
    BLUE='\033[44m'
    PURPLE='\033[45m'
    CYAN='\033[46m'
    LIGHTGREY='\033[47m'
    RESET='\033[49m'

class _Style(object):
    RESET='\033[0m'
    BLOD='\033[01m'
    DISABLE='\033[02m'
    UNDERLINE='\033[04m'
    REVERSE='\033[07m'
    STRIKETHROUGH='\033[09m'
    INVISIBLE='\033[08m'

Fore       = _Fore()
Style      = _Style()
Back       = _BackGround()

def _VERSION():
    print(Fore.RED + Style.UNDERLINE + Style.BLOD + Back.BLUE + '\t\t\t\t\t\tSos1ska' + Back.RESET + Style.RESET, Fore.RED + Style.UNDERLINE + Style.BLOD + 'my' + Fore.RESET + Style.RESET, Fore.GREEN + Style.BLOD + Style.UNDERLINE +  'creator' + Style.RESET)
Version = '0.0.1'
def VERSION():
    print('\t\t\t\t\t\t       '+Version), _VERSION()
def INFO():
    print()
    print()
    print()
    print("""Code Creator - https://vk.com/nikitasos1ska -- https://github.com/Sos1ska
VK Group - https://vk.com/spider_breaking
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Cool-Hackers - https://github.com/Cool-Hackers
Cool-Hackers: https://vk.com/nikitasos1ska -- https://github.com/Sos1ska,
              https://vk.com/2pac_jdm -- https://github.com/Ki11sesh,
              https://vk.com/covidone,
              https://vk.com/paket20
Technical support - https://vk.com/spider-breaking, soshack00@gmail.com""")
    print()
    print()
    print()