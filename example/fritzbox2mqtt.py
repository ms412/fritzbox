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

import fritzbox
import threading
import time
import json
import os
import sys
import logging
from configobj import ConfigObj
import paho.mqtt.client as mqtt
from library.loghandler import loghandler



class Fritzmonitor(threading.Thread):

    def __init__(self, configfile):
        threading.Thread.__init__(self)

        self._configfile = configfile

     #   self._log = logging.getLogger('fritzbox')
      #  fh = logging.FileHandler('/home/tgdscm41/fritzbox/Fritzmonitor.log')
       # fh.setLevel(logging.DEBUG)
        #self._log.addHandler(fh)

        self._fritz = None

    def readConfig(self):
        #   print('READCONFIG',self._configfile)
        _cfg = ConfigObj(self._configfile)

        if bool(_cfg) is False:
            print('ERROR config file not found', self._configfile)
            sys.exit()

        self._cfg_log = _cfg.get('LOGGING', None)
        self._cfg_ibox = _cfg.get('FRITZBOX', None)
        self._mqttCfg = _cfg.get('BROKER', None)
        # self._cfg_devices = _cfg.get('DEVICES',None)
        return True

    def startLogger(self):
     #   print('STart Logger')
       # self._log = logging.getLogger(__name__)
        #fh = logging.FileHandler('/home/tgdscm41/fritzbox/Fritzmonitor.log')
        #fh.setLevel(logging.DEBUG)
        #self._log.addHandler(fh)
      #  print(self._cfg_log)
        _mode = self._cfg_log.get('LOGMODE','PRINT')
        self._log = loghandler()
        self._log.handle(method=_mode,config=self._cfg_log)
        return True

    def startTR64(self):
        _host = self._cfg_ibox.get('HOST', '192.168.1.1')
        _user = self._cfg_ibox.get('USER', 'ms412')
        _password = self._cfg_ibox.get('PASSWORD', 'Swisscom10')

        self._fbox = fritzbox.Fritzbox()
        if not self._fbox.connect(_host, _user, _password):
            self._log.error('Failed to Connect to Fritzbox %s' % _host)
            return False

        return True

    def startCallMonitor(self):
        _host = self._cfg_ibox.get('HOST', '192.168.1.1')
        # _host = 'localhost'
        if self._fbox.cm_connect(_host):
            self._log.debug('Connected to CallMonitor with success')
            self._fbox.register_callback(self.callEvent)
        else:
            self._log.error('Failed to Connect to Fritzbox CallMonitor Interface Host: %s' % _host)
            return False

        return True

    def callEvent(self, msg):
        #  print('callback',msg)
        _from = msg.get('FROM', 0)
        # print(_from)
        _name, _id = self._fbox.LookupName(_from)
        self._log.debug('Query Name from %s; Name found %s' % (_from, _name))
        # print('Name',self._fbox.LookupName(_from))
        msg['NAME'] = _name
        msg['ID'] = _id
        self.mqttPublish('CALLMONITOR', msg)
        return _name

    #  def getPhonebook(self):
    #     _host =  '192.168.1.1'
    #    _user = 'tgdscm41'
    #   _password = 'nd%aG9im'

    #  self._fbox = fritzbox.Fritzbox()
    # self._fbox.connect(_host, _user, _password)

    #  self._fbox.GetPhoneBook()
    #    (name,number) = self._fbox.LookupName('841953200')
    #   print('Name: %s; Number: %s'%(name,number))
    #  self._fbox.cm_connect('localhost')
    # self._fbox.register_callback(self.callEvent)

    def getPM(self):
        return self._fbox.getPM()

    def getCallerList(self):
        _temp = {}
        _incomming = self._fbox.incommingCalls()
        _missed = self._fbox.missedCalls()
        _outgoing = self._fbox.outgoingCalls()
        #   print('Outgoing',_outgoing)
        _temp['INCOMMING'] = json.loads(_incomming)
        _temp['OUTGOING'] = json.loads(_outgoing)
        _temp['MISSED'] = json.loads(_missed)

        self._log.debug('getCallerList %s' % (_temp))

        return _temp

    def callFilter(self, data):
        _list = []

        for item in data:
            #  print('xxx',item)
            _templist = {}
            #  print('xxxxxxxxxxxx',item)
            _date = item.get('Date', '')
            _name = item.get('Name', '')
            if not _name:
                _name = 'Unknown'
            _duration = item.get('Duration', '')
            _caller = item.get('Caller')
            _to = item.get('Called')

            if 'Anrufbeantworter' not in _name:
                #       print('block')
                #  else:
                _templist['DATE'] = _date
                _templist['DURATION'] = _duration
                _templist['NAME'] = _name
                _templist['CALLER'] = _caller
                _templist['TO'] = _to

                _list.append(_templist)

        return _list[:5]

    def mqttPublish(self, topic, data):
        _host = str(self._mqttCfg.get('HOST', 'localhost'))
        _port = int(self._mqttCfg.get('PORT', 1883))
        _channel = str(self._mqttCfg.get('PUBLISH', 'OPENHAB'))
        _deviceId = str(self._mqttCfg.get('DEVICE', 'FRITZBOX'))
        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

        #   try:
        self._mqttc.connect(_host, _port, 60)
        _topic = '/' + _channel + '/' + _deviceId + '/' + topic
        self._mqttc.publish(_topic, json.dumps(data))
        #    print(_topic, json.dumps(data))
        self._mqttc.loop(10)
        self._mqttc.disconnect()
        self._log.debug('message delivered to mqtt Server: %s; Topic: %s; Message: %s' % (_host, _topic, data))
        #  except:
        #     self._log.error('Cannot deliver message to mqtt Server')

        return True

    def run(self):
        # print('START')
        self.readConfig()
        self.startLogger()
        self._log.info('Fritzbox Call Monitor')
        while not self.startTR64():
        #    print('X')
            self._log.debug('Failed to connect to Fritzbox, try again in 10 sec')
            time.sleep(10)


     #   print('TEST')
        time.sleep(10)
        self.startCallMonitor()
        time.sleep(10)

        _saveTime = time.time() + 1
        #    print(_saveTime)
        #    while True:

        while True:
            if not self._fbox.isconnected():
                self._log.error('Lost Connection to fritzbox')
                self.startTR64()
                time.sleep(10)
                self.startCallMonitor()
                time.sleep(10)


            if _saveTime < time.time():
                _saveTime = time.time() + 300
                _result = self.getCallerList()
                for key, item in _result.items():
                    self.mqttPublish(key, self.callFilter(item))

                self.mqttPublish('PM', self.getPM())

            time.sleep(1)


if __name__ == '__main__':
    if len (sys.argv) > 1:
        _configfile = sys.argv[1]

    else:
        _configfile = './fritzbox2mqtt.cfg'
    print(_configfile)
    fZm = Fritzmonitor(_configfile)
   # fZm = Fritzmonitor('/home/tgdscm41/fritzbox/Fritzmonitor.cfg')
    fZm.run()
