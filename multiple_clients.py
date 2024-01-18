import socket
import time
import asyncio

async def client1(server_ip,server_port):
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((server_ip, server_port))

    http_request_1 = "GET /user-agent HTTP/1.1\r\nHost: localhost :4221\r\nUser-Agent: curl/7.64.2\r\n"
    client1.sendall(http_request_1.encode('utf-8'))
    response1 = client1.recv(4221).decode('utf-8')
    return response1

async def client2(server_ip,server_port):
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2.connect((server_ip, server_port))

    http_request_2 = "GET / HTTP/1.1\r\nHost: localhost :4221\r\nUser-Agent: curl/7.64.1\r\n"
    client2.sendall(http_request_2.encode('utf-8'))
    response2 = client2.recv(4221).decode('utf-8')
    return response2

async def main():
    server_ip = 'localhost'
    server_port = 4221
    
    start_time = time.time()

    batch = asyncio.gather(client1(server_ip,server_port),client2(server_ip,server_port))
    response_client1 , response_client2 = await batch

    end_time = time.time()

    print(f"Response from client 1 : {response_client1}")
    print(f"Response from client 2 : {response_client2}")
    print(f"Time taken : {end_time-start_time}")
if __name__ == '__main__':
    asyncio.run(main())

