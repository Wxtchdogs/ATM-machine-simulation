import socket
count = 0

#Server
s = socket.socket()
port = 1234
s.bind(('', port))    
s.listen(3)

while count > 4:
    c, addr = s.accept()
    c.close()
    count = count + 1

#Client
s = socket.socket()
hostName = socket.gethostname()
ip = socket.gethostbyname(hostName)
s.connect((ip, 1234))
s.revc()
s.close()
