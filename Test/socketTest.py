import socket


HOST = "127.0.0.1"
IP = "192.168.1.36"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

# s.bind((IP, PORT))
# print("port bound")
# s.listen()
# print("listening for connection...")
# conn, addr = s.accept()
# print("Connected established from: {addr}")
# data = conn.recv(1024)
# print("data recieved, sending data back...")
# conn.sendall(data)

s.connect((IP, PORT))
data = s.recv()
print(data)
s.sendall(data)