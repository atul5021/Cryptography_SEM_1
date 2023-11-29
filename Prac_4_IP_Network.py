### Server 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP/IP

host = '127.0.0.1'  # localhost
port = 4556  # 65,535

s.bind((host,port))
s.listen(1)

c,addr = s.accept()
print("Connected with",addr)

while True:
    msg = input("Send message to client : ")
    c.send(msg.encode())
    print("== Waiting for response ==")
    c_msg=c.recv(1024)   # c_msg is client message
    print("Message from CLIENT :", c_msg.decode())



### Client 


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 4556

s.connect((host,port))

while True:
    print("== Waiting for response ==")
    s_msg=s.recv(1024) # s_msg server message
    print("Message from server : ",s_msg.decode())
    c_msg = input("Send message to SERVER : ")
    s.send(c_msg.encode())

