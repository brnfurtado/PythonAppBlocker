import pytz
import datetime
import psutil
import ctypes
import time
import threading
import json
import os

current_dir = os.path.dirname(__file__)

# Construct the file path for the JSON file
file_path = os.path.join(current_dir, 'params.json')

# Open the JSON file and load its contents
with open(file_path, 'r') as file:
    data = json.load(file)

blocked_apps = data["blocked_apps"]
allowed_days = data["allowed_days"]
start_block_hour = data["start_block_hour"]
end_block_hour = data["end_block_hour"]
timezone = pytz.timezone(data["timezone"])
terminate_time = 30

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

my_hour = datetime.datetime.now(timezone).hour
my_weekday = datetime.datetime.now(timezone).weekday()

blocked_processes_running = []

for p in psutil.process_iter():
    for blocked_app in blocked_apps:
        # print (p.name())
        if (blocked_app in p.name()):
            blocked_processes_running.append(p)

#Check conditions
forbidden_cond_1 = (my_hour <= end_block_hour)
forbidden_cond_2 = (my_hour >= start_block_hour)
forbidden_cond_3 = (my_weekday not in allowed_days)


if (forbidden_cond_1 and forbidden_cond_2 and forbidden_cond_3):
    if (len(blocked_processes_running) == 0):
        print ("No blocked process running")

    else:
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
    print ("Your allowed to have fun, enjoy!")
        
    #time.sleep(60)
        