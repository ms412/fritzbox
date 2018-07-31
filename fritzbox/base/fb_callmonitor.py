
__app__ = "fritzbox api"
__VERSION__ = "0.5"
__DATE__ = "21.07.2018"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2018 Markus Schiesser"
__license__ = 'GPL v3'

import fritzconnection
import logging
import socket
import threading
import time


class fb_callmonitor(object):

    def __init_(self):

        self._connection = None
        self.call_handler = {}
        self._callback = None

    def register_callback(self, callback = False):
        if(callback != False):
            self._callback = callback
        else:
            self._callback = None

    def cm_connect(self,host):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connection.connect((host, 1012))
            self._log.debug('Scucess connecting to %s at port %s'%(host,'1012'))
            threading.Thread(target=self.listen).start()
            self._log.debug("Listening for calls")
          #  print('OK')

        except socket.error as e:
            self.connection = None
            self._log.error('Cannot connect to %s at port %s'%(host,'1012'))
            return False
           # print('NOK')
        return True

    def reconnect(self):
        time.sleep(10)
        self._log.debug("Reconnect to Server")
        self.cm_connect('localhost')
        return True


    def disconnect(self):
        self.listen_running = False
        self._log.info('Disconnect from Fritzbox')
        self.connection.shutdown(2)
        return True


    def listen(self, recv_buffer=4096):
        self.listen_running = True
        buffer = ""
        data = True
        try:
          #  print('connect')
            self._log.info('Connected to Fritzbox Callmonitor')
            while (self.listen_running == True):
                data = self.connection.recv(recv_buffer)
                buffer += data.decode("utf-8")

                while buffer.find("\n") != -1:
                    line, buffer = buffer.split("\n", 1)
                    self._log.debug('Received data %s'% line)
                    self.parser(line)

                time.sleep(1)
        except:
            self._log.error('Lost Communication to Call Monitor Server')
            self.listen_running = False
            self.disconnect()
            self.reconnect()
        return

