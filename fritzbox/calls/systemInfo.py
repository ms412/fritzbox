
import fritzbox.api.deviceinfoSCPD as deviceinfoSCPD
import json

class systemInfo(deviceinfoSCPD.deviceinfoSCPD):

    def ManufactorName(self):

        return self.getInfo
