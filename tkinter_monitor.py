import time
import psutil
# importing everything from tkinter
from tkinter import *
# https://stackoverflow.com/questions/27123676/how-to-update-python-tkinter-window
# https://web.archive.org/web/20201112030233/http://effbot.org/tkinterbook/widget.htm#Tkinter.Widget.after-method
# https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/

# Creating App class which will contain
# Label Widgets
class App:
    def __init__(self, master) -> None:
  
        # Instantiating master i.e toplevel Widget
        self.master = master
  
        # Creating first Label i.e with default font-size
        Label(self.master, text="I have default font-size").pack(pady=20)
  
        # Creating second label
        # This label has a font-family of Arial
        # and font-size of 25
        Label(self.master,
              text="I have a font-size of 25",
  
              # Changing font-size here
              font=("Arial", 25)
              ).pack()
def test():  
    # Instantiating top level
    root = Tk()

    # Setting the title of the window
    root.title("Change font-size of Label")

    # Setting the geometry i.e Dimensions
    root.geometry("400x250")

    # Calling our App
    app = App(root)

    # Mainloop which will cause this toplevel
    # to run infinitely
    root.mainloop()

debug = False
last_rcv = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_rcv + last_sent

def get_data():
    global last_rcv, last_sent, last_total
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
    if debug:
        print(s)
    
    last_rcv = bytes_rcv
    last_sent = bytes_sent
    last_total = bytes_total
    
    #time.sleep(1)
    return s


# variable
#my_text = "GeeksforGeeks updated !!!"
# function define for
# updating the my_label
# widget content
def counter():
    # use global variable
    global my_text
    my_text = get_data()
    # configure
    my_label.config(text = my_text)
    Main_window.after(1000, counter)
# 
# def update():
#     l.config(text=str(random.random()))
#     root.after(1000, update)

# root = tk.Tk()
# l = tk.Label(text='0')
# l.pack()
# root.after(1000, update)
# root.mainloop()

def close():
    Main_window.destroy()
 
# creating the tkinter window
Main_window = Tk()
Main_window.geometry("600x240")
Main_window.resizable(False, False)
Main_window.title('Bandwidth Monitor')
#Main_window.config(bg='#84BF04')

# create a button widget and attached
# with counter function
# my_button = Button(Main_window,
#             text = "Please update",
#             command = counter)

# create a Label widget
my_label = Label(Main_window,
            text = "Starting ....",height=8, font=("Arial", 16))

# place the widgets
# in the gui window
my_label.pack()
#my_button.pack()
button = Button(Main_window, text = 'Close the window', command = Main_window.destroy)
button.pack()

# Start update function
counter()

# Start the GUI after a delay with callback function
#Main_window.after(1000, counter)


# Start the GUI infinite loop
#Main_window.mainloop()


# while True:
#     my_text = get_data()
#     counter()
#     time.sleep(1)

#Main_window.destroy()