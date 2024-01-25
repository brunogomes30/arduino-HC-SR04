import serial
import time
class ArduinoCommunication:

    def __init__(self, device = 'COM7', baudrate = 9600):
        self.serial = connect(device, baudrate)
        self.clear()
        self.value = -1


    def write(self, msg):
        self.serial.write(msg)
        
    def read(self):
        self.write(bytearray(0x01)) # request distance from arduino
        return self.serial.readline()

    def has_data(self):
        return self.serial.inWaiting() > 0
    
    def clear(self):
        self.serial.flushInput()
        self.serial.flushOutput()
    
    def update(self):
        # Read the line from the Arduino
        line = self.read().strip()
        # Split the line into values
        values = line.split(b' ')
        
        if len(values) <= 0 or values[0] == b'':
            return
        self.value = int(values[0])
        print(self.value)

    def value_was_read(self):
        return self.value != -1
        

def connect(device, baudrate):
    return serial.Serial(device, baudrate, timeout=1)