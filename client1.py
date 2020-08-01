import socket
import threading
import time

host=socket.gethostbyname(socket.gethostname())
port=4444
print(host)

client=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
client.connect((host,port))

def receive():
        data=client.recv(1024).decode()
        print("[Message intercepted]"+data)
        print('-->')
        receive()

def sent():
        message=input('-->')
        client.send(message.encode('utf-8'))
        sent()

t_receive=threading.Thread(target=receive)

if __name__=="__main__":
        t_receive.start()
        sent()

        client.close()

