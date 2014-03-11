#!/usr/bin/env python

"""
An echo server from http://ilab.cs.byu.edu/python
Multiclient server, using select
"""

import select
import socket
import sys
import pickle

host = 'localhost'
port = 1234
server_address = (host,port)
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(backlog)
strPath = 'cuaca.txt'
f=open(strPath)

dict = {}
semua = ''
for line in f:
	temp = line.split(',')
	dict[temp[0]] = temp[1]
	semua = semua + '\n' + temp[0] + ' : ' + temp[1]

#strText=f.read()
#dataSplit = strText.split('\n')
#cobaPickle = pickle.dumps(strText)

#server mempunyai 2 atau lebih pernyataan untuk modul sys
input = [server]

#menunggu client baru atau client yang lain untuk menginputkan masukan yang baru
running = 1

while running :
    print "Waiting multi connection"

    inputready, outputready, exceptready = select.select(input, [], [])

    for s in inputready :
        if s == server:
            #handle the server socket
            client, address = server.accept()
            #server.append(client)
            input.append(client)

        elif s == sys.stdin:
            #handle standard input
            test = raw_input("input : ")
            if (test == 'keluar') :
                running = 0
                break

        else:
            #handle all other sockets
            data = s.recv(size)
            if (data == 'keluar') :
                ret = 'server exit'
                cobaPickle = pickle.dumps(ret)
                s.send(cobaPickle)
                running = 0
                break

            temp = data.split(' ')
            ret = ''
            if temp[1] == 'semua' :
                ret = semua
            else :
                for key, value in dict.items() :
                    if (key == temp[1]) :
                        ret = temp[1] + ' : ' + dict[temp[1]]
                        break
                #ret = temp[1] + ' : ' + dict[temp[1]]

            cobaPickle = pickle.dumps(ret)
            s.send(cobaPickle)
server.close()