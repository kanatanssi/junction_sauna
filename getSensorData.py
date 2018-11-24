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

    first_unix_timestamp = float(str(measurement1['Timestamp'])) / 1000
    first_local_timezone = tzlocal.get_localzone()
    first_local_time = datetime.fromtimestamp(first_unix_timestamp, first_local_timezone)

    second_unix_timestamp = float(str(measurement2['Timestamp'])) / 1000
    second_local_timezone = tzlocal.get_localzone()
    second_local_time = datetime.fromtimestamp(second_unix_timestamp, second_local_timezone)
    print(first_temp, ' at: ', first_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"), last_temp, ' at: ',
          second_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))

    if first_temp / last_temp < 0.95:
        return True
    else:
        return False


# example usage doing the same thing as before
'''
while True:
    sensordata = get_sensor_data('Stove1', 4)
    check_for_loyly(sensordata[0], sensordata[-1])
    time.sleep(1)
'''