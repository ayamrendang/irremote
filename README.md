# irremote
IR Remote + Python3.

Neccessity is the mother of invention. It is by no means I am a lazy bastard and refuse to stand up to change the volume on my pc which is 3 steps away.

This project uses a common arduino with an IR receiver, upon receiving IR signals, everything is decoded and sent via serial. Essentially this part is the same as the common IR receiver tutorial, where the results are monitored in serial monitor. On the PC a python script is run to listen to the port and sends the desired commands to pc.

Responses on pc can be changed in the hello.py file. For more info, refer to the pynput readme.

Requirements: PC - Python/Python3, python3-dev, python-dev, pynput, pyserial.

Hardware - Arduino (any mcu that can run arduino code), IR receiver, usb cable.

DOES NOT NEED USB-HID CAPABLE CHIP.

Just by decoding any existing old/tv/vcr/fembot remote, you can reuse the remote for your ahem purposes. Works in any OS that can run python. Tested on Windows10 and MX Linux.

Code is only put together, special thanks to the persons who developed pynput, pyserial & arduino IR receiver code.
