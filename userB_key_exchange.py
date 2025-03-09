import socket


def client_key_exchange():
    host = socket.gethostname()  # on same machine
    port = 5000  # server/UserA port number

    userB = socket.socket()  # start connection
    userB.connect((host, port))  # connect to the server


    q = int(userB.recv(1024).decode())  # receive agreed q
    a = int(userB.recv(1024).decode())  # receive agreed a
    print("Received q & a")
    print("q: ", q)  # agree and show in terminal
    print("a: ", a)  # agree and show in terminal

    XB = 233 # userB selects a secret XB (XB < q)
    YB = a**(XB)%q # userB calcualtes the public component of the key YB=(a to the power of XB) mod q
    
    print("UserB Private Key: ", XB)
    print("UserB Public Key: ", YB)

    YA = int(userB.recv(1024).decode()) # receive UserA public Key

    print("UserA Public Key: ", YA)
    
    userB.send(str(YB).encode()) # userB transmits YB to UserA

    # At this point both users can calculate a common key k

    Kb = YA**(XB)%q # UserB calculates secret key
    print("Secret Key B: ", Kb)

    userB.close()  # close the connection


if __name__ == '__main__':
    client_key_exchange()

# Lucas Gaspar
# UserB has never received UserA's private key yet still comes to the same secret key
# Kb is equal to Ka because of the communitive property of multiplication 
# as well as the properties associated with modulos and exponents
# no matter which direction you calculcate it, the result will be the same,
# allowing both userA amd UserB to securely communicate