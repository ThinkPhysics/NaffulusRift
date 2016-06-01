# PyUserInput test.
# Requires sudo pip3 install pyuserinput python3-xlib
#
# Code heavily based on https://www.raspberrypi.org/learning/microbit-game-controller/worksheet/


import serial
from time import sleep
import pyautogui

def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def move ():
    deadzone_x = 200
    deadzone_y = 200
    key_delay = 0.4
    
    screensize_x, screensize_y = pyautogui.size()
    print(screensize_x, screensize_y)
    
    PORT = "/dev/ttyACM1"
    #~ PORT = "/dev/serial/by-id/usb-MBED_MBED_CMSIS-DAP_9900023431864e45001210060000003700000000cc4d28bd-if01"
    BAUD = 115200
    
    s = serial.Serial(PORT)
    s.baudrate = BAUD
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    
    while True:
        data = s.readline().decode('UTF-8')
        data_list = data.rstrip().split(' ')
        try:
            x, y, z, a, b = data_list
            
            x_mapped = arduino_map(int(x), -1024, 1024, -10, 10)
            y_mapped = arduino_map(int(y), -1024, 1024, -10, 10)
            
            x_centre = screensize_x / 2
            y_centre = screensize_y / 2
            
            print(x_mapped, y_mapped)
            pyautogui.moveRel(x_centre + x_mapped, y_centre + y_mapped)
        
            
        except:
            pass
        
    s.close()
    
    
if __name__ == "__main__":
    move()
