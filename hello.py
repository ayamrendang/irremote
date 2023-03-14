#https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
import serial
import pynput
import time
import os
from pynput.keyboard import Key, Controller

keyboard = Controller()
key=0
port='COM3'
ser = serial.Serial(
        # Serial Port to read the data from
        port=port,

        #Rate at which the information is shared to the communication channel
        baudrate = 9600,

        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,

       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,

        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,

        # Number of serial commands to accept before timing out
        timeout=1
)
# Pause the program for 1 second to avoid overworking the serial port
print("----")
print("Listening on " + port)
print("----")
while 1:
    x=ser.readline()
    y=x.hex()
    if (len(x)):
        if y == "370d0a":       #VOL-
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
        if y == "32310d0a":     #VOL+
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
        if y == "390d0a":       #EQ
            keyboard.press(Key.media_volume_mute)
            keyboard.release(Key.media_volume_mute)
        if y == "36380d0a":     #PREV
            keyboard.press(Key.media_previous)
            keyboard.release(Key.media_previous)
        if y == "36340d0a":     #NEXT
            keyboard.press(Key.media_next)
            keyboard.release(Key.media_next)
        if y == "36370d0a":     #PLAY/Pause
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause)
        if y == "36390d0a":     #CH-
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        if y == "37300d0a":     #CH
            if key:
                key = 0
                keyboard.release(Key.alt_l)
                keyboard.release(Key.tab)
            else:
                keyboard.press(Key.alt_l)
                keyboard.press(Key.tab)
                key = 1

        if y == "37310d0a":     #CH+
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        if y == "31330d0a":     #200+
            os.startfile('')
        if y == "32320d0a":     #0
            keyboard.press(Key.alt_l)
            keyboard.press(Key.f4)
            keyboard.release(Key.alt_l)
            keyboard.release(Key.f4)
        if y == "32350d0a":     #100+
            keyboard.press('f')
            keyboard.release('f')
        if y == "31320d0a":     #1
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
        if y == "32340d0a":     #2
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        if y == "39340d0a":     #3
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)
        if y == "380d0a":       #4
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        if y == "32380d0a":     #5
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        if y == "39300d0a":     #6
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        if y == "36360d0a":     #7
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        if y == "38320d0a":     #8
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        if y == "37340d0a":     #9
            keyboard.press(Key.page_down)
            keyboard.release(Key.page_down)
    time.sleep(0.3)
        
"""
CH-         36390d0a
CH          37300d0a
CH+         37310d0a
PREV        36380d0a
NEXT        36340d0a
PLAY/Pause  36370d0a
VOL-          370d0a
VOL+        32310d0a
EQ            390d0a
0           32320d0a
100+        32350d0a
200+        31330d0a
1           31320d0a
2           32340d0a
3           39340d0a
4             380d0a
5           32380d0a
6           39300d0a
7           36360d0a
8           38320d0a
9           37340d0a

if y == "36390d0a":     #CH-
if y == "37300d0a":     #CH
if y == "37310d0a":     #CH+
if y == "36380d0a":     #PREV
if y == "36340d0a":     #NEXT
if y == "36370d0a":     #PLAY/Pause
if y == "370d0a":       #VOL-
if y == "32310d0a":     #VOL+
if y == "390d0a":       #EQ
if y == "32320d0a":     #0
if y == "32350d0a":     #100+
if y == "31330d0a":     #200+
if y == "31320d0a":     #1
if y == "32340d0a":     #2
if y == "39340d0a":     #3
if y == "380d0a":       #4
if y == "32380d0a":     #5
if y == "39300d0a":     #6
if y == "36360d0a":     #7
if y == "38320d0a":     #8
if y == "37340d0a":     #9
"""
