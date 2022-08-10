
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
files = str(os.listdir("/files"))
requestFiles = []
listIP = []

def broadcastRequest():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(b"List all files.", ("255.255.255.255", 1234))

def broadcastListen(stop):
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    s.bind(("", 1234))
    while True:
        msg, senderIP = s.recvfrom(1234)
        newIP = senderIP

        if newIP not in listIP and newIP != gethostbyname(gethostname()):
            listIP.append(newIP)

        if stop():
            break

        msg.decode("utf-8")
        if msg == b'List all files.':
            print("Sending list of files")
            for file in files:
                transfer = "".join(file) # convert tuple to string
                s.sendto(transfer.encode("utf-8"), (senderIP, 1234))
        else:
            if msg not in files:
                requestFiles.append(msg)

stop = False

time.sleep(1)
Thread(target = broadcastListen, args = (lambda: stop,)).start()
time.sleep(1)
Thread(target = broadcastRequest).start()

stop = True

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