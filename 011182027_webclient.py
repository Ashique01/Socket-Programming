from socket import *

serverHost = "localhost"
serverPort = 8484
filename = "mytex.txt"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))
header = {
    "first_header": f"GET /{filename} HTTP/1.1",
    "Host": f"{serverHost}:{serverPort}",
    "Accept": "mytext.txt",
    "Accept-Language": "en-us",
}
httpHeader = "\r\n".join(f"{head}:{header[head]}" for head in header)
requestMessage = f"{httpHeader}\r\n\r\n"
clientSocket.send(requestMessage.encode("utf-8"))
print("request:\n", requestMessage)

result = ""
responseMessage = clientSocket.recv(4096)
while responseMessage:
    result += responseMessage.decode("utf-8")
    responseMessage = clientSocket.recv(4096)

clientSocket.close()
print("response: ", result)