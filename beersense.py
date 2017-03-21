import machine
import time

from umqtt import MQTTClient
from machine import Pin
from ds18x20 import DS18X20
from network import WLAN

class BeerSense:
        
    def sense(self):
        print('Temperature Sensing and Reporting via MQtt')

        client = MQTTClient("beersense", "mqtt.dynamicdevices.co.uk", port=1883)
        client.connect()

        client.publish("sensors/brewing/status/1", "Running")

        d=DS18X20(Pin('G17', mode=Pin.OUT))

        while(1):
            result=d.read_temps()
            if(len(result) == 0):
                print("Error Reading from DS18X20")
                client.publish("sensors/brewing/status/1", "Sensor Error")
            else:
                if(result[0] > 100.0):
                    print("Temp: Read Error")
                    client.publish("sensors/brewing/status/1", "Sensor Error")
                else:
                    print("Temp: " + str(result[0]) + " C")
                    client.publish("sensors/brewing/temp/1", str(result[0]))
            time.sleep(10)

bs = BeerSense()
bs.sense()
