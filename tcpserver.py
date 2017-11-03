import socket

# creating a socket object
serverSocket = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# get local Host machine name

port = 9999

# bind to port
serverSocket.bind(('', port))

# Que up to 5 requests
serverSocket.listen(5)
print ('The server is ready to receive')
while True:
    # establish connection
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	print('the hostname received from client is',message.decode('utf-8'))
	errorMessage = 'nslook up failed'
	try:
		modifiedMessage = socket.gethostbyname(message)
		print('the ip address after nslook up is',modifiedMessage)
		connectionSocket.send(modifiedMessage.encode('utf-8'))
	except socket.error:
		connectionSocket.send(errorMessage.encode('utf-8'))
	finally:
		connectionSocket.close()