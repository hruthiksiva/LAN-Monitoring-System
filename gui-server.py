from tkinter import *
import socket, cv2, sys
from vidgear.gears import NetGear
from pickle import dumps, loads
import threading

root=Tk()
root.title("LAN Monitoring System")
root.geometry('500x500')

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

clients=[]

#list
def listclient():
    global clients
    var = StringVar()
    result=""
    label=Label(root,textvariable=var).place(x=40,y=130)
    for i in clients:
        result= result + " "+i
    var.set("Client List : "+result)
  
def peepclient():
    temp2 = int(input('Enter you client ID =>'))
    send_signal(clients[temp2][1]) 
    threading.Thread(target=recv_video).start()
    pass


btn=Button(root,text="List",command=listclient)
btn.grid(column=1,row=0)

peep=Button(root,text="Peep",command=peepclient)
peep.place(x=10,y=40)


root.mainloop()