from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags
from bluez_peripheral.gatt.descriptor import descriptor, DescriptorFlags as DescFlags

import time

# Define a service like so.
class Read_Service(Service):
   def __init__(self):
      self.msg_to_send= ""
      # Call the super constructor to set the UUID.
      super().__init__("BEEE", True) 
   
   #Use the characteristic decorator to define your own characteristics.
   #Set the allowed access methods using the characteristic flags.
   @characteristic("BEF0", CharFlags.READ)
   def my_readonly_characteristic(self, options):
      # Characteristics need to return bytes.
      return bytes(self.msg_to_send, "utf-8")

   # Associate a descriptor with your characteristic like so.
   # Descriptors have largely the same flags available as characteristics.
   @descriptor("BEF2", my_readonly_characteristic, DescFlags.READ)
   # Alternatively you could write this:
   #@my_writeonly_characteristic.descriptor("BEF2", DescFlags.READ)
   def my_readonly_descriptors(self, options):
      # Descriptors also need to handle bytes.
      return bytes("This characteristic is completely pointless!", "utf-8")



