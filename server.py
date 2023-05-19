from socket import*
serverport=12000
ss=socket(AF_INET,SOCK_DGRAM)
ss.bind(('',serverport))
print('ready')
while True:
    q,add=ss.recvfrom(2048)
    a=q.decode().upper()
    ss.sendto(a.encode(),add)
    

wejgf
