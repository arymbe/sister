#!/usr/bin/env python

"""
An echo server from http://ilab.cs.byu.edu/python
Multiclient server, using select
"""

import select
import socket
import sys
import pickle

#ini buat setting koneksi
host = 'localhost'
port = 1234
server_address = (host,port)
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(backlog)

# buka inputan file
strPath = 'cuaca.txt'
f=open(strPath)

# baca inputan file
# buat array yang berindex string
dict = {}
semua = ''
for line in f:
	#di split berdasarkan koma, untuk mendapatkan nama hari dan cuacanya
	temp = line.split(',')
	#dict[Hari] bernilai cuaca
	dict[temp[0]] = temp[1]
	#variabel semua untuk menyimpan semua keterangan cuaca
	semua = semua + '\n' + temp[0] + ' : ' + temp[1]

#strText=f.read()
#dataSplit = strText.split('\n')
#cobaPickle = pickle.dumps(strText)

#server mempunyai 2 atau lebih pernyataan untuk modul sys
input = [server]

#menunggu client baru atau client yang lain untuk menginputkan masukan yang baru
running = 1

#ketika server dinyalakan
while running :
    print "Waiting multi connection"
#siap menerima inputan
    inputready, outputready, exceptready = select.select(input, [], [])
#menyimpan urutan perintah dan alamat client
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
#fungsi untuk keluar server
        else:
            #handle all other sockets
            data = s.recv(size)
            if (data == 'keluar') :
                ret = 'server exit'
                cobaPickle = pickle.dumps(ret)
                s.send(cobaPickle)
                running = 0
                break
#menyimpan imputan yang di split berdasarkan spasi
            temp = data.split(' ')
            ret = ''
            #ketika inputan bertuliskan semua dia akan mengembalikan variabel semuaa
            if temp[1] == 'semua' :
                ret = semua
            #jika tidak, dia akan ngeprint nama hari, dan cuaca pada hari tersebut
            else :
                for key, value in dict.items() :
                    if (key == temp[1]) :
                        ret = temp[1] + ' : ' + dict[temp[1]]
                        break
                #ret = temp[1] + ' : ' + dict[temp[1]]

            cobaPickle = pickle.dumps(ret)
            s.send(cobaPickle)
server.close()
