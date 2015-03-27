import socket

HOST = 'www.xrschzs.com'
PORT = 21507
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data: break
    
    s.sendto(data, (HOST, PORT))
    data, addr = s.recvfrom(BUFSIZE)
    if not data: break
    print data

s.close()

    

