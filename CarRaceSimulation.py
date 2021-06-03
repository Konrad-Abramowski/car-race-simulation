import os
import random
import Car
import time

if __name__ == "__main__":
    random.seed(10)

    # Ustawienia początkowe:
    Names = ('BMW', 'AUDI', 'VW', 'SKODA', 'FERRARI')
    number_of_cars = 2
    fuel = 100
    tires = 200
    race_progress = 0
    active_status = 'Startuje'

    Cars = [Car.Car(Names[i], fuel, tires, race_progress, active_status) \
            for i in range(number_of_cars)]

    Car.running = True
    for car in Cars:
        car.start()

    # for Windows change set 'cls'
    # for Linux change set 'clear'
    clear = lambda: os.system('clear')

    while True:
        clear()
        for car in Cars:
            print(car.active_status + ": " + car.name)
            print("Fuel:", car.fuel)
            print("Tires:", car.tires)
        time.sleep(0.1)