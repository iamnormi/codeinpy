import socket

table={'192.165.1.1':'1E.4A.4A.11',
'192.165.2.1':'5E.51.4B.01',
'192.165.1.3':'4B.35.CD.32',
'192.165.4.1':'AF.4D.1F.FF',
'192.165.3.2':'C3.C5.EE.C2',
'1E.4A.4A.11':'192.165.1.1',
'5E.51.4B.01':'192.165.2.1',
'4B.35.CD.32':'192.165.1.3',
'AF.4D.1F.FF':'192.165.4.1',
'C3.C5.EE.C2':'192.165.3.2'
}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen()
clientsocket, address=s.accept()
print("Connection From",address,"Has Established")
ip=clientsocket.recv(1024)
ip=ip.decode('utf-8')
mac=table.get(ip,'No entry for given address')
clientsocket.send(mac.encode())