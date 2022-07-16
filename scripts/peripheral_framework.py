from ble_peripheral import BLE_Peripheral

import asyncio

class central_framework:

   def __init__(self):
      self.ble_peripheral_obj = BLE_Peripheral()

# This method starts the advertisement.
# It takes in two parameters as input.
# device_name (The name that you want other devices to view you by) and time_out (duration (in seconds) for which the device should advertise itself).
# Returns True if advertisment has started successfully, otherwise returns False.
   def advertise(self,device_name = "PeripheralDev",time_out = 180):
      return self.ble_peripheral_obj.loop.run_until_complete(self.ble_peripheral_obj.addToServiceCollection(device_name,time_out))

# Checks for new message from the Central device (for a minute) and returns it.
# If it recieves no new command within a minute, it returns the None object.     
   def read(self):
      return self.ble_peripheral_obj.loop.run_until_complete(self.ble_peripheral_obj.call_read())

# Writes the message (taken as input) to the Central device.
   def write(self,response):
      return self.ble_peripheral_obj.loop.run_until_complete(self.ble_peripheral_obj.call_write(response))      

# Shut down the Peripheral.
   def exit(self):
      self.loop.ble_peripheral_obj.run_until_complete(self.ble_peripheral_obj.call_wait())
      self.loop.ble_peripheral_obj.close()
      exit()



### EXAMPLE SNIPPET ###      




obj= central_framework()
if obj.advertise("Pi2Pi_Dev",120):
   print("Ready to recieve")
   for l in range(3):
      recieve = obj.read()
      if not (recieve == None):
         obj.write("Recieved: "+ recieve )
else:
   print("Could not start Advertising")
obj.exit()
