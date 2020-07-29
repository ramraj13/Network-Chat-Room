import socket
import threading
import time

host=socket.gethostbyname(socket.gethostname())
port=4444
address=(host,port)
server=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
server.bind(address)

def client(conn,address1,connections):
    while True:
        data=conn.recv(1024)
        if not str(data.decode()):
            print(f"Client {address1}is Disconnected... ")
            break

        print(f"Data received from {address1} is {str(data.decode())}")

        for con in connections:
            if con!= conn:
                con.send(data)



    conn.close()


def handle_clients(conn,clients):
    pass

def start():
    clients=[]
    connections=[]
    server.listen()
    print("[Starting Server]Connecting to server...")
    while True:
        conn,address=server.accept()
        print(f"server connected at{address}")
        if address not in clients:
            clients.append(address)

        if conn not in connections:
            connections.append(conn)


        r1=threading.Thread(target=client,args=(conn,address,connections))
        r1.start()




if __name__=='__main__':
    start()