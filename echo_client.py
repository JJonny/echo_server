from socket import *


host = 'localhost'
port = 2222

message = str('close')

socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.connect((host, port))
socket_obj.send(message.encode(encoding='utf-8'))

data = socket_obj.recv(1024)

socket_obj.close()

