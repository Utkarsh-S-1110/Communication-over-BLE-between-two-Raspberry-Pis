from ble_central import BLE_Central
from ble_central import ScanDelegate
from bluepy import btle
from bluepy.btle import Scanner

import time

class central_framework:
    def __init__(self):
        self.ble_central_obj = BLE_Central()
        # To check for new message
        self.unique_id = 1

# Returns a list of the MAC addresses (as Strings) of all available BLE devices.
# Takes duration (in seconds) of the scanning process as parameter.
    def show_all_devices(self,timer=10):
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(timer)
        mac_Address = []
        for device in devices:
            mac_Address.append([device.addr])
        return mac_Address  

# Connects to the required device.
# Give the MAC address of the device you want to connect to as input parameter.
# If it successfully connects to the peripheral and finds it services, it will return True.
# Otherwise returns False.

    def connect(self,mac_Address):
        repeat = True
        start_time =time.time()
        while repeat:
            check_time = time.time()
            if int((check_time-start_time)/60) > 2:
                return False
            repeat=False
            try:
                self.dev = btle.Peripheral(mac_Address) 
            except btle.BTLEDisconnectError :
                repeat=True   
        time.sleep(1)
        return self.ble_central_obj.find_services()        

# Sends your message (length of string <= 15) to the connected peripheral and waits for the reply.
# Returns the String it recieves as a response from the peripheral.
# Returns None object if peripheral is disconnected before the central can read from it.

    def send(self,msg):
        v1= str(self.unique_id) + ";" + msg
        try:
            self.writeChar.write(bytes(v1, encoding='utf8'),True)
        except btle.BTLEGattError:
            return "Bluetooth command failed"
        response_list = [None,None]
        while not (response_list[0] == str(self.unique_id)):
            time.sleep(0.010)
            try:
                response = self.readChar.read().decode('utf-8')
                response_list=response.split(";",1)
            except btle.BTLEGattError:
                pass
            except btle.BTLEDisconnectError:
                return None                    
            
            
        self.unique_id+=1
        if self.unique_id > 9999 :
            self.unique_id=1
        return response_list[1]    



 ### EXAMPLE SNIPPET ###      
                


obj = central_framework()
all_devices = obj.show_all_devices()
print("The following Devices were found :")
for cnt,i in enumerate(all_devices):
    print(cnt,": ",i)
inp = input("Enter the index of the MAC address you want to connect to:")
print("Connecting to "+all_devices[int(inp)])
if obj.connect(all_devices[int(inp)]):
    print("Connected to peripheral")
    print(obj.send("Utkarsh"))
    print(obj.send("Amogh"))
    print(obj.send("Akshay"))
else:
    print("Could not connect")     