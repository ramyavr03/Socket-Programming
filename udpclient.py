import socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'abcdef' #python 3 supports byte values hence b
print('the hostname:',message)
clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('ipaddress',modifiedMessage.decode('utf-8'))
clientSocket.close()