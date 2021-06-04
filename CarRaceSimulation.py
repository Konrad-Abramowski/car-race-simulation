from PitStop import PitStop
import os
import random
import Car
import time

# TO DO:
# zasoby pitstopu: ilość opon i paliwa
# losowość zużycia opon i paliwa (minimalna)
# tankowanie i wymienianie opon 

if __name__ == "__main__":
    random.seed(10)

    # Ustawienia początkowe:
    Names = ('BMW', 'AUDI', 'VW', 'SKODA', 'FERRARI')
    number_of_cars = 2
    fuel = 100
    tires = 200
    loop_progress = 0
    active_status = 'Startuje'

    Cars = [Car.Car(Names[i], fuel, tires, loop_progress, active_status) \
            for i in range(number_of_cars)]

    Car.running = True
    for car in Cars:
        car.start()

    pit_stop = PitStop(10000,10000)
    pit_stop.start()

    # for Windows change set 'cls'
    # for Linux change set 'clear'
    def clear():
        if os.name == 'posix':
            os.system('clear')
        elif(os.name == 'nt'):
            os.system('cls')
    
    


    while True:
        clear()
        for car in Cars:
            print(car.active_status + ": " + car.name)
            print("Fuel:", car.fuel)
            print("Tires:", car.tires)
            print("Loop progress:", car.loop_progress)
        time.sleep(0.1)