import socket
import time

HOST = ''
PORT = 21507
BUFSIZE = 1024
udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind((HOST, PORT))

while True:
    print 'waiting from message...'
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[%s] %s' %(time.ctime(), data), addr)
    print '...received from and returned to:', addr

udpSerSock.close()

