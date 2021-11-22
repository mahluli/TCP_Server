#!/usr/bin/env python3

import socket
import sys

f = open("sensorlog.txt", "w+")

#TODO: Add code to create a socket ready to recieve data

HOST = "172.17.0.3"  # Standard loopback interface address (localhost)
PORT = 65432     # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    myHostName = socket.gethostname()
    print(myHostName)
    myIP = socket.gethostbyname(myHostName)
    print(myIP)
    s.bind((myIP, PORT))
    s.listen()
    print("waiting for device!!")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('\nReceived', repr(data.decode()))
            f.write("\nReceived: ")
            f.write(repr(data.decode()))
            f.flush()
            if not data:
                break


