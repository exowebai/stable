import socket
import sys
import select
import datetime
import csv

# Define the server's IP address and port
server_ip = '0.0.0.0'  # Replace with the actual IP of the server machine
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

# List to store input sources (stdin and client socket)
input_sources = [sys.stdin, client_socket]

while True:
    # Use select to monitor input sources for readability
    readable, _, _ = select.select(input_sources, [], [])

    for source in readable:
        if source == sys.stdin:
            # Read user input and send it to the server
            message = input("Enter a message to send to the server (or 'exit' to quit): ")

            if message.lower() == 'exit':
                client_socket.close()
                sys.exit(0)

            client_socket.send(message.encode('utf-8'))
        elif source == client_socket:
            # Receive and display messages from the server
            data = source.recv(1024).decode('utf-8')
            if not data:
                print("Server closed the connection.")
                client_socket.close()
                sys.exit(0)
            else:
                # save the data to a CSV file linked to the client
                line = {}
                line['src'] = socket.gethostname()
                line['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                line['data'] = data
                with open('data/'+line['src']+'.csv', 'a') as f:
                    writer = csv.DictWriter(f, fieldnames=['src', 'datetime', 'data'])
                    writer.writerow(line)
