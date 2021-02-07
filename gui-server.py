#imports
from tkinter import *
import socket, cv2
from vidgear.gears import NetGear
from pickle import dumps, loads
import threading


#functions
class Main():
    ids = {}
    clients ={}
    
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
    #gui settings
    root=Tk()
    root.title("LAN Monitoring System")
    root.geometry('500x500')
    main = Main()
    main.start()

    #button listener functions
    def peepclient():
        temp2 = input('[ Client Name ] > ')
        if temp2 in main.clients.keys():
            main.send_sig(main.clients[temp2][0],'VID') 
            main.recv_video()
        else:
            printmsg('log', 'Invalid', f'No Client named {temp2} !')
    def denyip():
        pass

    def allowip():
        pass

    def help():
        helplab=Label(root,text="""list - List the Clients Connected to the Lan Monitor
peep - Peep into Clients Screen
deny_ip - Block an ip address or website in clients computer
allow_ip - Allow an ip address or website in clients computer
exit - Exit the Program
help - To list commands""",justify=LEFT).place(x=150,y=280)

    def exit():
        root.destroy()

    def listclient():
        var = StringVar()
        result=""
        label=Label(root,textvariable=var).place(x=150,y=100)
        for i in main.clients:
            result= result + " "+i
        var.set("Client List : "+result)
        if main.clients == {}:
            var.set("No clients connected")
        else:
            for i in main.clients:
                result= result + " "+i
        var.set("Client List : "+result)

#peep button
    peep=Button(root,text="Peep",command=peepclient)
    peep.place(x=10,y=40)

#list clients
    list=Button(root,text="List",command=listclient)
    list.place(x=10,y=100)


#deny ip
    denyip=Button(root,text="Deny IP",command=denyip)
    denyip.place(x=200,y=160)
    denytxt = Text(root, height=1,width=20)
    denytxt.place(x=10, y=160)

#allow ip
    allowip=Button(root,text="Allow IP",command=allowip)
    allowip.place(x=400,y=160)


#help button
    help=Button(root,text="Help",command=help)
    help.place(x=10,y=280)

#exit button
    exit=Button(root,text="Exit",command=exit)
    exit.place(x=10,y=340)

    root.mainloop()