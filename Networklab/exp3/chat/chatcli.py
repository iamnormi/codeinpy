import socket,sys

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',11000)
client.connect(server_address)
print("conecting to port",server_address)
message=input()
client.sendall(message.encode())
while message!='end':
    data=client.recv(1000).decode()
    if data:
        print("From server:",data)
        message=input()
        client.sendall(message.encode())
    else:
        break
client.close()