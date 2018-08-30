
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

    def X_AVM_DE_GetOnlineMonitor(self,_if):
      #  print(self._session.get_action_arguments('WANCommonInterfaceConfig:1', 'X_AVM-DE_GetOnlineMonitor'))
        value = self._session.call_action('WANCommonInterfaceConfig', 'X_AVM-DE_GetOnlineMonitor', NewSyncGroupIndex=_if)
        self._log.debug('X_AVM-DE_GetOnlineMonitor %s' % value)
        return value

    def GetCommonLinkProperties(self):
        value = self._session.call_action('WANCommonInterfaceConfig', 'GetCommonLinkProperties')
        self._log.debug('GetCommonLinkProperties  %s' % value)
        return value
