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
 
    def __init__(self, name, fuel, tires, loop_progress, active_status, car_speed, pit_stop, race_progress, place):
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
        self.pit_stop = pit_stop
        self.race_progress = race_progress
        self.place = place

    def set_loop_progress(self, car_speed):
        if self.loop_progress + car_speed >= 100: self.loop_progress = self.loop_progress - 100 + car_speed
        else: self.loop_progress = self.loop_progress + car_speed

    def set_race_progress(self, car_speed):
        if self.loop_progress + car_speed >= 100: self.race_progress = self.race_progress + 1

    def set_place(self, race_progress, place):
        if  self.race_progress >= loops:
                self.place = first_place
                print(self.name + ": Miejsce ", self.place)
                first_place = first_place + 1
                self.__flag.clear() # albo tutaj nie wiem
        
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()
            fuel_wear = round(random.uniform(0.5, 1.5), 2)
            tires_wear = round(random.uniform(1, 2.5), 2)
            if (self.loop_progress < 10 and (100/self.car_speed > self.fuel/1.5 or 100/self.car_speed > self.tires/2.5)): #1.5 i 2.5 to maks zużycia opon lub paliwa; możemy dać takie ryzyko, że zamiast maks zużycia dać średnią, wtedy bedzie 50% szans, że dojedzie 
                self.use_pit_stop(self.pit_stop)
            self.fuel = self.fuel - fuel_wear
            self.tires = self.tires - tires_wear
            self.set_race_progress(self.car_speed)
            self.set_loop_progress(self.car_speed)
            time.sleep(0.2)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def use_pit_stop(self, pit_stop):
        #  TODO 
        # lock PitStop thread (lock, acquire)
        # threading.Lock(pit_stop).acquire
        
        self.pause()  
        time.sleep(0.1)
        pit_stop.fuel = pit_stop.fuel - (100 - self.fuel)
        self.fuel = 100
        pit_stop.tires = pit_stop.tires - (100 - self.tires)
        self.tires = 100
        self.resume()

        #  TODO 
        # release PitStop
