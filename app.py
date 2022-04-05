# env-1\Scripts\activate
# Set-ExecutionPolicy Unrestricted -Scope Process
# python app.py
import warnings
import serial
import serial.tools.list_ports
import requests
import json

edgex_ip    = "172.20.10.69"
core_metadata = 59881
core_data = 59880
core_command = 59882 
device_rest = 59986

device_name="PIR-Device-1"
sensor_name="PIR"

vals={'motion':True,'nomotion':False}

ports=list(serial.tools.list_ports.comports())
for p in ports:
    print(p.name)
    print(p)

arduinoData=serial.Serial('COM3',9600,timeout=1)


while True:
    while(arduinoData.inWaiting()==0):
        pass
    data=arduinoData.readline()
    data=str(data,'utf-8').strip('\r\n')
    print(data)
    print("Sending data to edgex...")
    url = f"http://{edgex_ip}:{device_rest}/api/v2/resource/{device_name}/{sensor_name}"
    print(url)
    break
    payload=vals[data]
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)