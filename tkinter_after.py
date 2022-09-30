import tkinter as tk
from tkinter import ttk
import time
# https://www.pythontutorial.net/tkinter/tkinter-after/

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter after() Demo')
        self.geometry('300x100')

        self.style = ttk.Style(self)

        self.button = ttk.Button(self, text='Wait 3 seconds')
        self.button['command'] = self.start
        self.button.pack(expand=True, ipadx=10, ipady=5)

    def start(self):
        print('start')
        self.change_button_color('red')
        #self.configure(bg = 'red')
        #time.sleep(3)                        # sleep stops the main thread
        #self.change_button_color('black')    # so update only after the sleep time
        
        # using after don't stop main thread
        self.after(3000,lambda: self.change_button_color('black'))
        
        # change window background color 2 sec later
        self.after(5000,lambda: self.configure(bg = 'blue'))   

    def change_button_color(self, color):  # change button foreground
        self.style.configure('TButton', foreground=color)
        print(color)


if __name__ == "__main__":
    app = App()
    app.mainloop()