from PitStop import PitStop
import os
import random
import Car
import time

# TO DO:

pit_fuel = 10000
pit_tires = 10000
pit_stop = PitStop(pit_fuel,pit_tires)

# tankowanie i wymienianie opon 

if __name__ == "__main__":
    random.seed(10)

    # Ustawienia początkowe:
    number_of_cars = 2
    Names = ('BMW', 'AUDI', 'VW', 'SKODA', 'FERRARI')
    fuel = 100
    tires = 100
  
    loop_progress = 0
    active_status = 'Startuje'

    pit_stop.start()

    Cars = [Car.Car(Names[i], fuel, tires, loop_progress, active_status, round(random.uniform(1.5, 3.5), 2), pit_stop) \
            for i in range(number_of_cars)]

    for car in Cars:
        car.start()



    # for Windows change set 'cls'
    # for Linux change set 'clear'
    def clear():
        if os.name == 'posix':
            os.system('clear')
        elif(os.name == 'nt'):
            os.system('cls')
    
    time.sleep(3)

    while True:
        clear()

        for car in Cars:
            print(car.active_status + ": " + car.name)
            print("Fuel: {:.2f}".format(car.fuel))
            print("Tires: {:.2f}".format(car.tires))
            print("Loop progress: {:.2f}".format(car.loop_progress))
            print("Car speed: {:.2f}".format(car.car_speed))
            print("\n")

        print("PitStop")
        print("Fuel: {:.2f}".format(pit_stop.fuel))
        print("Tires: {:.2f}".format(pit_stop.tires))
        print("PitStop status busy or not")
        print("\n")

        time.sleep(0.1)


    