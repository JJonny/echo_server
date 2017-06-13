from socket import *


host = '0.0.0.0'
port = 2222

socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.bind((host, port))
socket_obj.listen(10)

while True:
    connection, address = socket_obj.accept()
    print('Server connected by', address)

    while True:
        data = connection.recv(1024)
        if not data:
            break

        if data == b'close':
            print('connection close')
            connection.close()
            break

        print(data)
        connection.send(b'Echo=>' + data)
connection.close()
socket_obj.close()
print('socket closed')
