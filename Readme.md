# Python program blocker

## Introduction
The project consists of a Python Application that allow users to block certain Apps the designated time.
It was developed during the 2019 pandemic where most people had to migrate to a homeoffice enviroment,
thus providing a challenge to guarantee focus and productivity during the working hours.
Hope this project can help anyone struggling to maintain focus or a defined work schedule during
homeoffice.

## Usage
All parameters are set in the json file "params.json", which the user can set accordingly.
Further explanation on each parameter below.

### Blocked Apps
Defines which programs are blocked. The program searches for programs that contains the names 
described and automatically shuts them down if they are turned on during the blocked time.

### Allowed days
Defines the parameters for what days the program ignores, by default set for values 5 and 6 
which are saturday and sunday.

### Start and End block time
Defines the start of the block time and the end of the block time, which are by default 6 and 20 (hour).

### Timezone
User timezone, by default is set to "America, Sao Paulo", which is BRZ, or GMT - 3.


## Setup
The user should set in the Windows "Task Scheduler" a task which executes the installed python
path, with the extra parameter of "main.py", and starting on the installed project location.