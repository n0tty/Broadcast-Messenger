import socket
from Tkinter import *
/*

  Broadcast Messenger by n0tty\n
  legendtanoybose@gmail.com
  http://the-bose.com
  
__________                     
\\______   \\ ____  ______ ____  
 |    |  _//  _ \\/  ___// __ \\ 
 |    |   (  <_> )___ \\\\  ___/ 
 |______  /\\____/____  >\\___  >
        \\/           \\/     \\/ 
        
*/

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Please input the ip, port and message you would like\nto broadcast and click \"Send the Message\" button")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.udpip_lbl = Label(self, text = "IP")
        self.udpip_lbl.grid(row = 1, column = 0, sticky = W)
        self.udpip_ent = Entry(self)
        self.udpip_ent.grid(row = 1, column = 1, sticky = W)

        self.udpport_lbl = Label(self, text = "Port")
        self.udpport_lbl.grid(row = 2, column = 0, sticky = W)
        self.udpport_ent = Entry(self)
        self.udpport_ent.grid(row = 2, column = 1, sticky = W)
        
        self.msg_lbl = Label(self, text = "Message")
        self.msg_lbl.grid(row = 3, column = 0, sticky = W)
        self.msg_ent = Entry(self)
        self.msg_ent.grid(row = 3, column = 1, sticky = W)
        self.send_btn = Button(self, text = "Send the Message", command = self.msg_send)
        self.send_btn.grid(row = 4, column = 0, sticky = W)
        self.srvr_txt = Text(self, width = 35, height = 10, wrap = WORD)
        self.srvr_txt.grid(row = 5, column = 0, columnspan = 2, sticky = W)

        self.inst_lbl1 = Label(self, text = "\tAll rights reserved by Tanoy Bose\n\thttp://the-bose.com")
        self.inst_lbl1.grid(row = 6, column = 0, columnspan = 2, sticky = W)


    def msg_send(self):
        global MESSAGE
        global UDP_IP
        global UDP_PORT
        MESSAGE = self.msg_ent.get()
        print MESSAGE

        self.srvr_txt.delete(0.0, END)
        self.srvr_txt.insert(0.0, "Last Broadcast Information")
        self.srvr_txt.insert(END, "\nMessage: ")
        self.srvr_txt.insert(END, MESSAGE)

        UDP_IP = self.udpip_ent.get()
        UDP_PORT = int(self.udpport_ent.get())
        #UDP_IP = "127.0.0.1"
        #UDP_PORT = 5005

        self.srvr_txt.insert(END, "\nServer IP: ")
        self.srvr_txt.insert(END, UDP_IP)
        self.srvr_txt.insert(END, "\nBroadcast Port: ")
        self.srvr_txt.insert(END, UDP_PORT)

        print "UDP target IP:", UDP_IP
        print "UDP target port:", UDP_PORT
        print "message:", MESSAGE

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))



#main
server = Tk()
server.geometry("288x325")
server.title("Message Broadcast Server")
app = Application(server)

server.mainloop()
