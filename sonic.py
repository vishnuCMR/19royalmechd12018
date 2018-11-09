from gpiozero import DistanceSensor
from time import sleep
s=DistanceSensor(echo=18, trigger=17)
while True:  
    print(s.distance)
    sleep(1)

