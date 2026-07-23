import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen(1)

print("Server started...")
print("Waiting for log data...")

connection, address = server.accept()

print("Connected:", address)

data = connection.recv(1024).decode()

print("Received Log:")
print(data)

connection.close()

server.close()