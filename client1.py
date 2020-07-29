import socket
import threading
import time


host=socket.gethostbyname(socket.gethostname())
port=4444

client=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
client.connect((host,port))


message=input("-->")
while message !='q':

        while True:

                client.send(message.encode('utf-8'))
                data=client.recv(1024).decode()
                if not str(data):
                        break
                print("[Message INTERCEPTED::]Received data--> "+data)
                message=input("-->")

client.close()