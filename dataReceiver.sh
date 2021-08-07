#!/bin/bash

source devel/setup.bash

cd src/monitor/scripts
chmod 777 main.py

{
gnome-terminal -t "runMonitor" -x bash -c "rosrun monitor main.py"
}&

