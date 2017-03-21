#  Connect to WiFi
import machine
from network import WLAN

wlan = WLAN(mode=WLAN.STA)

if not wlan.isconnected():
    print('Connecting to WiFi''')
    wlan.connect('VM0184406',  auth=(WLAN.WPA2,  '2sqmsfFGqpry'),  timeout=5000)
    while not wlan.isconnected():
        machine.idle()

    if wlan.isconnected():
        print("Connected OK")
    else:
        print("Error Connecting")
else:
    print("WiFi already connected")
    
print(wlan.ifconfig())

# Run Sense
from beersense import BeerSense
bs = BeerSense()
bs.sense()
