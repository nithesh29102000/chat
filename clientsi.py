from socket import*
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort)) 
p = input("Enter number: ")
n = input("Enter number: ")
r = input("Enter number: ")
clientSocket.send(p.encode())
clientSocket.send(n.encode())
clientSocket.send(r.encode()) 
modifiedSentence = clientSocket.recv(1024) 

print ('From Server:', modifiedSentence.decode())
clientSocket.close()


