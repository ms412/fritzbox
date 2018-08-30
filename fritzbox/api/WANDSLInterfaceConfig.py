
import fritzbox.base.fb_base as fb
from lxml import etree


class WANDSLInterfaceConfig(fb.fb_base):

    def GetDSLInfo(self):
        value = self._session.call_action('WANDSLInterfaceConfig', 'GetInfo')
        self._log.debug('GetInfo %s' % value)
        return value

    def GetStatisticsTotal(self):
        value = self._session.call_action('WANDSLInterfaceConfig', 'GetStatisticsTotal')
        self._log.debug('GetStatisticsTotal %s' % value)
        return value
