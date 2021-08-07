#!/bin/bash

source devel/setup.bash
<<<<<<< HEAD
cd src/monitor/scripts
chmod 777 main.py
=======
>>>>>>> main
{
gnome-terminal -t "runMonitor" -x bash -c "rosrun monitor main.py"
}&

