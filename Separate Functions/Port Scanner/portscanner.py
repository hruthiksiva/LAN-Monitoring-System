import socket

target = '103.58.116.134'

def portscan(port):
	try:
		socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((target,port))
		return True
	except:
		return False
print(portscan(80))
