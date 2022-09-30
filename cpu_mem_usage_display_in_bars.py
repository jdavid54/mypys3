import psutil
import time

def test():
    while True:
        print(psutil.cpu_percent())
        print(psutil.virtual_memory().percent)
        time.sleep(5)

#test()

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent *  bars) + '-' * (bars - int(cpu_percent *  bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent *  bars) + '-' * (bars - int(mem_percent *  bars))
    
    '''
    f'{value:{width}.{precision}}'
    where:

    value is any expression that evaluates to a number
    width specifies the number of characters used in total to display, but if value needs more space than the width specifies then the additional space is used.
    precision indicates the number of characters used after the decimal point
    '''
    
    print(f"\rCPU usage: |{cpu_bar}| {cpu_usage:{5}.2f}%  ",end="")
    print(f"MEM usage: |{mem_bar}| {mem_usage:{5}.2f}%  ", end="")
   
while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent,20)
    time.sleep(0.5)
