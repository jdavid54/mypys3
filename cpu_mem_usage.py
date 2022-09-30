import tkinter as tk
from tkinter import ttk
import time
# https://www.pythontutorial.net/tkinter/tkinter-after/
import psutil

class CpuMemUsage(tk.Tk):
    #attributes
    cpu_percent = (psutil.cpu_percent() / 100.0)
    mem_percent = (psutil.virtual_memory().percent / 100.0)
    cpu_thres = 0.5
    mem_thres = 0.8
    bars = 10
    
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('CPU/MEM usage at '+self.time_string())
        self.resizable(0, 0)
        self.geometry('350x80')
        self['bg'] = 'black'  # canvas color
        self.bind("<Button-1>", lambda e:self.switch_mode()) 
        
        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='white', foreground='green')
        
        # labels
        self.label = ttk.Label(self,
            text=self.cpu_plot(),
            font=('Lucida Console', 11), anchor='center', width=35)
        #self.label.place(anchor='center')

        self.mode = True   # plot with bars
        self.cpu_alert = self.cpu_percent>self.cpu_thres
        self.mem_alert = self.mem_percent>self.mem_thres
        
        self.label2 = ttk.Label(self,
            text=self.mem_plot(),
            font=('Lucida Console', 11), anchor='center', width=35) #,justify='center')
        
        self.label.pack(anchor='center',expand=True)
        self.label2.pack(expand=True)

        # schedule an update every 1 second
        self.label.after(1000, self.update)

    def time_string(self):
        return time.strftime('%H:%M:%S')
    
    def update_data(self):        
        self.cpu_percent = (psutil.cpu_percent() / 100.0)            
        self.cpu_alert = self.cpu_percent>self.cpu_thres
#         if self.cpu_alert:
#             #self.cpu_alert=True
#             self['bg'] = 'red'
#         else:
#             #self.cpu_alert=False
#             self['bg'] = 'black'
        
        self.mem_percent = (psutil.virtual_memory().percent / 100.0)
        self.mem_alert = self.mem_percent>self.mem_thres
        
    def cpu_plot(self):
        cpu_bar = '█' * int(self.cpu_percent *self.bars) + '-' * (self.bars - int(self.cpu_percent *self.bars))                
        return f"CPU usage: |{cpu_bar}| {self.cpu_percent*100:{5}.2f}%  "    
    
    def mem_plot(self): 
        mem_bar = '█' * int(self.mem_percent *self.bars) + '-' * (self.bars - int(self.mem_percent *self.bars))
        return f"MEM usage: |{mem_bar}| {self.mem_percent*100:{5}.2f}%  "

    def switch_mode(self):
        self.mode = not self.mode
    
    def reset_mode(self):
        self.geometry('350x80')
        self.label.configure(background='white',font=('Lucida Console', 11), anchor='center', width=35)   #background='white', foreground='green',             
        self.label2.configure(background='white',font=('Lucida Console', 11), anchor='center', width=35)        
                    
    def update(self):
        self.update_data()
        """ update the label every 1 second """
        self.title('CPU/MEM usage at '+self.time_string())
        self.label.configure(text=self.cpu_plot()) 
        self.label2.configure(text=self.mem_plot())
        
        if self.cpu_alert:
            self.label.configure(foreground='red')           
        else:
            self.label.configure(foreground='green')
        
        if self.mem_alert:
            self.label2.configure(foreground='orange')            
        else:
            self.label2.configure(foreground='green')
                    
        #self.display_usage()  # show in shell
        
        # schedule another timer
        if self.mode==True:
            self.reset_mode()     # return from mode Digital
            self.label.after(1000, self.update)
        else:    
            self.label.after(1000, self.update2)
        
    def update2(self):
        self.update_data()
        self.geometry('320x150')
        self['bg'] = 'black'

        """ update the label every 1 second """
        self.title('CPU/MEM usage at '+self.time_string())
        #self.label.configure(text=self.time_string())
        self.label.configure(text=f'CPU:{self.cpu_percent*100:{5}.2f}%',font=('Digital-7',30),background='black')                
        self.label2.configure(text=f'MEM:{self.mem_percent*100:{5}.2f}%',font=('Digital-7',30),background='black')
        
        if self.cpu_alert:
            self.label.configure(foreground='red')           
        else:
            self.label.configure(foreground='green')
            
        if self.mem_alert:
            self.label2.configure(foreground='orange')                       
        else:
            self.label2.configure(foreground='green')    
            
        #self.display_usage()  # show in shell
        
        # schedule another timer
        if self.mode==True:
            self.label.after(1000, self.update)
        else:    
            self.label.after(1000, self.update2)
        
    def display_usage(self):
        #self.bars=30
        #cpu_percent = (cpu_usage / 100.0)
        cpu_bar = '█' * int(self.cpu_percent*self.bars) + '-' * (self.bars - int(self.cpu_percent *self.bars))
        #mem_percent = (mem_usage / 100.0)
        mem_bar = '█' * int(self.mem_percent*self.bars) + '-' * (self.bars - int(self.mem_percent *self.bars))
        print(f"\rCPU usage: |{cpu_bar}| {self.cpu_percent*100:{5}.2f}%  ",end="")
        print(f"MEM usage: |{mem_bar}| {self.mem_percent*100:{5}.2f}%  ", end="")

if __name__ == "__main__":
    usage = CpuMemUsage()
    usage.mainloop()
