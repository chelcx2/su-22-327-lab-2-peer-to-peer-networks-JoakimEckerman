
import sys, os
import socket
from threading import Thread
from socket import *
from tracemalloc import stop
from ping3 import ping


print ("starting...")

# returns a list of files we have
files = os.listdir("/files")
# names of the files the node doesnt have
requestFiles = []
# all the ips of the other nodes 
listIP = []
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
#listIP.append(gethostbyname(gethostname()))

#send a msg to all of the other nodes
def broadcastRequest():
    #creating a socket using IPv4, UDP socket
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(b"List all files.", ("255.255.255.255", 1234))

#listening for a msg from the other nodes
def broadcastListen(stop):
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("", 1234))
    while True:
        #receiving the msg we get from broadcast 
        msg, senderIP = s.recvfrom(1234)
        newIP = str(senderIP[0])

        if newIP not in listIP and newIP != gethostbyname(gethostname()):
            listIP.append(newIP)

        if stop():
            break

        msg = msg.decode("utf-8")
        if msg == "List all files.":
            print("Sending list of files")
            for file in files:
                s.sendto(file.encode("utf-8"), (newIP, 1234))
        else:
            if msg not in files:
                requestFiles.append(msg)

def fileTransferSend():
    #making our server
    def server():
    #creating our server socket
    serversock = socket.socket()
    host = socket.gethostname();
    port = 9000;
    #bind the ip and port to serversock
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
    for file in files:
        print("sending: " + file)
        filesize = os.path.getsize(file)
        print("filesize: " + filesize)
        s.connect("", 1234)
        s.send(f"{file}{SEPARATOR}{filesize}".encode("utf-8"))
        with open(file, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                s.sendall(bytes_read)

def fileTransferRecieve():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("", 1234))
    s.listen()
    clientSocket, clientIP = s.accept()
    received = clientSocket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filesize = int(filesize)
    if filename not in files:
        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = clientSocket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)
        requestFiles.remove(filename)
'''Each device on the network can safely run a service on the same port. EX >>
172.17.0.1:1234
172.17.0.2:1234
172.17.0.3:1234
172.17.0.4:1234
'''
        

stop = False

time.sleep(1)
Thread(target = broadcastListen, args = (lambda: stop,)).start()
time.sleep(1)
Thread(target = broadcastRequest).start()
time.sleep(1)
Thread(target = broadcastListen, args = (lambda: stop,)).start()
stop = True
time.sleep(1)
Thread(target = fileTransferSend).start()
time.sleep(1)
Thread(target = fileTransferRecieve).start()

print("exiting...")
sys.exit()

'''
if os.path.isfile("serverlist.txt"):
    os.remove("serverlist.txt")

ad = ''.join(str(address));
ad1 = ad.split()
ad2= ad1[0]
ad3=ad2[2:15]
print ad3
f = open('serverlist.txt', 'a')
f.write(ad3+'\n')
f.close()
'''