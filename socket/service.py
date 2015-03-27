import socket

HOST = ''
PORT = 50009
BUFSIZE = 1023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(0)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFSIZE)
    print 'Connected by', addr, data
    if not data:
        break
    conn.sendall('Serivce '+ data)
conn.close()

