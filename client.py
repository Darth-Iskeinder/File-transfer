import socket
s = socket.socket()
host = input(str("Enter the host address of the sender: "))
port = 9090
s.connect((host,port))
print("Connected...")

filename = input(str("Enter a filename for the incoming file: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File received succesfully.")
