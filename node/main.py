
import sys, os, traceback, time
from threading import Thread
from socket import *
from tracemalloc import stop


print ("starting...")
print(gethostbyname(gethostname()))

files = os.listdir("/files")
requestFiles = []
listIP = []
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
#listIP.append(gethostbyname(gethostname()))

def broadcastRequest():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(b"List all files.", ("255.255.255.255", 1234))
    s.close()

def broadcastListen(stop):
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("", 1234))
    while True:
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
        elif msg in files and newIP != gethostbyname(gethostname()):
            print("I have the file!")
            t1 = Thread(target = sendFile, args = (msg, newIP, ))
            t1.start()
            t1.join()  
        elif msg not in files:
            requestFiles.append(msg)
            print("Requesting " + msg)
            t1 = Thread(target = requestFile, args = (msg, ))

                    
    s.close()

def sendFile(filename, node):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    print("Connecting to " + node)
    s.connect((node, 1234))
    print("Sending " + filename)
    filesize = os.path.getsize("/files/" + filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode("utf-8"))
    with open("/files/" + filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            #time.sleep(1)
    s.close()

def requestFile(filename):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(("", 1234))
    s.listen()

    s.sendto(filename.encode("utf-8"), ("255.255.255.255", 1234))
    clientSocket, clientIP = s.accept()
    print("Connected to " + clientIP)
    
    
    received = clientSocket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filesize = int(filesize)
    if filename not in files:
        with open("/files/" + filename, "wb") as f:
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
    time.sleep(1)
    s.close()

        

stop = False
time.sleep(5)
Thread(target = broadcastListen, args = (lambda: stop,)).start()
time.sleep(1)
Thread(target = broadcastRequest).start()
time.sleep(1)
Thread(target = broadcastListen, args = (lambda: stop,)).start()
print(listIP)

stop = True

#Thread(target = recieveFile).start()
#Thread(target = sendFile).start()



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