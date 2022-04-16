# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
def FORM_CREATE_SH_TOAST(msg):
    Create_Form = f'termux-toast \'{msg}\''
    return Create_Form
def FORM_CREATE_SH_NOTIFICATION(msg):
    Create_Form = f'termux-notification --action \'{msg}\''
    return Create_Form