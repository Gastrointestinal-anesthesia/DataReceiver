from hl7parser.hl7 import HL7Message


class HL7Data:
    def __init__(self, data):
        # Encode data
        self.message = str(data, 'utf-8')[1:]
        # Generate OBX contents
        self.finalMsg = HL7Message(self.message)

        self.itemDict = {
            'MDC_PULS_OXIM_PULS_RATE': -1,
            'MDC_ECG_HEART_RATE': -1,
            'MDC_PRESS_CUFF_DIA': -1,
            'MDC_PRESS_CUFF_SYS': -1,
            'MDC_PULS_OXIM_SAT_O2': -1,
            'MNDRY_EEG_BISPECTRAL_INDEX': -1,
        }

        self.DataProcess()

    def DataProcess(self):

        for term in self.finalMsg.obx:
            index = str(term[2]).split('^')[1]
            value = str(term[4])
            if index not in self.itemDict:
                continue
            self.itemDict[index] = int(float(value))
            if value == '':
                pass

    def GetItemDict(self):
        return self.itemDict
