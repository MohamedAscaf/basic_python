import socket

s = socket.socket()
host = socket.gethostname()
print(host)
port = 45
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got Connecting From', addr)
    s1="Thank You For Connecting"
    c.send(s1.encode())
    c.close()
