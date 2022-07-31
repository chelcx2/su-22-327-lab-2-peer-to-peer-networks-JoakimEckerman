
"""this the client, the sender"""
import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

""" here we specify the IP address, port of the server we will try to connect to, and the name of the files we will be sending  """
# the ip address or hostname of the server, the receiver
host = "192.168.1.101"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
filename = "data.csv"
# get the file size
filesize = os.path.getsize(filename)