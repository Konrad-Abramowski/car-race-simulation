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
 
    def __init__(self, name, fuel, tires, race_progress, active_status):
        thr.Thread.__init__(self)
        self.__flag = thr.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()
        self.name = name
        self.fuel = fuel
        self.tires = tires
        self.race_progress = race_progress
        self.active_status = active_status

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()
            self.fuel = self.fuel - 1
            self.tires = self.tires - 1
            time.sleep(0.1)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()