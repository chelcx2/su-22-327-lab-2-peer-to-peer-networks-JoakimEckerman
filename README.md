# CECS 327 Lab - Peer to Peer Networks

## Assignment Description
The goal of this assignment is to become familiar with peer to peer (P2P) networks and having a client act as both client and server using the same codebase. You may work on this project in pairs if you choose.

Design a program which allows two or more computers to synchronize files across a local area network (LAN). In order to complete the assignment, I am requiring the use of [Docker](https://www.docker.com) to implement your distributed network which will simulate the networking environment and manage the seperate nodes in this network.

Each Docker contianer will be a seperate instance of your running code. All nodes *must* be identical in code with the exception of the configuration locations, directory attachments, etc. Essentially, only their Docker config files may differ.

You will be "exchanging" files from one node to the other through the use of *[sockets](https://linux.die.net/man/7/socket)*, which are [Linux and Unix's way of implementing interprocess communication](https://www.linuxhowtos.org/C_C++/socket.htm).

Here is an example of the "networking" that I would like to have implemented (warning: lots of *set theory math* ahead):

> Nodes $P_{1},P_{2},\ldots P_{n}$ have clients $C_{1},C_{2},\ldots C_{n}$ installed on each node respectively. $F_{1},F_{2},\ldots F_{n}$ are sets of files where $F_{1}$ is the set of files on node $P_{1}, F_{2}$ is the set of files on node $P_{2}$, and so forth.

> The goal of your program should be the unification of all sets of files, $F$, so that $P_{i},C_{i}\cup \{ F_{j}\}$ on each client.

Essentially, what I am asking you to do is to create your own mini version of [Dropbox](https://dropbox.com); rather, you will be making a program which will run many instances in Docker and each "instance" will act as a node to synchronize all of the files which one instance "points" to (which may be on a local hard-drive, a network, or *anywhere* really) with the contents of whatever the other node "points" to.

Since your computer is emulating the "universe" for your running nodes, you can (and should) specify seperate "sync" locations for each node. This can be done by using a [Docker Compose config file](https://docs.docker.com/compose) for your assignment. Docker Compose allows for one file to configure many different Docker nodes all at once.

## Some Notes
* If you're working in pairs for this assignment, please let me know ASAP and I will create a single git repository for both people to use.
* If you've done the previous assignment (and hopefully feel more comfortable using Docker), great! If not, this is where I would highly recommend to start. Also, if you did the lesson and want a bit "more", I encoruage you to find a few Docker repositories and play with them. I particulary enjoy tinkering with the [repos made by linuxserver.io](https://www.linuxserver.io).
* If you're feeling okay with Docker and still don't know where to start, try making a Docker container with a defined port/socket and a simple program to handle that socket [using something like this](https://realpython.com/python-sockets).
* You might need a distributed hash table (DHT) 
implementation in order to complete this assignment, although, if you are clever, there is a way to do this assignment without one. :)

* Before diving in to the project, there are a few things that I recommend you consider:
  * How will your nodes discover other clients on the network? Remember, just because it's Docker doesn't mean we don't have to implement the LAN networking too.
  * How will your client deal with files of the same name but different contents? Different timestamps?
  * How will your client determine the order of syncing with regards to the files of other clients? (Docker might help here).

# Deliverables
Demonstrate your working code on a unique set of files for each Docker node (minimum of *four* active nodes) for the instructor.

Your submission must follow the following rules, else *I will not grade it and you will receive a zero for the submission*:

* Do *not* use compression on your files
* Make sure that all significant code is *commented* with your own explanations. Since this is potentially a *group* assignment, your commit comments are highly important as well. Please use them.
