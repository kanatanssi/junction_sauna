import urllib.request
import json
returnedData = urllib.request.urlopen(urllib.request.Request(
    "https://apigtw.vaisala.com/hackjunction2018/saunameasurements/latest?SensorID=Bench2&limit=1",
    headers={"Accept" : 'application/json'}
)).read()

jsonData = json.loads(returnedData)
print('CURRENT TEMPERATURE: ', jsonData[0]['Measurements']['Temperature']['value'], '\n')
print(json.dumps(jsonData, indent=4))
