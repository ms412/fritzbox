#!/usr/bin/env python3
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


__app__ = "fritzbox2mqtt Adapter"
__VERSION__ = "0.5"
__DATE__ = "19.07.2018"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2018 Markus Schiesser"
__license__ = 'GPL v3'

from configobj import ConfigObj
#import fritzconnection as fritzbox
import fritzconnection
# from library.sr04 import sr04
<<<<<<< HEAD
import logging
=======
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
import paho.mqtt.client as mqtt
import os
import time
import sys
import json
import fritzbox
<<<<<<< HEAD
import threading
=======
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b

# import io
# from library.configfile import configfile
# from library.mqttpush import mqttpush
from library.loghandler import loghandler

<<<<<<< HEAD
#logger = logging.getLogger()

class manager(threading.Thread):

    def __init__(self, configfile='fritzbox2mqtt.cfg'):
        threading.Thread.__init__(self)
=======

class manager(object):

    def __init__(self, configfile='fritzbox2mqtt.cfg'):
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        self._configfile = configfile

        self._general = None
        self._mqttbroker = None

        self._msg = {}

    def readConfig(self):
        #   _cfg = configfile(self._configfile)
        #  _config = _cfg.openfile()
        _config = ConfigObj(self._configfile)
<<<<<<< HEAD
    #    print(_config)
=======
        print(_config)
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        self._logcfg = _config.get('LOGGING', None)
        self._mqttCfg = _config.get('BROKER', None)
        self._fboxCfg = _config.get('FRITZBOX', None)
        return True

    def startLogger(self):
        print('logconfig',self._logcfg)
<<<<<<< HEAD
    #    logger = logging.getLogger()
     #   handler = logging.StreamHandler()
      #  formatter = logging.Formatter(
      #      '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
       # handler.setFormatter(formatter)
       # logger.addHandler(handler)
       # logger.setLevel(logging.DEBUG)

        #self._log = loghandler('FRITZBOX2MQTT')
        self._log = loghandler()
=======
        self._log = loghandler('FRITZBOX2MQTT')
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        self._log.handle(self._logcfg.get('LOGMODE'), self._logcfg)
        return True

    def startFritz(self):
        _host = self._fboxCfg.get('HOST', '192.168.1.1')
        _user = self._fboxCfg.get('USER', 'admin')
        _password = self._fboxCfg.get('PASSWORD', None)

        self._fbox = fritzbox.Fritzbox()
        self._fbox.connect(_host, _user, _password)
      #  print('outgoing', self._fbox.outgoingCalls())

    def getOutgoingCalls(self):
        _outgoing = json.loads(self._fbox.outgoingCalls())
       # print('outgoig Cals')
<<<<<<< HEAD
        self._log.debug('Outgoing calls %s'% _outgoing)
=======
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        return _outgoing

    def getMissedCalls(self):
        _missed = json.loads(self._fbox.missedCalls())
<<<<<<< HEAD
        self._log.debug('Missed calls %s'% _missed)
=======
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        return _missed

    def getIncommingCalls(self):
        _incomming = json.loads(self._fbox.incommingCalls())
<<<<<<< HEAD
        self._log.debug('Incomming calls %s'%  _incomming)
=======
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        return _incomming

    def getPM(self):
        _pm = json.loads(self._fbox.getPM())
<<<<<<< HEAD
        self._log.debug('PM data %s'% _pm)
        return _pm
    
    def systemInfo(self):
        return self._fbox.ManufactorName()

   # def curretnCall(self):

=======
        return _pm
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b


    def mqttPublish(self, topic, data):
        self._host = str(self._mqttCfg.get('HOST', 'localhost'))
        self._port = int(self._mqttCfg.get('PORT', 1883))
        main_channel = str(self._mqttCfg.get('PUBLISH', '/OPENHAB'))
        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

        #  self._mqttc = mqtt.Client()
<<<<<<< HEAD
        try:
            self._mqttc.connect(self._host, self._port, 60)
            deviceId = 'FRITZBOX'
            _topic = main_channel + '/' + deviceId + '/' + topic
            self._mqttc.publish(_topic, json.dumps(data))
            self._mqttc.loop(10)
            self._mqttc.disconnect()
            self._log.debug('message delivered to mqtt Server')
        except:
            self._log.error('Cannot deliver message to mqtt Server')

=======
        self._mqttc.connect(self._host, self._port, 60)

       # print('Data',data)
        deviceId = 'FRITZBOX'
      #  for item in data:
          #  _item = json.dumps(item)
         #   print(_item,type(_item),type(item))
        _topic = main_channel + '/' + deviceId + '/' + topic
        print(_topic, json.dumps(data))
        self._mqttc.publish(_topic, json.dumps(data))
        #    print('cc', _topic, _item)
        self._mqttc.loop(10)

        self._mqttc.disconnect()
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        return True

    def filterCalls(self,data):
        _list = []
<<<<<<< HEAD
      #  print('data',data)
=======
        print('data',data)
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
        for item in data:
            _templist = {}
          #  print('xxxxxxxxxxxx',item)
            _date = item.get('Date','')
            _name = item.get('Name','')
            if not _name:
                _name = 'Unknown'
            _duration = item.get('Duration','')
            _caller = item.get('Caller')

            #print('lll',_caller)
<<<<<<< HEAD
            if 'Anrufbeantworter' not in _name:
            #   print('block')
           # else:
=======
            if 'Anrufbeantworter' in _name:
                print('block')
            else:
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
                _templist['DATE']=_date
                _templist['DURATION']=_duration
                _templist['NAME']=_name
                _templist['CALLER'] =_caller

                _list.append(_templist)

      #  print(_list)

        return _list[:5]





<<<<<<< HEAD


=======
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
    def run(self):
        self.readConfig()
        self.startLogger()
        self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))

        self.startFritz()

        while(True):
            _out = self.getOutgoingCalls()
            _filter = self.filterCalls(_out)
<<<<<<< HEAD
         #   print('OUTGOING',_filter)
=======
            print('OUTGOING',_filter)
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
            self.mqttPublish('OUTGOING',_filter)

            _in = self.getIncommingCalls()
            _filter = self.filterCalls(_in)
<<<<<<< HEAD
          #  print('INCOMMING',_filter)
=======
            print('INCOMMING',_filter)
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
            self.mqttPublish('INCOMMING',_filter)

            _miss = self.getMissedCalls()
            _filter = self.filterCalls(_miss)
<<<<<<< HEAD
           # print('MISSED',_filter)
            self.mqttPublish('MISSED',_filter)

            _pm = self.getPM()
          #  print('PM',_pm)
            self.mqttPublish('PM',_pm)

           # print('next')
            print('ttttttttttttttttttttttt',self.systemInfo())
=======
            print('MISSED',_filter)
            self.mqttPublish('MISSED',_filter)

            _pm = self.getPM()
            print('PM',_pm)
            self.mqttPublish('PM',_pm)

            print('next')
>>>>>>> 84b190caa3ce80ee3a7cd07a9ad8cf2891e3854b
            time.sleep(30)
       # self._log.info('Startup, %s %s %s' % (__app__, __VERSION__, __DATE__))
        #  self._log.info('Start Reading Valuse')
       # data = self.startMeasure()
       # print('DAten', data)
      #  self._log.info(data)
        #  self.publishData(data)
      #  self.mqttPublish(data)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        configfile = sys.argv[1]
    else:
        configfile = './fritzbox2mqtt.cfg'

    mgr_handle = manager(configfile)
    mgr_handle.run()
