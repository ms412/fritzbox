import fritzbox.base.fb_callmonitor as fb
import time
import datetime


class callmonitor(fb.fb_callmonitor):

     def parser(self,line):
        line = line.split(";")
        timestamp = time.mktime(datetime.datetime.strptime((line[0]), "%d.%m.%y %H:%M:%S").timetuple())
        if (line[1] == "RING"):
            self._log.debug('Ring %s'%line)
            self.call_handler({"type": "incoming", "from": line[3], "to": line[4], "device": line[5],"initiated": timestamp, "accepted": None, "closed": None})
        #    self.call_callback(int(line[2]), "incoming", self.call_handler[int(line[2])])
        elif (line[1] == "CALL"):
            self._log.debug('Call', line)
            self.call_handler[int(line[2])] = {"type": "outgoing", "from": line[4], "to": line[5], "device": line[6],
                                               "initiated": timestamp, "accepted": None, "closed": None}
         #   self.call_callback(int(line[2]), "outgoing", self.call_handler[int(line[2])])
        elif (line[1] == "CONNECT"):
            self._log.debug('Connect', line)
            self.call_handler[int(line[2])]["accepted"] = timestamp
          #  self.call_callback(int(line[2]), "accepted", self.call_handler[int(line[2])])
        elif (line[1] == "DISCONNECT"):
            self._log.debug('Disconnect %s'% line)
            self.call_handler(timestamp)
           # self.call_callback(int(line[2]), "closed", self.call_handler[int(line[2])])


