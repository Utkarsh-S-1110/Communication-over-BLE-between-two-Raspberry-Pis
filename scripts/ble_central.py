from bluepy.btle import DefaultDelegate
from bluepy import btle
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

class BLE_Central:
    def __init__(self):
        self.dev = None
    def find_services(self):
        try:
            uuidConfig = btle.UUID(0xBEEF)
            WriteService = (self.dev).getServiceByUUID(uuidConfig)
            self.writeChar = WriteService.getCharacteristics()[0]
        except btle.BTLEDisconnectError:
            return False
        time.sleep(1.0) # Allow sensor to stabilise
        try:
            uuidConfig = btle.UUID(0xBEEE)
            readService = self.dev.getServiceByUUID(uuidConfig)
            self.readChar = readService.getCharacteristics()[0]
            
        except btle.BTLEDisconnectError:
            return False
        time.sleep(1.0) # Allow sensor to stabilise 
        return True

  

