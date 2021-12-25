import socket,sys

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",10000)
server.bind(server_address)
server.listen(1)
print("Waiting for connection")
connection,client_address=server.accept()

print("Connection eatablished",client_address)
data=connection.recv(1000)
print("Received:",data)
connection.sendall(data)

connection.close()
server.close()