#!/usr/bin/env python3

import MonitorSocket
import HL7Process
import MonitorPublisher

MonitorSocket1 = MonitorSocket.MonitorSocket(7890)
MonitorPublisher1 = MonitorPublisher.MonitorPublisher()

if __name__ == "__main__":
    while True:
        try:
            MonitorData1 = HL7Process.HL7Data(MonitorSocket1.ReceiveAPackage())
            MonitorPublisher1.AddMsg(MonitorData1)
        except Exception as e:
            print(repr(e))
