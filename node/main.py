
import sys, os, traceback, time
from threading import Thread
from socket import *
from tracemalloc import stop
from ping3 import ping


print ("starting...")

'''
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", 1234))
s.sendto(msg, ("255.255.255.255", 1234))
s.listen()
'''
files = os.listdir("/files")
requestFiles = []
listIP = []
#listIP.append(gethostbyname(gethostname()))

def broadcastRequest():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(b"List all files.", ("255.255.255.255", 1234))

def broadcastListen(stop):
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
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
        else:
            if msg not in files:
                requestFiles.append(msg)

def fileTransfer():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    for file in requestFiles:
        filesize = os.path.getsize(file)
        s.connect("", 1234)
        s.send(f"{file}{SEPARATOR}{filesize}".encode("utf-8"))
        

stop = False

time.sleep(1)
Thread(target = broadcastListen, args = (lambda: stop,)).start()
time.sleep(1)
Thread(target = broadcastRequest).start()
time.sleep(1)
Thread(target = broadcastListen, args = (lambda: stop,)).start()

stop = True
print("exiting...")

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