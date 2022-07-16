from bluez_peripheral.gatt.service import ServiceCollection
from bluez_peripheral.util import *
from bluez_peripheral.advert import Advertisement

from write_Service import Write_Service
from read_Service import Read_Service

import asyncio
import time


class BLE_Peripheral:

   def __init__(self):
      self.latest_id = 0
      self.loop = asyncio.get_event_loop()

   async def addToServiceCollection(self,name,my_timeout):
      try:
         # This needs running in an awaitable context.
         self.bus = await get_message_bus()
         self.bus2 = await get_message_bus()

         # Instance and register your service.
         self.service = Write_Service()
         self.service2 = Read_Service()

         await (self.service).register(self.bus)
         await (self.service2).register(self.bus2)

         self.adapter = await Adapter.get_first(self.bus)
         self.adapter2 = await Adapter.get_first(self.bus2)

         # The services that we're advertising. BEEF is write char. and BEEE is read char.
         my_service_ids = ["BEEF","BEEE"]
         # The appearance of my service. 
         my_appearance = 0 
         self.advert = Advertisement(name, my_service_ids, my_appearance, my_timeout)
         await self.advert.register(self.bus, self.adapter)
         await self.advert.register(self.bus2, self.adapter2)

      except :
         return False
      await asyncio.sleep(0.010)
      return True              

   async def call_read(self):
      start_time = time.time()
      split_list=[]
      while True: 
         if int (time.time()-start_time) > 120 :
            return(None)
         if (self.service).getNewData() == None:
            await asyncio.sleep(0.010)
            continue
         data_rec =self.service.getNewData().decode('utf-8')
         try:
            split_list= data_rec.split(";", 1)
            if not (split_list[0] == str(self.latest_id)):
               self.latest_id+=1
               return split_list[1]
         except:
            pass
         await asyncio.sleep(0.010)

   async def call_write(self,response):
      try:
         await asyncio.sleep(0.010)
         self.service2.msg_to_send = str(self.latest_id)+";"+response
         return True
      except :
         return False       

   async def call_wait(self):
      await asyncio.sleep(5)


