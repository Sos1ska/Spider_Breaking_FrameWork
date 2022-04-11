import requests, bs4, json, datetime

class Version:
    version = "0.9"
    typeversion = "[ BETA ]"

def main():
    send_request = requests.get('https://raw.githubusercontent.com/Sos1ska/Spider_Breaking_FrameWork/sos-utils/S_B_FrameWork/version.json')
    soup = bs4.BeautifulSoup(send_request.text, 'html.parser').text
    site_json = json.loads(soup)
    Handler = site_json
    if int(Version.version) == int('%s' % (Hanlder["versionInt"]):
        print('[ root ] - [ INFO Not Found Update ] ' + str(datetime.datetime.now()) 
    if int(Version.version) not int('%s' % (Handler["versionInt"]):
        pass
