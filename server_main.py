# -*- coding: utf-8 -*-

import socket, cv2
from vidgear.gears import NetGear
import threading
import sys
from getpass import getpass



class Main():
    ids = {}
    clients = {}
    
    def __init__(self, port = 12350):
        self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.port = port
        
    def start(self, n_cli = 5):
        self.sock.bind(('',self.port))
        self.sock.listen(n_cli)
        self.ids['recv_sig'] = threading.Thread(target=self.start_sig)
        self.ids['recv_sig'].start()
        
    def send_sig(self, c_sock, sig):
        c_sock.send(sig.encode())
        
    def recv_sig(self):
        sig = self.sock.recv(1024).decode()
        
    def start_sig(self):
        while True :
            c_sock, addr = self.sock.accept()
            name = c_sock.recv(1024).decode()
            self.clients[name] = [c_sock, addr]
    
    def recv_video(self, port = 54321):
        def inner(port):
            client = NetGear(port = str(port), protocol="tcp", receive_mode=True)
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
        self.ids['recv_video'] = threading.Thread(target=inner, args=(port,))
        self.ids['recv_video'].start()
        
    def deny_ip(self, c_sock, website = None):
        self.send_sig(c_sock, f'DENY {website}')
    
    def allow_ip(self, c_sock,website = None):
        self.send_sig(c_sock, f'ALLOW {website}')
        
def printmsg(msgtype, msg, hdr = 'Undefined'):
    if msgtype == 'log':
        print(f'[ {hdr} ] > {msg}')
    else:
        print(msg)
    

if __name__ == '__main__':

    username="admin"
    password="Csa@12345"
    success=0
    while success==0:
        loginuser=input("Enter username : ")
        loginpass = getpass()
        if(loginuser==username) and (loginpass==password):
            success=1
        else:
            success=0
            print("Oops! try again, incorrect username or password")



    help_str = """--------------->
list - List the Clients Connected to the Lan Monitor
peep - Peep into Clients Screen
deny_ip - Block an ip address or website in clients computer
allow_ip - Allow an ip address or website in clients computer
exit - Exit the Program
help - To list commands
--------------->"""
    try:
        main = Main()
        main.start()
        
        print(help_str)
        while True:
            temp1 = input('[ LAN MONITOR ] > ')
            if temp1 == 'list':
                if main.clients == {}:
                    printmsg(None, 'No Clients Connected !')
                else:
                    for clients in main.clients:
                        printmsg(None, clients)
                    
            elif temp1 == 'peep':
                temp2 = input('[ Client Name ] > ')
                if temp2 in main.clients.keys():
                    main.send_sig(main.clients[temp2][0],'VID') 
                    main.recv_video()
                else:
                    printmsg('log', 'Invalid', f'No Client named {temp2} !')
            
            elif temp1 == 'deny_ip':
                temp2 = input('[ Client Name ] > ')
                temp3 = input('[ Website ] > ')
                if temp2 in main.clients.keys():
                    main.deny_ip(main.clients[temp2][0], temp3)
                else:
                    printmsg('log', 'Invalid', f'No Client named {temp2} !')
                    
            elif temp1 == 'allow_ip':
                temp2 = input('[ Client Name ] > ')
                temp3 = input('[ Website ] > ')
                if temp2 in main.clients.keys():
                    main.allow_ip(main.clients[temp2][0], temp3)
                else:
                    printmsg('log', 'Invalid', f'No Client named {temp2} !')
            
            elif temp1 == 'help':
                print(help_str)
            
            elif temp1 == 'exit':
                sys.exit()
            else:
                printmsg('log', f'No command named {temp1} !, type help for more details.', 'Invalid')
    except:
        print("Server is already Online")