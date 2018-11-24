# augmenting the experience inside
# give information outside

## Serial to Arduino
import serial
import time
import struct

ser = serial.Serial('/dev/tty.usbserial', 9600)
time.sleep(2)

while True:

    ## Get the sensor data

    ## recognize if 0 - nothing, 1 - normal, 2 - loyly, 3 - open door
    ent = 0;

    ## Send the data
    ser.write(struct.pack('>B', ent))
    time.sleep(.1)