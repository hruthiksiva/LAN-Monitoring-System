import tkinter as tk
from tkinter import filedialog,Text
import os

root=tk.Tk()
apps=[]

if os.path.isfile('save.txt'):
	with open('save.txt','r') as f:
		tempApps = f.read()
		tempApps=tempApps.split(',')
		apps=[x for x in tempApps if x.strip()]


def addApp():

	for widget in frame.winfo_children():
		widget.destroy()

	filename=filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("Executables","*.exe"),("All Files","*.*")))
	apps.append(filename)
	print(apps)
	for app in apps:
		label=tk.Label(frame,text=app,bg="gray")
		label.pack()

	
def runApps():
	for app in apps:
		os.startfile(app)

canvas=tk.Canvas(root, height=600,width=600,bg="#FFFFFF")
canvas.pack()

frame=tk.Frame(root,bg="black")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openFile = tk.Button(root,text="Open File",padx=10,pady=5,command=addApp)
openFile.pack()

runApps = tk.Button(root,text="Run Apps",padx=10,pady=5,command=runApps)
runApps.pack()

for app in apps:
	label=tk.Label(frame,text=app)
	label.pack()

root.mainloop()

with open('save.txt','w') as f:
	for app in apps:
		f.write(app+',')

		