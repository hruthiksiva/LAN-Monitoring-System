# -*- coding: utf-8 -*-

import socket
from vidgear.gears import ScreenGear
from vidgear.gears import NetGear
from pickle import dumps, loads
import threading

class Main():
    ids = {}
    
    def __init__(self, port = 12350):
        self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.port = port
        
        
    def start(self, name = 'unknown'):
        self.sock.connect(('localhost', self.port, 0, 0))
        self.sock.send(name.encode())
        self.recv_sig()
        
    def send_sig(self, sig):
        self.sock.send(sig.encode())
        
    def recv_sig(self):
        def inner():
            while True:
                sig = self.sock.recv(1024).decode()    
                print(sig)
                if sig == 'VID':
                    self.send_video()
                elif 'DENY' in sig :
                    self.deny_ip(sig[5:])
                elif 'ALLOW' in sig :
                    self.deny_ip(sig[6:])
                elif sig == 'CHAT':
                    pass
        self.ids['recv_sig'] = threading.Thread(target=inner)
        self.ids['recv_sig'].start()
            
    def send_video(self, port = 54321):
        def inner(port):
            stream = ScreenGear().start()
            server = NetGear(port=str(port), protocol="tcp")
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
        self.ids['send_video'] = threading.Thread(target=inner, args=(port,))
        self.ids['send_video'].start()
        
    def deny_ip(self, website = None):
        with open(HOSTS_PATH, 'r+') as file: 
            content = file.read()
            if website in content: 
                pass
            else: 
                file.write(f'{REDIRECT_IP} {website}\n')
    
    def allow_ip(self, website = None):
        with open(HOSTS_PATH, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not website in line: 
                    file.write(line)
            file.truncate()
            
if __name__ == '__main__':
    REDIRECT_IP = '127.0.0.1'
    #HOSTS_PATH = '/etc/hosts'
    HOSTS_PATH = 'C:\Windows\System32\drivers\etc\hosts'

    main = Main()
    
    temp1 = input('[ NAME ] > ')
    main.start(temp1)

    while True:
        temp1 = input('[ LAN MONITOR CLI] > ')