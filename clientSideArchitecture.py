import socket
import threading
#import pygame

# Initialize pygame
#pygame.mixer.init()

# Load a sound file for the notification
#notification_sound = pygame.mixer.Sound('pika.mp3')
# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#cname = input('Enter your name : ')

# Connect to the server
server_address = ('172.22.100.182', 5410)  # Use the same address and port as the server
client_socket.connect(server_address)

# Function to send messages
def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Start a thread to send messages
send_thread = threading.Thread(target=send_messages)
send_thread.start()

# Receive and print messages from the server

try:
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"\t\t\t {message.decode('utf-8')}")
# Play the notification sound
#        notification_sound.play()

except KeyboardInterrupt:
    print("Client stopped.")
    client_socket.close()
