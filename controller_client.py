import socket
import directkeys

ip = "192.168.11.128"
port = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))

keys = [directkeys.D, directkeys.S, directkeys.W, directkeys.A, directkeys.SPACE, directkeys.ESC]

while True:
    data, addr = s.recvfrom(1024)
    x = data.decode()
    for i in range(len(x)):
        if(x[i] == "1"):
            directkeys.PressKey(keys[i])
        else:
            directkeys.ReleaseKey(keys[i])
    #print(x)
