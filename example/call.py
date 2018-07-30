#############################################################################
#                             py-fritz-monitor                              #
#                               Version 1.0.1                               #
#                                                                           #
# The folowing code is written in Python 3                                  #
# It uses port 1012 of fritzbox routers to read incoming and outgoing calls #
# The feature which is used is called call monitor                          #
# If the connection does not work, please read the readme file              #
# Original work by http://www.blog.smartnoob.de                             #
# If you find bugs or you have any question, please inform me via GitHub    #
# https://github.com/HcDevel/py-fritz-monitor                               #
#############################################################################

import socket
import threading
import time
import datetime


class callmonitor:
    def __init__(self, hostname="fritz.box", port=1012):
        self.hostname = hostname
        self.port = port
        self.connection = None
        self.call_handler = {}
        self.callback = None

    def register_callback(self, function_name=-1):
        if (function_name != -1):
            self.callback = function_name
        else:
            self.callback = None

    def call_callback(self, id, action, details):
        print(self.callback,id,action,details)
        if (self.callback != None):
            self.callback(id, action, details)

    def connect(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connection.connect((self.hostname, self.port))
            print("Success connecting to", self.hostname, "on port:", str(self.port))
            threading.Thread(target=self.listen).start()
            print("Listening for calls")

        except socket.error as e:
            self.connection = None
            print("Cannot connect to", self.hostname, "on port:", str(self.port), "\nError:", e)

    def disconnect(self):
        self.listen_running = False
        self.connection.shutdown(2)

    def listen(self, recv_buffer=4096):
        self.listen_running = True
        buffer = ""
        data = True
        while (self.listen_running == True):
            data = self.connection.recv(recv_buffer)
            buffer += data.decode("utf-8")

            while buffer.find("\n") != -1:
                line, buffer = buffer.split("\n", 1)
                self.parse(line)

            time.sleep(1)
        return

    def parse(self, line):
        line = line.split(";")
        timestamp = time.mktime(datetime.datetime.strptime((line[0]), "%d.%m.%y %H:%M:%S").timetuple())
        if (line[1] == "RING"):
            self.call_handler[int(line[2])] = {"type": "incoming", "from": line[3], "to": line[4], "device": line[5], "initiated": timestamp, "accepted": None, "closed": None}
            self.call_callback(int(line[2]), "incoming", self.call_handler[int(line[2])])
        elif (line[1] == "CALL"):
            self.call_handler[int(line[2])] = {"type": "outgoing", "from": line[4], "to": line[5], "device": line[6],"initiated": timestamp, "accepted": None, "closed": None}
            self.call_callback(int(line[2]), "outgoing", self.call_handler[int(line[2])])
        elif (line[1] == "CONNECT"):
            self.call_handler[int(line[2])]["accepted"] = timestamp
            self.call_callback(int(line[2]), "accepted", self.call_handler[int(line[2])])
        elif (line[1] == "DISCONNECT"):
            self.call_handler[int(line[2])]["closed"] = timestamp
            self.call_callback(int(line[2]), "closed", self.call_handler[int(line[2])])




#if __name__ == "__main__":

def my_cb( id, action, details):
    print("Call: " + str(id) + " - " + action)
    print(details)


call = callmonitor(hostname='192.168.1.1')
            # Create new instance of py-fritz-monitor, Optinal parameters: host, port
print(my_cb)
call.register_callback(my_cb)  # Defines a function which is called if any change is detected, unset with call.register_callback (-1)
call.connect()

# Some examples, remove in productive usage!
call.parse("09.03.14 21:51:56;CALL;0;12;453423;04829401845;SIP0;")  # Simulates outgoing call
call.parse("09.03.14 18:20:59;RING;0;04829401845;453423;SIP0;")  # Simmulates incoming call (choose between CALL and RING!)
call.parse("09.03.14 21:52:06;CONNECT;0;12;04829401845;")  # Simulates an accepted call
call.parse("09.03.14 21:52:06;DISCONNECT;0;12;04829401845;")  # Simulates an ended call

# Please note: Phone numbers are fictional. Don't call them!

input("Press key to exit\n")
call.disconnect()