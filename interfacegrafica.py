import tkinter as tk
from tkinter import TOP, BOTH, X, N, LEFT, RIGHT, E, NE, NW, Y, VERTICAL
import os
import subprocess
import nmap

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.tcp_ou_udp()

    def tcp_ou_udp(self):
        self.L1 = tk.Label(text="IP do host ou rede: ")
        self.L1.pack(anchor=NW, padx=5, pady=5)
        self.E1 = tk.Entry()
        self.E1.pack(fill=X, padx=5)

        self.L2 = tk.Label(text="A partir da porta: ")
        self.L2.pack(anchor=NW, padx=5, pady=5)
        self.E2 = tk.Entry()
        self.E2.pack(fill=X, padx=5)

        self.L3 = tk.Label(text="Ate a porta: ")
        self.L3.pack(anchor=NW, padx=5, pady=5)
        self.E3 = tk.Entry()
        self.E3.pack(fill=X, padx=5)

        self.TCP = tk.IntVar()
        self.TCPcb = tk.Checkbutton(self)
        self.TCPcb["text"] = "TCP"
        self.TCPcb["variable"] = self.TCP
        self.TCPcb.pack(side=TOP)

        self.UDP = tk.IntVar()
        self.UDPcb = tk.Checkbutton(self)
        self.UDPcb["text"] = "UDP"
        self.UDPcb["variable"] = self.UDP
        self.UDPcb.pack(side=TOP)

        self.show = tk.Button(self, text="SHOW", bg="blue", fg="white", command=self.check_var)
        self.show.pack(side="bottom", fill=X)

        self.quit = tk.Button(self, text="QUIT", bg="red", fg="white", command=self.master.destroy)
        self.quit.pack(side="bottom", fill=X)
        
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def check_var(self):
        self.tcp = self.TCP.get()
        self.udp = self.UDP.get()
        ip = self.E1.get()
        inicio = self.E2.get()
        fim = self.E3.get()
        rang =  "{0}-{1}".format(inicio, fim)
        nm = nmap.PortScanner()
        nm.scan(ip, rang)
        lista_hosts = nm.all_hosts()

        listbox = tk.Listbox(self.master, yscrollcommand=self.scrollbar.set)

        for host in lista_hosts:
            listbox.insert(tk.END, '----------------------------------------------------')
            string = 'Host : %s (%s)' % (host, nm[host].hostname())
            listbox.insert(tk.END, string)
            string = 'State : %s' % (nm[host].state())
            listbox.insert(tk.END, string)
            if (self.tcp) and (self.udp):
                for proto in nm[host].all_protocols():
                    listbox.insert(tk.END,'-----------------')
                    string = 'Protocol : %s' % proto
                    listbox.insert(tk.END, string)
                    lport = nm[host][proto].keys()
                    for port in lport:
                        listbox.insert(tk.END,'----------')
                        string = 'port : %s' %(port)
                        listbox.insert(tk.END, string)
                        string = 'name : %s' %(nm[host][proto][port]['name'])
                        listbox.insert(tk.END, string)

            if (self.tcp) and (not self.udp):
                for port in nm[host].all_tcp():
                    listbox.insert(tk.END,'----------')
                    string = 'port : %s' %(port)
                    listbox.insert(tk.END, string)
                    string = 'name : %s' %(nm[host]["tcp"][port]['name'])
                    listbox.insert(tk.END, string)

            elif (not self.tcp) and (self.udp):
                for port in nm[host].all_udp():
                    listbox.insert(tk.END,'----------')
                    string = 'port : %s' %(port)
                    listbox.insert(tk.END, string)
                    string = 'name : %s' %(nm[host]["udp"][port]['name'])
                    listbox.insert(tk.END, string)

  
        listbox.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.scrollbar.config(command=listbox.yview)
                
root = tk.Tk()
root.geometry("400x500+300+300")
app = Application(master=root)
app.mainloop()