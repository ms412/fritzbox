

__app__ = "fritzbox api"
__VERSION__ = "0.5"
__DATE__ = "21.07.2018"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"
__copyright__ = "Copyright (C) 2018 Markus Schiesser"
__license__ = 'GPL v3'

import fritzconnection
import logging



class fb_base(object):

    def __init_(self):

        self._log.debug('Create Fritzbox Object')
        self._session = None
      #  self._phonebook = {}


    def connect(self,host, user, passwd):

        self._session = fritzconnection.FritzConnection(address=host, port=49000, user=user, password=passwd)
        print(self._session.call_action('WANCommonInterfaceConfig', 'GetTotalBytesSent')['NewTotalBytesSent'])
        if not self._session.modelname:
            self._log.error('Cannot connect to Fritzbox')
            return None
        self._log.info('Connect to %s' % self._session.modelname)

        return self._session.modelname

