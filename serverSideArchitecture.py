import socket
import threading
import pygame


# Initialize pygame
#pygame.mixer.init()

# Load a sound file for the notification
#notification_sound = pygame.mixer.Sound('notification_notif.mp3')

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sname = input('Enter your name : ')

# Bind the socket to an address and port
server_address = ('172.22.101.13', 5410)  # You can change the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# Function to send messages
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Start a thread to send messages
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()

# Receive and print messages from the client
try:
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"\t\t\t {message.decode('utf-8')}")
# Play the notification sound
#       notification_sound.play()
except KeyboardInterrupt:
    print("Server stopped.")
    client_socket.close()
    server_socket.close()

