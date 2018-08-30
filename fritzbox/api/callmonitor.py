import fritzbox.base.fb_callmonitor as fb
import time
import datetime


class callmonitor(fb.fb_callmonitor):

     def parser(self,line):
        line = line.split(";")
        timestamp = time.mktime(datetime.datetime.strptime((line[0]), "%d.%m.%y %H:%M:%S").timetuple())
        if (line[1] == "RING"):
            self._log.debug('Ring %s'%line)
            self.call_handler({"TYPE": "RING", "FROM": line[3], "TO": line[4], "DEVICE": line[5],"DATE": timestamp})
        elif (line[1] == "CALL"):
            self._log.debug('Call %s'% line)
            self.call_handler({"TYPE": "OUTGOING", "FROM": line[4], "TO": line[5], "DEVICE": line[6],"DATE": timestamp})
        elif (line[1] == "CONNECT"):
            self._log.debug('Connect %s'% line)
            self.call_handler({"TYPE": "CONNECT", "FROM": line[4],"DATE": timestamp})
        elif (line[1] == "DISCONNECT"):
      #  else:
            self._log.debug('Disconnect %s'% line)
            self.call_handler({"TYPE": "DISCONNECT", "FROM": line[4],"DATE": timestamp})
        else:
            self._log.error('Unknown Message type %s'% line)



