import socket

s = socket.socket()
host = socket.gethostname()
port = 45

s.connect((host, port))
a=s.recv(1024)
print(a.decode()+" I Am A Client One")
s.close()
