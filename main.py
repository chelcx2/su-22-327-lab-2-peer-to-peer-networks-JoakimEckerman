
import socket

localHost = "127.0.0.1" 
port = 1234  # Port to listen on (non-privileged ports are > 1023)

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

