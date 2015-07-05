# Basic TCP Client
# Written by Azlirn


import socket

target_host = raw_input("Enter the target host (ONLY TESTED WITH IPv4 Addresses): ")
target_port = raw_input("Enter the target port: ")

target_host = "www.google.com"
target_port = 80

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to client
client.connect((target_host,int(target_port)))

# Send some data
client.send("GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print response

exit()
