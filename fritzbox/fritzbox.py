
import logging
from logging import NullHandler

from fritzbox.calls.callhistory import callhistory
from fritzbox.calls.wanif import wanif
from fritzbox.calls.systemInfo import systemInfo
from fritzbox.calls.callmonitor import callmonitor
from fritzbox.calls.phonebook import phonebook


logging.getLogger(__name__).addHandler(NullHandler())

class Fritzbox(callhistory,
               callmonitor,
               wanif,
               systemInfo,
               phonebook):

    def __init__(self):
      #  print('Create Fritzbox Object 123')
        self._log = logging.getLogger('fritzbox')




       # self._log.debug('Create boxmgr object')


    pass