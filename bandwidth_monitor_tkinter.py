import time
import psutil
import tkinter
#https://docs.python.org/3/library/tkinter.html
from tkinter import messagebox
from tkinter import Tk, Text



# This code is to hide the main tkinter window
def test_box():
    root = Tk()
    root.withdraw()
    # Message Box
    messagebox.showinfo("Title", "Message")

def alert(title, msg):
    #root = tkinter.Tk()
    #root.withdraw()
    messagebox.showinfo(title, msg)
    
def alertDayInfo(s):
    
    #alert('Day info', s);
    tk_show(s, 'Today info')

def alertAbout():
    alert('About', ABOUT);


def tk_show(s, title="Month calendar"):
#     root = Tk()
#     root.geometry("600x140")
#     root.resizable(False, False)
#     root.title(title)
    text = Text(root, height=8)
    #text.pack()
    #text.insert('2.0', s)
    l1 = tkinter.Label(text=s, fg="black", bg="white")
    #l2 = tkinter.Label(text="Test", fg="black", bg="white")
    l1.pack()
    #l2.pack()
    root.mainloop()

title="Month calendar"
root = Tk()
root.geometry("600x140")
root.resizable(False, False)
root.title(title)

last_rcv = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_rcv + last_sent

while True:
    bytes_rcv = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_rcv + bytes_sent

    new_rcv = bytes_rcv - last_rcv
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total
    
    mb_new_rcv = new_rcv / 1024 /1024
    mb_new_sent = new_sent / 1024 /1024
    mb_new_total = new_total / 1024 /1024

    s = f"{mb_new_rcv:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total"
    #print(f"{mb_new_rcv:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")
    print(s)
    alertDayInfo(s)
    
    last_rcv = bytes_rcv
    last_sent = bytes_sent
    last_total = bytes_total
    
    time.sleep(1)
