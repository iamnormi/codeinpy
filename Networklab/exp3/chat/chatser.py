import socket,sys

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',11000)
server.bind(server_address)
server.listen(1)
print("Waiting for a connection")
connection,client_address=server.accept()
print("Connection establised with",client_address)
message=""
while message!="end":
    data=connection.recv(1000).decode()
    if data:
        print("From client:",data)
        message=input()
        connection.sendall(message.encode())
    else:
        break
connection.close()
server.close()