import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

log_message = "INFO User logged into the system"

client.send(log_message.encode())

print("Log sent successfully")

client.close()