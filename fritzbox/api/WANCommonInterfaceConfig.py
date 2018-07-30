
import fritzbox.base.fb_base as fb
from lxml import etree


class WANCommonInterfaceConfig(fb.fb_base):

    def __init__(self):
        print('WANCommonInterfaceConfig Create')

    def GetTotalBytesSent(self):
        value = self._session.call_action('WANCommonInterfaceConfig', 'GetTotalBytesSent')['NewTotalBytesSent']
        self._log.debug('GetTotalBytesSent %s' % value)
        return value

    def GetTotalBytesReceived(self):
        value = self._session.call_action('WANCommonInterfaceConfig', 'GetTotalBytesReceived')['NewTotalBytesReceived']
        self._log.debug('GetTotalBytesSent %s' % value)
        return value

    def GetTotalPacketsSent(self):
        value = self._session.call_action('WANCommonInterfaceConfig', 'GetTotalPacketsSent')['NewTotalPacketsSent']
        self._log.debug('GetTotalBytesSent %s' % value)
        return value

    def GetTotalPacketsReceived(self):
        value = self._session.call_action('WANCommonInterfaceConfig', 'GetTotalPacketsReceived')['NewTotalPacketsReceived']
        self._log.debug('GetTotalBytesSent %s' % value)
        return value