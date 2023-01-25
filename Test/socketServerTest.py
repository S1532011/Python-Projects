# import socket

# HOST = "127.0.0.1"
# PORT = 65432

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen()
# conn, addr = s.accept()
# data = conn.recv(1024)
# conn.sendall(data)


# import the socketserver module of Python

import socketserver

class MyTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("Recieved one request from {}".format(self.client_address[0]))
        msg = self.rfile.readline().strip()
        print("Data Recieved from client is:".format(msg))
        print(msg)  
        self.wfile.write("Hello Client....Got your message".encode())
aServer = socketserver.TCPServer(("127.0.0.1", 65432), MyTCPRequestHandler)
aServer.serve_forever()