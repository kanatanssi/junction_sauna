# augmenting the experience inside
# give information outside

## Serial to Arduino
import getSensorData as gsd
import serial
import time
import struct

ard_connected = False

if(ard_connected):
    arduino = serial.Serial('/dev/cu.usbmodem1411', 115200, timeout=.1)
    print(arduino.name)
    time.sleep(2)

def get_enthalpy():
    print("get")
    bench_data = gsd.get_sensor_data('Bench2', 1)
    return bench_data['Measurements']['Enthalpy']['value']

while True:

    ## Get the sensor data
    ent = get_enthalpy()
    if(not ard_connected):
        print(ent)
        time.sleep(1)

    ## recognize if 0 - nothing, 1 - normal, 2 - loyly, 3 - open door

    if(ard_connected):
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