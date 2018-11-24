# augmenting the experience inside
# give information outside

## Serial to Arduino
import getSensorData as gsd
import consts
import serial
import time
import struct

ard_connected = True

if(ard_connected):
    arduino = serial.Serial('/dev/cu.usbmodem1411', 115200, timeout=.1)
    print(arduino.name)
    time.sleep(2)

def get_enthalpy():
    bench_data = gsd.get_sensor_data('Bench2', 1)
    return bench_data[0]['Measurements']['Enthalpy']['value']


def get_enthalpy2():
    bench_data = gsd.get_sensor_data('Bench2', 1)
    return bench_data[0]['Measurements']['Temperature']['value']


def loyly():
    sensordata = gsd.get_sensor_data('Stove1', 3)
    return gsd.check_for_loyly(sensordata[0], sensordata[-1])

def doorOpen():
    sensordata = gsd.get_sensor_data('Doorway1', 4)
    return gsd.check_for_opendoor(sensordata[0], sensordata[-1])


def check_state():
    if loyly():
        print("loyly")
        return consts.states['s_loyly']
    if doorOpen():
        print("door open")
        return consts.states['s_openDoor']

    ent = get_enthalpy()
    if ent < consts.maxEnt['s_nothing']:
        return consts.states['s_nothing']

    if ent < consts.maxEnt['s_heatingup']:
        print('s_heatingup')
        return consts.states['s_heatingup']
    if ent < consts.maxEnt['s_meh']:
        print('s_meh')
        return consts.states['s_meh']
    if ent < consts.maxEnt['s_warm']:
        print('s_warm')
        return consts.states['s_warm']
    if ent < consts.maxEnt['s_hot']:
        print('s_hot')
        return consts.states['s_hot']
    if ent < consts.maxEnt['s_sizzle']:
        print('s_sizzle')
        return consts.states['s_sizzle']
    return consts.states['hell']




while True:

    ## Check the state
    state = check_state()

    if(not ard_connected):
        print(state)
        time.sleep(1)

    ## recognize if 0 - nothing, 1 - normal, 2 - loyly, 3 - open door

    if(ard_connected):
        ## Send the data
        arduino.write(str.encode(str(state)))
        #arduino.write("Hello from Python!")
        print("Sent state " + str(state) + " to arduino")
        data = arduino.readline()
        if data:
            print(data.decode())  # strip out the new lines for now
            time.sleep(1)
            # (better to do .read() in the long run for this reason