#! /usr/bin/python

# This is our first networking script.

import socket

print('Enter the address you want to grab banner from: ')

tcp_address = input()

port = int(input('Enter port number: '))

try:
    firstSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    firstSocket.connect((tcp_address, port))

    print('Connected!')

    banner = firstSocket.recv(1024)

    print(banner)

except ValueError:
    print("Port must be a number.")
except Exception as e:
    print("Error: ", e)

    firstSocket.close()
