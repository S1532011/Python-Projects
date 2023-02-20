import socket

HOST = "127.0.0.1"
PORT = 80
NOTFOUND = "404"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    print(data)
    fileName = data.split()[1]
    if(fileName == "/"):
        fileName = "/index.html"
    try:
        file = open("Test/pyWebTest" + str(fileName), "r")
        fileData = file.read()
        conn.sendall(fileData.encode())
        print(fileData)
    except FileNotFoundError:
        conn.sendall(NOTFOUND.encode())
        print(NOTFOUND)
    s.close()