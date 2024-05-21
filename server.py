import socket
  
def handle_request(request):
   
    parts = request.split(' ')
    
    
    if len(parts) > 1:
        path = parts[1]
    else:
        path = '/'
    if path == '/' or path == '/index.html':
        response = "HTTP/1.0 200 OK\n\n"
        with open('index.html', 'r') as file:
            response += file.read()
    elif path == '/about.html':
        response = "HTTP/1.0 200 OK\n\n"
        with open('about.html', 'r') as file:
            response += file.read()
    else:
        response = "HTTP/1.0 404 NOT FOUND\n\n<h1>404 Not Found</h1>"
    
    return response

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
print("Server started on port 8080")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Request: {request}")
    response = handle_request(request)
    
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
