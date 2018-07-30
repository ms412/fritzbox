import socket
import sys
import time

HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 1012  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# Start listening on socket
s.listen(10)
print('Socket now listening')

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print(    'Connected with ' + addr[0] + ':' + str(addr[1]))
    time.sleep(10)
    msg = '28.07.18 19:55:51;RING;0;0041795678728;+4984176290;POTS;\n'
  #  conn.sendall('28.07.18 19:55:51;RING;0;0041795678728;+4984176290;POTS;\n')
    conn.send(msg.encode())
    time.sleep(10)
    msg = '28.07.18 19:55:59;DISCONNECT;0;0;\n'
    conn.send(msg.encode())

s.close()