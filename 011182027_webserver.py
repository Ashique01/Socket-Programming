# import socket module
from socket import *
from datetime import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverHost = "localhost"
serverPort = 8484
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)

while True:

    print("\nReady to serve...\n")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(4096)
        print(message.decode("utf-8"))
        if not message:
            continue
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        requestTime = datetime.now().strftime("%Y-%m-%d %H:%M")
        responseHeader = "HTTP/1.1 200 OK"
        header = {
            "Date": requestTime,
            "Content-Length": len(outputdata.encode("utf-8")),
            "Content-Type": "mytext.txt; charset=utf-8",
        }
        httpHeader = "\r\n".join(f"{head}:{header[head]}" for head in header)
        responseMessage = f"{responseHeader}\r\n{httpHeader}\r\n\r\n"
        connectionSocket.send(responseMessage.encode("utf-8"))
        print(responseMessage)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode("utf-8"))
        connectionSocket.close()
    except IOError:

        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: mytext.txt\r\n\r\n<!DOCTYPE html><html><body><h1>404 Not Found<h1></body></html>") # response header + error html page
        print("HTTP/1.1 404 Not Found\r\nContent-Type: mytext.txt\r\n\r\n<!DOCTYPE html><html><body><h1>404 Not Found<h1></body></html>")
        connectionSocket.close()
serverSocket.close()