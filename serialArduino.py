# augmenting the experience inside
# give information outside

## Serial to Arduino
import serial
import time
import struct

arduino = serial.Serial('/dev/cu.usbmodem1411', 115200, timeout=.1)
print(arduino.name)
time.sleep(2)

while True:

    ## Get the sensor data

    ## recognize if 0 - nothing, 1 - normal, 2 - loyly, 3 - open door
    ent = 2

    ## Send the data
    arduino.write(struct.pack('>B', ent))
    #arduino.write("Hello from Python!")
    print("sent")
    data = arduino.readline()
    print("read")
    if data:
        print("data")
        print(data)  # strip out the new lines for now
        # (better to do .read() in the long run for this reason