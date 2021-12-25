import socket,sys

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",10000)

client.connect(server_address)

message=input()
print("Sending",message)
client.sendall(message.encode())

data=client.recv(1000).decode()
print("ECHO:",data)
client.close()