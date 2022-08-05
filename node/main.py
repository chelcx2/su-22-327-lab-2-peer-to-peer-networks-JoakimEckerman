
import sys, tqdm, os
from tkinter import SEPARATOR #automatically imported when using SEPARATOR
from socket import *
from ping3 import ping

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

print ("starting...")

s = socket(AF_INET, SOCK_STREAM)
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
    sys.exit()

print ("exiting...")