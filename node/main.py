
import sys
from socket import *

print ("starting...")
 
try:
    #resolving ip address
    hostIP = gethostbyname(gethostname()) 
    print("Host ip: {}".format(hostIP))
except gaierror:
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
print ("Looking for open ports...")
for port in range(65535):      #check for all available ports
  
    try:
        #print('trying')
        serv = socket(AF_INET, SOCK_STREAM) # create a new socket
  
        serv.bind((hostIP, port)) # bind socket with address
             
    except:
  
        print('[OPEN] Port open :',port) #print open port number
  
    #print('closing')
    serv.close() #close connection
'''
try:
    # will scan ports between 65400 to 65450
    for port in range(65400, 65450):
        s = socket(AF_INET, SOCK_STREAM)
        print("resolving s as ".format(s))
        setdefaulttimeout(1)

        result = s.connect_ex((hostIP,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
         #connecting to server
        #s.connect((host_ip,port))
        #print("Port {} is open".format(port))
        #s.close()

except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except error:
        print("\ Server not responding !!!!")
        sys.exit()
'''


print ("exiting...")



'''
# creating socket object and then setting up a listening socket for the SERVER side
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #associates socket w a specific network interface and port num
    s.bind((localHost, port))
    #listening for connections from CLIENTS
    s.listen()
    #here it accepts the connection and will give us a NEW socket obj >> this the socket well use to communicate w the CLIENT
    conn, addr = s.accept()

    # Defining a target
    if len(sys.argv) == 2:
        # translate hostname to IPv4
        target = s.gethostbyname(sys.argv[1])
    else:
        print("Invalid amount of Argument")
    
    # Add Banner
    print("=" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("=" * 50)
    
    try:
        # will scan ports between 65400 to 65450
        for port in range(65400,65450):
            s.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port)) # open socket list goes here?
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

    with conn:
        print(f"Connected by {addr}")
        # add to a list before sending files
        while True:
            #infinite loop to loop over blocking calls and send sent CLIENT data using .sendall()
            data = conn.recv(65432) 
            if not data:
                break
            conn.sendall(data)

'''
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
