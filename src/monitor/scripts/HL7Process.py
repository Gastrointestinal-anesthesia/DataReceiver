import pandas as pd
from hl7parser.hl7 import HL7Message

class HL7Data:
    def __init__(self, data):
        # Encode data
        self.message = str(data, 'utf-8')
        self.li = self.message.split('\r')
        if '' in self.li:
            self.li.remove('')
