import socket
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print('the hostname received from client is',message.decode('utf-8'))
	errorMessage = 'nslook up failed'
	try:
		modifiedMessage = socket.gethostbyname(message)
		print('ip address after nslookup',modifiedMessage)
		serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
	except socket.error:
		serverSocket.sendto(errorMessage.encode('utf-8'), clientAddress)
	