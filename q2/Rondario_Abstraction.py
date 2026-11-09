from abc import ABC, abstractmethod

# task 1 & 2
class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

# task 3 & 4
class PHSensor(Sensor):

    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")


class TempSensor(Sensor):

    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")

# Sucess Run for task 3 & 4
print("--- Lab Inventory System ---")
ph = PHSensor()
temp = TempSensor()

ph.get_reading()
temp.get_reading()
print("----------------------------")

# task 5 "Break it" test
try: 
    my_sensor = Sensor()
except TypeError as e:
    print(e)