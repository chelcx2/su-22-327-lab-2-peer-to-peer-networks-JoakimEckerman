
import sys, os
import socket
from threading import Thread
from socket import *



print ("starting...")

def server():
    serversock = socket.socket()
    host = socket.gethostname();
    port = 9000;
    serversock.bind((host,port));
    filename = ""
    serversock.listen(10);
    print ("Waiting for a connection.....")

    clientsocket,addr = serversock.accept()
    print("Got a connection from %s" % str(addr))
    while True:
        size = clientsocket.recv(16) # Note that you limit your filename length to 255 bytes.
        if not size:
            break
        size = int(size, 2)
        filename = clientsocket.recv(size)
        filesize = clientsocket.recv(32)
        filesize = int(filesize, 2)
        file_to_write = open(filename, 'wb')
        chunksize = 4096
        while filesize > 0:
            if filesize < chunksize:
                chunksize = filesize
            data = clientsocket.recv(chunksize)
            file_to_write.write(data)
            filesize -= len(data)

        file_to_write.close()
        print ('File received successfully')
    serversock.close()

def client():
        
    s = socket.socket()
    host = socket.gethostname()
    port = 9000
    s.connect((host, port))
    path = "blah"
    directory = os.listdir(path)
    for files in directory:
        print (files)
        filename = files
        size = len(filename)
        size = bin(size)[2:].zfill(16) # encode filename size as 16 bit binary
        s.send(size)
        s.send(filename)

        filename = os.path.join(path,filename)
        filesize = os.path.getsize(filename)
        filesize = bin(filesize)[2:].zfill(32) # encode filesize as 32 bit binary
        s.send(filesize)

        file_to_send = open(filename, 'rb')

        l = file_to_send.read()
        s.sendall(l)
        file_to_send.close()
        print ('File Sent')

    s.close()

'''   s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 1234))
s.listen()
try:
    #resolving ip address
    hostIP = gethostbyname(gethostname())
    print("Host ip: {}".format(hostIP))
except gaierror:
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

listIP = []
for num in range(2,6):
    ip = "172.30.0."+str(num)
'''Each device on the network can safely run a service on the same port. EX >>
172.17.0.1:1234
172.17.0.2:1234
172.17.0.3:1234
172.17.0.4:1234
'''
    if ping(ip):
        if not ip in listIP:
            listIP.append(ip)

#print(*listIP, sep = "\n")
#print ("Looking for open ports...")

try:
    found = False
    for ip in listIP:
        # will scan all ports
        print("looking for open ports in {}".format(ip))
        for port in range(1,65535):
            s = socket(AF_INET, SOCK_STREAM)
            #setdefaulttimeout(1)

            result = s.connect_ex((ip,port))
            if result == 0:
                print("Port {} is open".format(port))
                found = True
            s.close()
    if not found:
        print("no open ports found")

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except error:
    print("\ Server not responding !!!!")
    sys.exit()    '''


print ("exiting...")