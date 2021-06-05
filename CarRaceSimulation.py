from PitStop import PitStop
import os
import random
import Car
import time

# TO DO:



# tankowanie i wymienianie opon 

if __name__ == "__main__":
    random.seed(10)

    # Ustawienia początkowe:
    number_of_cars = 2
    Names = ('BMW', 'AUDI', 'VW', 'SKODA', 'FERRARI')
    fuel = 100
    tires = 100
    pit_fuel = 100000
    pit_tires = 100000
    loop_progress = 0
    race_progress = 0
    loops = 1
    first_place = 1
    active_status = 'Startuje'


    pit_stop = PitStop(pit_fuel,pit_tires, "not busy")
    pit_stop.start()

    Cars = [Car.Car(Names[i], fuel, tires, loop_progress, active_status, round(random.uniform(1.5, 3.5), 2), pit_stop, race_progress, 0) \
            for i in range(number_of_cars)]

    for car in Cars:
        car.start()

    def clear():
        if os.name == 'posix':
            os.system('clear')
        elif(os.name == 'nt'):
            os.system('cls')
    
    time.sleep(3)
    while True:
        clear()

        for car in Cars:
            if car.race_progress >= loops:
                car.place = first_place
                print(car.name + ": Miejsce ", car.place)
                first_place = first_place + 1
                car.__flag.clear() #### tutaj
            else:
                print(car.active_status + ": " + car.name)
                print("Fuel: {:.2f}".format(car.fuel))
                print("Tires: {:.2f}".format(car.tires))
                print("Loop progress: {:.2f}".format(car.loop_progress))
                print("Car speed: {:.2f}".format(car.car_speed))
                print("Race progress: ", car.race_progress)
            print("\n")

        print("PitStop")
        print("Fuel: {:.2f}".format(pit_stop.fuel))
        print("Tires: {:.2f}".format(pit_stop.tires))
        print("PitStop status: " + pit_stop.status)
        print("\n")

        time.sleep(0.2)


    