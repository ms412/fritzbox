import fritzbox.api.callmonitor as callmonitor
import json

class callmonitor(callmonitor.callmonitor):

    def __init__(self):
        print('Callmonitor Object')
        self._callback = None

    def register_callback(self, callback = None):
        print('e',callback)
        if (callback == None):
            print('Not register')
        else:
            print('Register')
            self._callback = callback
        print(self._callback)

    def call_handler(self,a):
        print('test',a)

