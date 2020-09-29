
#Regular Expressions

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


import re
hand = open('mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):    #the . represents and character 
        print(line)
        count += 1 
print(count)




import re
hand = open('mbox.txt')
count = 0
for line in hand:
    line = line.rstrip()
    e = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', line)
    if len(e) > 0:
        print(e)
        count += 1 
print(count)

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.

import re
hand = open('mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
        count += 1 
print(count)


import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)



# gets time the mail was send
import re
hand = open('mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    t = re.findall('^From .* ([0-9][0-9].[0-9][0-9].[0-9][0-9])\s', line)
    if len(t) > 0:
        print(t)
        count += 1 
print(count)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)




import re
hand = open('regex_sum_955401.txt')

lst = list()

for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]*\d', line)
    if len(x) > 0:
        lst.extend(x)    
for i in range(0, len(lst)): 
    lst[i] = int(lst[i]) 
    
total = sum(lst)
print(total)



import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()



import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    time.sleep(0.25)            #when conenting this line then the data recived will be the max every iteration. flow control
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

#read any size file without using all memory downloading in blocks
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
