import urllib.request
import json
import time
from datetime import datetime
import tzlocal


# Return a list of json object containg the sensor data
def get_sensor_data(sensorname, number):
    sensordata = urllib.request.urlopen(urllib.request.Request(
        "https://apigtw.vaisala.com/hackjunction2018/saunameasurements/latest?SensorID=" +
        sensorname + "&limit=" + str(number),
        headers={"Accept": 'application/json'}
    )).read()
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



# example usage doing the same thing as before
while True:
    sensordata = get_sensor_data('Doorway1', 4)
    if check_for_opendoor(sensordata[0], sensordata[-1]):
        print('DOOR OPEN')
    time.sleep(1)
