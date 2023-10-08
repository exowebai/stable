import socket
import threading
import datetime
import csv

# Define the server's IP address and port
server_ip = '0.0.0.0'  # Listen on all available network interfaces
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (maximum 10 clients in the queue)
server_socket.listen(10)

print(f"Server is listening on {server_ip}:{server_port}")

# List to store client threads
client_threads = []

def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break  # Exit the loop if no data is received

            # save the data to a CSV file linked to the client
            line = {}
            line['src'] = socket.gethostname()
            line['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line['data'] = data
            with open('data/server.csv', 'a') as f:
                writer = csv.DictWriter(f, fieldnames=['src', 'datetime', 'data'])
                writer.writerow(line)

            # Broadcast the received message to all clients
            for client_thread in client_threads:
                if client_thread != threading.current_thread():
                    client_thread.client_socket.send(data.encode('utf-8'))
        except:
            # Handle any errors or disconnections here
            break

    # Remove the client thread from the list
    client_threads.remove(threading.current_thread())
    client_socket.close()

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Create a thread to handle the client's messages
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.client_socket = client_socket
    client_thread.start()
    client_threads.append(client_thread)
