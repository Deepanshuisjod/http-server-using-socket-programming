#!/usr/bin/env python3
import socket
import os

PORT, SERVER = 4221, 'localhost'
ADDR = (SERVER, PORT)

# Function to check if file exists
def file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)

# Function to extract content from the file if exists
def fetch_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def post_content(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)
    return True

# Function to handle get request by the client
def get_request(path, connection_from_client, address, request):
    # root path
    if path == '/':
        print(f"Connection from: {address}")
        response_body = "This is the root path!"
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

    # /echo/abc path
    elif path.startswith('/echo'):
        print(f"Connection from: {address}")
        response_body = path.split('/')[2]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

    # /user-agent path
    elif path.startswith('/user-agent'):
        print(f"Connection from: {address}")
        user_agent = request.split('User-Agent: ')[1].split('\r\n')[0]
        response_body = user_agent
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

    # Get a file / fetching data from a file
    elif path.startswith('/files'):
        print(f"Connection from: {address}")
        file_path = '.' + path.split(' ')[1]
        print(file_exists(file_path))
        if file_exists(file_path):
            content = fetch_content(file_path)
            response_body = content
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"

    # responding with 404 error. The page you are trying to request DNE
    else:
        print("Connection from the client side did not establish!")
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    connection_from_client.send(response.encode('utf-8'))
    connection_from_client.close()

# Function to handle post request by the client
def post_request(path, request, connection_from_client, address):
    print(f"Connection from: {address}")
    content = request.split('\r\n') # Get the last line as content
    content = content.split(' ')[-1] 
    file_path = '.' + path.split(' ')[0]
    if file_exists(file_path):
        posted = post_content(file_path, content)
        response_body = "Content posted successfully" if posted else "Failed to post content"
        response = f"HTTP/1.1 201 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    connection_from_client.send(response.encode('utf-8'))
    connection_from_client.close()

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    connection_from_client, address = server.accept()
    request = connection_from_client.recv(4096).decode('utf-8')  # Adjust the buffer size
    path = request.split(' ')[1]
    request_type = request.split(' ')[0]

    if request_type == 'GET':
        get_request(path, connection_from_client, address, request)

    elif request_type == 'POST':
        post_request(path, request, connection_from_client, address)
