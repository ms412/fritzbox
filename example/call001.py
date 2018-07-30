
import fritzbox
from library.loghandler import loghandler

class calltest(object):

    def logger(self):
        self._log = loghandler()
        self._log.handle('PRINT')
        return True

    def getPhonebook(self):
        _host =  '192.168.1.1'
        _user = 'tgdscm41'
        _password = 'nd%aG9im'

        self._fbox = fritzbox.Fritzbox()
        self._fbox.connect(_host, _user, _password)
        self._fbox.GetPhoneBook()
        (name,number) = self._fbox.LookupName('841953200')
        print('Name: %s; Number: %s'%(name,number))


    def run(self):
        fb = fritzbox.Fritzbox()
      #  fb.getPhoneBook()
        fb.cm_connect('localhost')
       # print('ff',self.jumpin)

        fb.register_callback(self.jumpin)

    def jumpin(self):
        pass
        return

if __name__ == '__main__':
    ct = calltest()
    ct.logger()
    ct.getPhonebook()
 #   ct.run()