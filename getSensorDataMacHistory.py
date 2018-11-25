import urllib.request
import json
import time
from datetime import datetime
import tzlocal
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()


# Return a list of json object containg the sensor data
'''def get_sensor_data(sensorname, number):
    req = urllib.request.urlopen(urllib.request.Request(
        "https://apigtw.vaisala.com/hackjunction2018/saunameasurements/latest?SensorID=" +
        sensorname + "&limit=" + str(number),
        headers={"Accept": 'application/json'}
    ), context=context)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    sensordata = req.read()
    return json.loads(sensordata)
'''
def get_ville_measurements():
    req = urllib.request.urlopen(urllib.request.Request(
        "https://apigtw.vaisala.com/hackjunction2018/saunameasurements/history?SensorID=Stove1&after=1543082220208&before=1543082482068",
        headers={"Accept": 'application/json'}), context=context)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    sensordata = req.read()
    return json.loads(sensordata)

# input: two json measurements, which are the elements of the list returned by get_sensor_data
# return True if it detects loyly, False if not
def check_for_loyly(measurement1, measurement2):
    first_temp = measurement1['Measurements']['Temperature']['value']
    last_temp = measurement2['Measurements']['Temperature']['value']

    first_local_time = get_localtime_from_measurement(measurement1)
    second_local_time = get_localtime_from_measurement(measurement2)

    print(first_temp, ' at: ', first_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"), last_temp, ' at: ',
          second_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))

    if first_temp / last_temp < 0.95:
        return True
    else:
        return False


def check_for_opendoor(measurement1, measurement2):
    first_temp = measurement1['Measurements']['Relative humidity']['value']
    last_temp = measurement2['Measurements']['Relative humidity']['value']

    first_local_time = get_localtime_from_measurement(measurement1)
    second_local_time = get_localtime_from_measurement(measurement2)

    print(first_temp, ' at: ', measurement1['Timestamp'], first_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"),
    last_temp, ' at: ', measurement1['Timestamp'], second_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))

    if last_temp - first_temp > 1.5:
        return True
    else:
        return False


def get_localtime_from_measurement(measurement):
    unix_timestamp = float(str(measurement['Timestamp'])) / 1000
    local_timezone = tzlocal.get_localzone()
    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    return local_time


def get_next_four_measurements():
    measurements = get_ville_measurements()
    for index in (range(len(measurements[0:-3]))):
        yield measurements[index: index + 3]

# example usage doing the same thing as before
if __name__ == '__main__':

    for sensordata in get_next_four_measurements():
        print(sensordata)
        if check_for_loyly(sensordata[0], sensordata[-1]):
            print('LOYLY')
        time.sleep(0.7)


"""while True:
    sensordata = get_sensor_data('Doorway1', 4)
    if check_for_opendoor(sensordata[0], sensordata[-1]):
        print('DOOR OPEN')
    time.sleep(1)"""

#while True:
#    sensordata = get_sensor_data('Stove1', 4)
#    if check_for_opendoor(sensordata[0], sensordata[-1]):
#        print('DOOR OPEN')
#    if check_for_loyly(sensordata[0], sensordata[-1]):
#        print('LOYLY')
#    time.sleep(1)
