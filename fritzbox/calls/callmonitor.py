import fritzbox.api.callmonitor as callmonitor
import json

class callmonitor(callmonitor.callmonitor):

  #  def __init__(self):
   #     print('Callmonitor Object')
     #    self._callback = None

    def register_callback(self, callback = None):
       # print('e',callback)
        if (callback == None):
        #    print('Not register')
            self._log.error('Failed to resiger Callback handler %s' % callback)
        else:
            self._log.debug('Registered Callback handler for call notifications %s' % callback)
            self._callback = callback
     #   print(self._callback)

    def call_handler(self,notification):
      #  print('test',a)
        self._log.debug('Received call Notification %s'% notification)
        self._callback(notification)

