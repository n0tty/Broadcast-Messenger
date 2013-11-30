import socket
from Tkinter import *

UDP_IP = "192.168.0.1" #Change to server IP
UDP_PORT = 5005        #Change to server port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "recvd msg:", data
    print addr

    blah = Tk()
    blah.title("LAN Broadcast Messenger")
    blah.geometry("288x325")
    app1 = Frame(blah)
    app1.grid()
    lbls = Label(app1, text = "Latest Message Recieved: ")
    lbls.grid(row = 0, column = 0, columnspan = 2, sticky = W)
    lbls1 = Label(app1, text = data)
    lbls1.grid(row = 1, column = 0, columnspan = 2, sticky = W)
    lbl1 = Label(app1, text = "\tAll rights reserved by Tanoy Bose\n\thttp://the-bose.com")
    lbl1.grid(row = 6, column = 0, columnspan = 2, sticky = W)

    blah.mainloop()
