import sys
import time
import fritzbox
import threading

from configobj import ConfigObj

from library.loghandler import loghandler


class monitorDevice(threading.Thread):
    def __init__(self,configfile):
        threading.Thread.__init__(self)

        self._configfile = configfile
        self._log = None

        self._ibox = None

    def readConfig(self):
        print('READCONFIG',self._configfile)
        _cfg = ConfigObj(self._configfile)

        if bool(_cfg) is False:
            print('ERROR config file not found', self._configfile)
            sys.exit()

        self._cfg_log = _cfg.get('LOGGING', None)
        self._cfg_ibox = _cfg.get('INTERNET-BOX',None)
        self._cfg_devices = _cfg.get('DEVICES',None)
        return True

    def startLogger(self):
        self._log = loghandler()
        # print(self._cfg_log)
        self._log.handle(self._cfg_log.get('LOGMODE'), self._cfg_log)
        #       self._log.handle()
        self._log.level(self._cfg_log.get('LOGLEVEL', 'DEBUG'))
        return True

    def connect(self):
        _host = self._cfg_ibox.get('HOST','192.168.1.1')
        _user = self._cfg_ibox.get('USER','admin')
        _password = self._cfg_ibox.get('PASSWORD',None)

        self._fbox = fritzbox.Fritzbox()
        self._fbox.connect(_host,_user,_password)
        print('outgoing',self._fbox.outgoingCalls())

    def run(self):
        self.readConfig()
        self.startLogger()
        self.connect()
        self.monitor()

        #while True:
       #     self.monitor()
         #   time.sleep(5)

    def monitor(self):

        while True:
            print('active',self._fbox.currentActiveCalls())
            print('Outgoing', self._fbox.currentActiveOutgoingCalls())
            print('PM',self._fbox.getPM())
            time.sleep(10)


if __name__ == "__main__":
    mon = monitorDevice('./Callmonitor.cfg')
    mon.start()