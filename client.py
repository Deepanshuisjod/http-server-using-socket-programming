import socket

server_ip = 'localhost'
server_port = 4221

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

http_request = "GET / HTTP/1.1\r\nHost: localhost :4221\r\nUser-Agent: curl/7.64.1\r\n"

client.sendall(http_request.encode('utf-8'))

response = client.recv(4221).decode('utf-8')
print(response)

client.close()


