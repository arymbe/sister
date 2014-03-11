#!/usr/bin/env python

"""
Client yang akan meminta request data dari server
"""

import socket
import sys
import pickle
import shutil


#ini buat setting koneksi
host = 'localhost'
port = 1234
server_address = (host,port)
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

while 1:
    #read from keyboard
    #line = sys.stdin.readline()
    #ini buat masukin inputan
    line = raw_input(">> ")
    #ini buat ngirim inputan ke server
    s.send(line)
    #ini buat keluar
    if (line == 'keluar') :
        break
    #ini buat ngambil paket
    data = s.recv(size)
    #ini buat ngeload paket
    data = pickle.loads(data)
    #ini buat ngeprint
    print data
s.close()
