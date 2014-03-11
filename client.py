#!/usr/bin/env python

"""
Client yang akan meminta request data dari server
"""

import socket
import sys
import pickle
import shutil

host = 'localhost'
port = 1234
server_address = (host,port)
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

while 1:
    #read from keyboard
    #line = sys.stdin.readline()
    line = raw_input(">> ")
    s.send(line)

    if (line == 'keluar') :
        break
    data = s.recv(size)
    data = pickle.loads(data)
    print data
s.close()