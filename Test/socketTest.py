import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "127.0.0.1"
port = 80

s.connect((host_ip, port))
s.sendall(b"Hello!")