#!/bin/bash

source devel/setup.bash
{
gnome-terminal -t "runMonitor" -x bash -c "rosrun monitor main.py"
}&

