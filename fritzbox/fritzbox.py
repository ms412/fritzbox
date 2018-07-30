import logging

from fritzbox.calls.caller import caller
#from fritzbox.calls.callmonitor import callmonitor
from fritzbox.calls.wanif import wanif
from fritzbox.calls.systemInfo import systemInfo
from fritzbox.calls.cm import callmonitor
from fritzbox.calls.phonebook import phonebook



class Fritzbox(caller,
               callmonitor,
               wanif,
               systemInfo,
               phonebook):

    def __init__(self):
        print('Create Fritzbox Object 123')
        self._log = logging.getLogger('fritzbox')
        self._log.debug('Create boxmgr object')


    pass