import threading
import threading as thr
import random
import time

# Symulacja wyscigu samochodowego, gdzie paliwo i opony są zasobami, które należy uzupełniać.
# Zasobem wspólnym jest droga do pitstopu i sam pitstop.

# fuel = 100          #od 0 do 100, 100 oznacza pelny bak paliwa
# tires = 100         #od 0 do 100, 100 oznacza nowe opony
# race_progress = 0   #od 0 do 100, 0 oznacza poczatek wyscigu

lock = thr.Lock()

class Car(thr.Thread):
 
    running = True
 
    def __init__(self, name, fuel, tires, loop_progress, active_status, car_speed):
        thr.Thread.__init__(self)
        self.__flag = thr.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()
        self.name = name
        self.fuel = fuel
        self.tires = tires
        self.loop_progress = loop_progress
        self.active_status = active_status
        self.car_speed = car_speed

    def set_loop_progress(self, car_speed):
        if self.loop_progress + car_speed >= 100: self.loop_progress = self.loop_progress - 100 + car_speed
        else: self.loop_progress = self.loop_progress + car_speed
        
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()
            fuel_wear = round(random.uniform(0.5, 1.5), 2)
            tires_wear = round(random.uniform(1, 2.5), 2)
            if (self.loop_progress == 0 and (self.fuel < 25 or self.tires < 25)):
                print("pitstop")
                time.sleep(3)
            self.fuel = self.fuel - fuel_wear
            self.tires = self.tires - tires_wear
            self.set_loop_progress(self.car_speed)
            time.sleep(0.5)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()
