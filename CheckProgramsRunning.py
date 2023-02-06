import pytz
import datetime
import psutil
import ctypes
import time
import threading

terminate_time = 5

# buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10


def Mbox_Warning(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, MB_OK | ICON_STOP)


#Checks the apps
blocked_app_list = [
    "Exile",
    "Counter",
    "League",
    "Building",
]


start_block_time = 6
end_block_time = 20
unblock_days = [5,6]

#while (True):
tz = pytz.timezone('America/Sao_Paulo')
my_hour = datetime.datetime.now(tz).hour
my_weekday = datetime.datetime.now(tz).weekday()

blocked_processes_running = []

for p in psutil.process_iter():
    for blocked_app in blocked_app_list:
        # print (p.name())
        if (blocked_app in p.name()):
            blocked_processes_running.append(p)

if (blocked_processes_running.count == 0):
    print ("No blocked process running")


#Check conditions
forbidden_cond_1 = (my_hour <= end_block_time or my_hour > start_block_time)
forbidden_cond_2 = (my_weekday not in unblock_days)

if (blocked_processes_running.count == 0):
    print ("No blocked process running")


if (forbidden_cond_1 and forbidden_cond_2):
    for blocked_process in blocked_processes_running:
        print ("Blocked app running: " + blocked_process.name())
        title = 'WARNING: Process [{}] is running'.format(blocked_process.name())
        text = 'Process will be terminated in [{}] seconds'.format(terminate_time)
        thread_stop = threading.Thread(target=Mbox_Warning,args=(title, text))
        thread_stop.start()
        time.sleep(terminate_time)
        blocked_process.terminate()
        print("Stopping process")
else:
    print (forbidden_cond_1)
    print (forbidden_cond_2)
    print (my_hour)
    print (end_block_time)
    print (start_block_time)
    print ("Your allowed to have fun, enjoy!")
        
    #time.sleep(60)
        