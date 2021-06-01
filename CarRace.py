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
        self.name = name
        self.fuel = fuel
        self.tires = tires
        self.race_progress = race_progress
        self.active_status = active_status

    def run(self):
        while(self.fuel>0):
            self.status()
            self.fuel -= self.fuel
            self.tires -= self.tires
            time.sleep(1)

    def status(self):
        print (self.active_status, self.fuel)

def CarRaceSimulation():

    random.seed(10)

    # Ustawienia początkowe:
    Names = ('BMW','AUDI','VW','SKODA','FERRARI')
    number_of_cars = 2
    fuel = 100
    tires = 200
    race_progress = 0
    active_status = 'Startuje'

    Cars = [Car(Names[i], fuel, tires, race_progress, active_status) \
            for i in range(number_of_cars)]

    Car.running = True
    for car in Cars: 
        car.start()

    for car in Cars: 
        car.join()


CarRaceSimulation()