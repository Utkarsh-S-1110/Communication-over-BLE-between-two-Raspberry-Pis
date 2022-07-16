from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags
from bluez_peripheral.gatt.descriptor import descriptor, DescriptorFlags as DescFlags

import time

# Define a service like so.
class Write_Service(Service):
    def __init__(self):
        self._write_value = None
        # Call the super constructor to set the UUID.
        super().__init__("BEEF", True)
        
 
    # This is a write only characteristic.
    @characteristic("BEF1", CharFlags.WRITE)
    def my_writeonly_characteristic(self, options):
        # This function is a placeholder.
        # In Python 3.9+ you don't need this function (See PEP 614)
        pass

    # In Python 3.9+:
    @my_writeonly_characteristic.setter
    # Define a characteristic writing function like so.
    def my_writeonly_characteristic(self, value, options):
        self._write_value = value
        
      

    # Associate a descriptor with your characteristic like so.
    # Descriptors have largely the same flags available as characteristics.
    @my_writeonly_characteristic.descriptor("BEF3", DescFlags.READ)
    def my_readonly_descriptors(self, options):
        # Descriptors also need to handle bytes.
        return bytes("This characteristic is completely pointless too!", "utf-8")

    def getNewData(self):
        return self._write_value
        