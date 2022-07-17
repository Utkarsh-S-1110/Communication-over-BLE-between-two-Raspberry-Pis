# Communication-over-BLE-between-two-Raspberry-Pis
## Work in Progress
## Overview
This project provides a framework to use simple functions to convert your Raspberry Pis into Central and Peripheral devices and to read and write data between them.
## Functionality
There are wide ranges of applications for exchanging data between two devices over Bluetooth Low Energy. <br />
This can be used as a part of a larger project like, maybe you have installed multiple Raspberry Pis in a large facility and are continuously sending data to the cloud through different WiFi connections. If one of them is unable to connect to its WiFi network, it could share its data locally with another Pi over B.L.E and ask it to send both of their data to the cloud. Or you could try something simpler like, just controlling your Pi project through your laptop.
### You get the following functionality with the framework scripts:
For the Central Device use the functions in the central_framework.py script. <br /> 
It makes use of the bluepy module. [Click here](https://github.com/IanHarvey/bluepy) to know more. <br />
1) **show_all_devices()**
Returns a list of the MAC addresses of all available BLE devices. <br />
2) **connect()**
Connects to the required device. <br />
3) **send()**
Sends your message to the connected peripheral and waits for the reply. <br />
###
For the Peripheral Device use the functions in the peripheral_framework.py script. <br /> 
It makes use of the  bluez-peripheral library. [Click here](https://github.com/spacecheese/bluez_peripheral) to know more. <br />
1) **advertise()**
This method starts the advertisement of your device.<br />
2) **read()**
Checks for a new message from the Central device.<br />
3) **write()**
Writes a message to the Central device.<br />
4) **exit()**
Shuts down the Peripheral.<br />
## Run Locally
Install the following Bluetooth packages/libraries -
1) **Bluez** <br />
We will follow instructions from this [instructables](https://www.instructables.com/Control-Bluetooth-LE-Devices-From-A-Raspberry-Pi/). <br /> 
     - Download the desired version of X.XX.tar.xz from [here](https://www.kernel.org/pub/linux/bluetooth/) (where X.XX is the version).
     - On the terminal run (change X.XX for your version):<br /><br />
       ```cd ~; wget https://www.kernel.org/pub/linux/bluetooth/bluez-X.XX.tar.xz```<br /><br />
       ```tar xvf bluez-X.XX.tar.xz```<br /><br />
       ```sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev```<br /><br />
       ```cd bluez-X.XX```<br /><br />
       ```export LDFLAGS=-lrt```<br /><br />
       ```./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-library -disable-systemd```<br /><br />
       ```make```<br /><br />
       ```sudo make install```<br /><br />
       ```sudo cp attrib/gatttool /usr/bin/```<br /><br />
     - Start bluez service <br /><br />
       ```sudo systemctl start bluetooth```<br /><br />
2) **bluepy** <br /><br />
     ```sudo pip3 install bluepy```<br /><br />
3) **bluez-peripheral** <br /><br />
     ```Sudo pip3 install bluez-peripheral``` <br />
###     
Now clone this repository in your desired folder. <br /><br />
```git clone https://github.com/Utkarsh-S-1110/Communication-over-BLE-between-two-Raspberry-Pis.git``` <br /><br />
You are now ready to use the functions from peripheral_framework.py and central_framework.py in your projects.
