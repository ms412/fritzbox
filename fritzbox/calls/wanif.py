import fritzbox.api.WANCommonInterfaceConfig as WANCommonInterfaceConfig
import fritzbox.api.WANDSLInterfaceConfig as WANDSLInterfaceConfig
import json

class wanif(WANCommonInterfaceConfig.WANCommonInterfaceConfig,WANDSLInterfaceConfig.WANDSLInterfaceConfig):

    def getPM(self):
        _value= {}
        _value['RX_BYTE']=self.GetTotalBytesReceived()
        _value['TX_BYTE']=self.GetTotalBytesSent()
        _value['RX_PACKETS']=self.GetTotalPacketsReceived()
        _value['TX_PACKETS']=self.GetTotalPacketsSent()

      #  return json.dumps(_value)
        return _value

    def onlineMonitor(self,_if):
        return json.dumps(self.X_AVM_DE_GetOnlineMonitor(_if))

    def linkPerformance(self):
        return self.GetCommonLinkProperties()

    def accessType(self):
        return self.GetCommonLinkProperties()['NewWANAccessType']

    def GetInfo(self):
        return self.GetDSLInfo()

    def GetStatisticsTotalDSL(self):
        print(self.GetStatisticsTotal())