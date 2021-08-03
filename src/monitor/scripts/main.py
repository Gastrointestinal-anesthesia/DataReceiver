#!/usr/bin/env python3

import MonitorSocket
import HL7Process
import MonitorPublisher

MonitorSocket1 = MonitorSocket(7890)

if __name__ == "__main__":
    try:
        DataRecord()
    except Exception as e:
        print(repr(e))
