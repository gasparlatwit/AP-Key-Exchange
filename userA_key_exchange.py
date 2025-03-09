import socket


def server_key_exchange():
    host = socket.gethostname()
    port = 5000  # initiate port

    userA = socket.socket()  
    userA.bind((host, port))   

    userA.listen(1) # only allows for 1 user connection since it is a 1 - 1 exchange
    conn, address = userA.accept()  # accept new connection
    print("Key Exchange with: " + str(address))
    
    q = 353 # a prime number used as the module
    a = 3 # a primative root of q and a < q
    print("Sent agreed q & a")
    print("q: ", q)
    print("a: ", a)
    conn.send(str(q).encode()) # send agreed q and a
    conn.send(str(a).encode()) # they publically agree on this but I am having userA send them as a start to the connection

    XA = 97 # userA selects XA = 97
    YA = a**(XA)%q # userA calculates the public component of the key YA=(a to the power of XA) mod q
    
    print("UserA Private Key: ", XA)
    print("UserA Public Key: ", YA)

    conn.send(str(YA).encode())# userA transmites YA to UserB

    YB = int(conn.recv(1024).decode())
    print("UserB Public Key: ", YB)

    # At this point both users can calculate a common key k

    Ka = YB**(XA)%q # userA calculates secret key
    print("Secret Key A: ", Ka)


    conn.close()  # close the connection


if __name__ == '__main__':
    server_key_exchange()

# Lucas Gaspar
# UserA has never received UserB's private key yet still comes to the same secret key
# Ka is equal to Kb because of the communitive property of multiplication 
# as well as the properties associated with modulos and exponents
# no matter which direction you calculcate it, the result will be the same,
# allowing both userA amd UserB to securely communicate