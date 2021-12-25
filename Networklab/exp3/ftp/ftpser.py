import socket,sys

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',11000)
server.bind(server_address)
server.listen(1)
connection,client_address=server.accept()
file_name="sample.txt"
connection.sendall(file_name.encode())
file=open("sample.txt","rb")
data=file.read()
connection.sendall(data)
file.close()
connection.close()
server.close()
