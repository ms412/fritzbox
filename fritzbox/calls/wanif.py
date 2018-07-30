import fritzbox.api.WANCommonInterfaceConfig as WANCommonInterfaceConfig
import json

class wanif(WANCommonInterfaceConfig.WANCommonInterfaceConfig):

    def getPM(self):
        _value= {}
        _value['RX_BYTE']=self.GetTotalBytesReceived()
        _value['TX_BYTE']=self.GetTotalBytesSent()
        _value['RX_PACKETS']=self.GetTotalPacketsReceived()
        _value['TX_PACKETS']=self.GetTotalPacketsSent()

        return json.dumps(_value)

