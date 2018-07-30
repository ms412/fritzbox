
import fritzbox.base.fb_base as fb
from lxml import etree


class deviceinfoSCPD(fb.fb_base):

    #def __init__(self):
      #  print('WANCommonInterfaceConfig Create')

    def getInfo(self):
        value = self._session.call_action('deviceinfoSCPD', 'GetInfo') ['NewManufacturerName']
        self._log.debug('GetInfo %s' % value)
        print(value)
        return value

