import time
import psutil

last_rcv = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_rcv + last_sent
rcv_total = 0
sent_total = 0
total_rcv = 0

while True:
    bytes_rcv = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_rcv + bytes_sent

    new_rcv = bytes_rcv - last_rcv
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total
    rcv_total += new_rcv
    
    
    mb_new_rcv = new_rcv / 1024 /1024
    mb_new_sent = new_sent / 1024 /1024
    mb_new_total = new_total / 1024 /1024
    mb_rcv_total = rcv_total / 1024 / 1024
    mb_sent_total = sent_total / 1024 / 1024
    sent_total += mb_new_rcv
    
    print(f"{mb_new_rcv:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total",end=' (Cumul:')
    print(f"rcv:{mb_rcv_total:.2f} MB, sent:{mb_sent_total:.2f} MB)")
    
    last_rcv = bytes_rcv
    last_sent = bytes_sent
    last_total = bytes_total
    
    
    time.sleep(1)
