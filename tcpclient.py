import socket
# creates socket object
clientSocket = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
host = 'localhost' 
port = 9999
clientSocket.connect((host, port))
message='fhjhkj' #python 3 supports byte values hence b
print('the hostname:',message)
clientSocket.send(message.encode('utf-8'))
modifiedMessage = clientSocket.recv(1024) # msg can only be 1024 bytes long
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
