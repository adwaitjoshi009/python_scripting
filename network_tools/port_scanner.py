#! /usr/bin/python

# This is our port scanner script.

import socket

print('Enter the target that you want to scan: ')

tcp_address = input()

start_port = int(input('Enter first port: '))
end_port = int(input('Enter last port: '))

save_option = input('Save results to file? (y/n): ')

output_file = None
results = []

if save_option == 'y':
    output_file = input('Please enter filename: ')

try:
    print('\nScanning...\n')

    for port in range(start_port, end_port + 1):

        firstSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        firstSocket.settimeout(0.5)

        result = firstSocket.connect_ex((tcp_address, port))

        if result == 0:
            output = '[+] Port ' + str(port) + ' is OPEN'
            print(output)
            results.append(output)

        firstSocket.close()

    if output_file:
        file = open(output_file, 'w')

        for line in results:
            file.write(line + '\n')

        file.close()

        print('\nResults saved to ' + output_file)

except ValueError:
    print('Port must be a number.')

except Exception as e:
    print('Error: ', e)