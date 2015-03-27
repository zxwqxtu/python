import socket

HOST = ''
PORT = 50009
BUFSIZE = 1023

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.send(raw_input('> '))
    data = s.recv(BUFSIZE)
    print 'Received', repr(data)
    s.close()
