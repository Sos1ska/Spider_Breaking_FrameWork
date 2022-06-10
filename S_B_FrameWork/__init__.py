from .services import Main as Main_S_B_FrameWork
from .services import MainUnionCode
from .services import _debug_ as debug
from .services import _error_ as error
from .services import _info_ as info
from .services import _warning_ as warning
from .services.Notification.Windows.CreateNotification import (
    MainCode_CreaterNotificationForWindows, vbAbortRetryIgnore,
    vbApplicationModal, vbCritical, vbDefaultButton1, vbDefaultButton2,
    vbDefaultButton3, vbDefaultButton4, vbExclamation, vbInformation,
    vbMsgBoxHelpButton, vbMsgBoxRight, vbMsgBoxRtlReading,
    vbMsgBoxSetForeground, vbOKCancel, vbOKOnly, vbQuestion, vbRetryCancel,
    vbSystemModal, vbYesNo, vbYesNoCancel)
from .services.Notification.Windows.CreateNotification import MainCode_CreaterNotificationForWindows as NotificationWindows
from .services.Notification.Termux.CreateNotification import MainCode_CreaterNotificationForTermux as NotificationTermux
from .services import Main_One_Dot_Zero as Main_S_B_FrameWorkNew_ONE_DOT_ZERO
