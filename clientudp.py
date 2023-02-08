from socket import*
servername='127.0.0.1'
serverport=12000
server=socket(AF_INET,SOCK_DGRAM)
n=input()
server.sendto(n.encode(),(servername,serverport))
r,add=server.recvfrom(2048)
print(r.decode())
server.close()


