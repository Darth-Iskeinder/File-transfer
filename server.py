import socket

s = socket.socket()
host = socket.gethostname()
port = 9090
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for connection...")
conn, addr = s.accept()
print(addr, "Has connecteb")

filename = input(str("Enter the filename of the file: "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data transmitted succesfully")
