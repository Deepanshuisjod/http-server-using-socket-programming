import socket

server_ip = 'localhost'
server_port = 4221

client = socket.socket()
client.connect((server_ip,server_port))

request = 'POST /files/sample.txt HTTP/1.1\r\nContent : Hi there , How are you my name is Deepanshu\r\n\r\n'

client.sendall(request.encode('utf-8'))

response = client.recv(4221).decode('utf-8')
print(response)

client.close()
