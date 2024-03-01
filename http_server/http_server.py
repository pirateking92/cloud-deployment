import socket

def handle_request(request):
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, world! YOU IS STUPID\r\n"
    return response

def run_server(host, port):
    # create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"SERVER LISTENING ON {host}: {port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"CONNECTION FROM {client_address}")

            with client_socket:
                request_data = client_socket.recv(1024).decode("utf-8")
                if request_data:
                    print("RECEIVED REQUEST YO:")
                    print(request_data)

                    response_data = handle_request(request_data)
                    client_socket.sendall(response_data.encode("utf-8"))

                    print("RESPONSE SEENNTTT")
                else:
                    print("NO DATA FROM CLIENT!!!")

if __name__ == "__main__":
    # Define server host and port
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8080
    
    # Run the server
    run_server(SERVER_HOST, SERVER_PORT)