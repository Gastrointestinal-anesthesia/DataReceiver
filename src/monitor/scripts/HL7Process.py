import pandas as pd
from hl7parser.hl7 import HL7Message

class HL7Data:
    def __init__(self, data):
        # Encode data
        self.message = str(data, 'utf-8')[1:]
        self.DataProcess()

    def DataProcess(self):
        # Generate OBX contents
        self.finalMsg = HL7Message(self.message)

        for term in self.finalMsg.obx:
            index = str(term[2]).split('^')[1]
            value = term[4]
            if index == 'MDC_ECG_HEART_RATE':
                print(index, int(value))
                # anesthesia_msg.RATE = int(float(str(value)) * 100)
                # anesthesia_msg.RATE = anesthesia_msg.RATE / 100
            elif index == 'MDC_PRESS_CUFF_DIA':
                print(index, int(value))
                # anesthesia_msg.DIAP = int(float(str(value)) * 100)
                # anesthesia_msg.DIAP = anesthesia_msg.DIAP / 100
            elif index == 'MDC_PRESS_CUFF_SYS':
                print(index, int(value))
                # anesthesia_msg.SYSP = int(float(str(value)) * 100)
                # anesthesia_msg.SYSP = anesthesia_msg.SYSP / 100
            elif index == 'MDC_PULS_OXIM_SAT_O2':
                print(index, int(str(value)))
                # anesthesia_msg.SpO2 = int(float(str(value)) * 100)
                # anesthesia_msg.SpO2 = int(anesthesia_msg.SpO2 / 100)
            # elif index == 'MDC_BLD_PERF_INDEX':
            #     print(index, float(value))
            #     # anesthesia_msg.SaO2 = int(float(str(value)) * 100)
            #     # anesthesia_msg.SaO2 = anesthesia_msg.SaO2 / 100
            elif index == 'MNDRY_EEG_BISPECTRAL_INDEX':
                print(index, int(value))
                # anesthesia_msg.BIS = int(float(str(value)) * 100)
                # anesthesia_msg.BIS = anesthesia_msg.BIS / 100
            if value == '':
                pass
