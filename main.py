import zmq, time, pickle, sys

context = zmq.Context()
me = str(sys.argv[1])
s = context.socket(zmq.PUSH) # create a push socket
src = SRC1 if me == '1' else SRC2 # check task source host
prt = PORT1 if me == '1' else PORT2 # check task source port
p = "tcp://"+ src +":"+ prt # how and where to connect
s.bind(p) # bind socket to address

while True: # generate 100 workloads
    pass
    #workload = random.randint(1, 100) # compute workload
    #s.send(pickle.dumps((me,workload))) # send workload to worker


#context = zmq.Context()
me = str(sys.argv[1])
r = context.socket(zmq.PULL) # create a pull socket
p1 = "tcp://"+ SRC1 +":"+ PORT1 # address first task source
p2 = "tcp://"+ SRC2 +":"+ PORT2 # address second task source
r.connect(p1) # connect to task source 1
r.connect(p2) # connect to task source 2

while True:
    pass
    #work = pickle.loads(r.recv()) # receive work from a source
    #time.sleep(work[1]*0.01) # pretend to work