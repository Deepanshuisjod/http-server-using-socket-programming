# HTTP Server using Socket Programming

## Overview

This is a simple HTTP server implemented in Python using socket programming. The server follows the TCP/IP model and provides basic functionality to handle HTTP requests and responses.

## Prerequisites

Ensure you have a good understanding of the following concepts before using this HTTP server:

- **Socket Programming:** Understanding of how sockets work is crucial as the server relies on socket programming to handle communication between clients and the server.

- **TCP/IP Model:** Familiarity with the TCP/IP model, its layers, and how it facilitates communication between devices.

- **TCP/IP Sockets:** Understanding of TCP/IP sockets, especially how they are used for communication between processes over a network.

- **HTTPS Headers:** Knowledge of HTTP headers, especially those related to secure communication (HTTPS). This is important for handling secure connections.

- **HTTP Verbs:** Understanding of HTTP methods (GET, POST, PUT, DELETE, etc.) and how they are used in client-server communication.

## Features


- **Basic HTTP Server:** Handles basic HTTP requests and responds with appropriate HTTP status codes.

- **TCP/IP Communication:** Implements communication using the TCP/IP protocol stack.

- **HTTPS Support:** Provides basic support for HTTPS communication, ensuring secure data transfer.

- **Multiple Client Connections:** Demonstrates how to handle multiple client connections concurrently, allowing the server to serve multiple clients simultaneously.

- **File Handling:** Shows how to fetch files using HTTP GET requests and how to post content to a file using HTTP POST requests.

- **Error Handling:** Responds with a 404 error if a requested file is not found.

- **Header Parsing:** Explains how to parse HTTP headers to extract information about the client's request.


## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/Deepanshuisjod/http-server-using-socket-programming.git
   cd http-server-using-socket-programming
2. Run the Server:

     ```bash
   ./server.py
