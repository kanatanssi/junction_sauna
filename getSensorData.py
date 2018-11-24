import urllib.request
import json
import time
from datetime import datetime
import tzlocal

while True:
    returned_data = urllib.request.urlopen(urllib.request.Request(
        "https://apigtw.vaisala.com/hackjunction2018/saunameasurements/latest?SensorID=Stove1&limit=4",
        headers={"Accept": 'application/json'}
    )).read()

    json_data = json.loads(returned_data)

    # print('CURRENT TEMPERATURE: ', jsonData[0]['Measurements']['Temperature']['value'], '\n')
    # print(json.dumps(jsonData, indent=4))
    first_temp = json_data[0]['Measurements']['Temperature']['value']
    last_temp = json_data[-1]['Measurements']['Temperature']['value']

    first_unix_timestamp = float(str(json_data[0]['Timestamp']))/1000
    first_local_timezone = tzlocal.get_localzone()
    first_local_time = datetime.fromtimestamp(first_unix_timestamp, first_local_timezone)

    second_unix_timestamp = float(str(json_data[-1]['Timestamp'])) / 1000
    second_local_timezone = tzlocal.get_localzone()
    second_local_time = datetime.fromtimestamp(second_unix_timestamp, second_local_timezone)
    print(first_temp, ' at: ', first_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"), last_temp, ' at: ', second_local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))

   # print(first_temp, last_temp)
    if first_temp / last_temp < 0.95:
        print('Holy loyly burning through the lungs right now')
    time.sleep(1)





'''for measurement in jsonData:
    unix_timestamp = float(str(measurement['Timestamp']))/1000
    local_timezone = tzlocal.get_localzone()
    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    print(local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))
''''''
ts = float(jsonData[0]['Timestamp'])
t = datetime.utcfromtimestamp(ts)
print('date, time: ', datetime.fromtimestamp(ts))
print(t.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))'''
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
