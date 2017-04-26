import requests
import pprint
import time
import sys
from upm import pyupm_lm35 as sensorObj

artikcloud = "https://api.artik.cloud/v1.1/messages"
bearer = ''
sdid = ''

if len(sys.argv) == 3:
    bearer = 'Bearer ' + sys.argv[1]
    sdid = sys.argv[2]

    print(bearer +" "+ sdid)

else:
    print("Usage: temp_client.py [token] [device_id]")
    sys.exit(0)

headers_dict =  {
     "Content-Type": "application/json",
     "Authorization": bearer
   }

sensor = sensorObj.LM35(0)

while True:
    temp = int(sensor.getTemperature())
    print("Temperature:", temp , "C")
    data_dict = ' {"sdid": "' + sdid + '","type": "message","data": {"temperature": "'+str(temp)+'" } }'
    r = requests.post(artikcloud, headers = headers_dict, data=data_dict)
    #pprint.pprint(r.headers)
    pprint.pprint(r.content)
    time.sleep(10)

