# -*- coding:UTF-8 -*-
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'c0000101a60a00'
data_sent = ''
for i in range(0,len(data),2):
    print(i)
    d = int( data[i:i+2], 16 )
    print(d)
    data_sent += struct.pack('B', d)
s.sendto(data, ('103.41.55.244', 34013))
