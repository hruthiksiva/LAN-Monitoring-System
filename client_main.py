# -*- coding+9: utf-8 -*-

import socket
from vidgear.gears import ScreenGear
from vidgear.gears import NetGear
from pickle import dumps, loads
import threading

def chat_send():   
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    port = 12345                  
    s.connect(('localhost', port, 0, 0))
    
    print (s.recv(1024) )   
    s.close()
    
def send_video():
    stream = ScreenGear().start()
    server = NetGear(port="54548", protocol="tcp")
    print('Sharing Screen')
    while True:
        try:
            frame = stream.read()
            if frame is None:
                break
            server.send(frame)
    
        except KeyboardInterrupt:
            break
        
    stream.stop()
    server.close()
    
def recv_signal(sock):
    sig = sock.recv(1024).decode()
    
    if sig == 'VID':
        x = threading.Thread(target=send_video)
        x.start()
        
    elif sig == 'CHAT':
        pass
    
if __name__ == '__main__':
    
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    port = 12351
    s.connect(('localhost', port, 0, 0))

    x = threading.Thread(target=recv_signal, args=(s,))
    x.start()
    
    while True:
        x = input('')
        if x == 'exit':
            break
        else:
            pass