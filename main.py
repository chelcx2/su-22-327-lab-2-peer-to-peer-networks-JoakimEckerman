
import datetime, sys, socket #, pickle

localHost = "127.0.0.1" 
port = 65432  # Port to listen on (non-privileged ports are > 1023)

''' creating socket object and then setting up a listening socket for the SERVER side'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket1:
    '''client.socket()'''
    '''specifying socket type Note: this protocol default is TCP'''
    socket.SOCK_STREAM
    socket.AF_INET()
    '''associates socket w a specific network interface and port num'''
    socket.bind((localHost, port))
    '''listening for connections from CLIENTS'''
    socket.listen()
    ''' here it accepts the connection and will give us a NEW socket obj >> this the socket well use to communicate w the CLIENT'''
    conn, addr = socket.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            '''infinite loopto loop over blocking calls and send sent CLIENT data using .sendall()'''
            data = conn.recv(1024) 
            if not data:
                break
            conn.sendall(data)

# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
 
# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
  
try:
    # will scan ports between 65400 to 65450
    for port in range(65400,65450):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()


"""
context = zmq.Context()
me = str(sys.argv[1])
s = context.socket(zmq.PUSH) # create a push socket
src = SRC1 if me == '1' else SRC2 # check task source host
prt = PORT1 if me == '1' else PORT2 # check task source port
p1 = "tcp://"+ SRC1 +":"+ PORT1 # address first task source
p2 = "tcp://"+ SRC2 +":"+ PORT2 # address second task source
s.bind(p1) # bind socket to address 1
s.bind(p2) # bind socket to address 2
s.connect(p1) # connect to task source 1
s.connect(p2) # connect to task source 2

while True: # do stuff
    pass
    #workload = random.randint(1, 100) # compute workload
    #s.send(pickle.dumps((me,workload))) # send workload to worker
    #work = pickle.loads(r.recv()) # receive work from a source
    #time.sleep(work[1]*0.01) # pretend to work
"""
