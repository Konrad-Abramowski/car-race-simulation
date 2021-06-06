from PitStop import PitStop
import os
import random
import Car
import time

if __name__ == "__main__":
    random.seed(10)

    timeout = time.time() + 60 

    # Ustawienia początkowe:
    number_of_cars = 10
    Names = ('BMW1', 'AUDI', 'VW1', 'FIAT1', 'BMW2', 'AUDI2', 'FORD2', 'VW2', 'FORD1', 'FIAT2')
    fuel = 100
    tires = 100
    pit_fuel = 100000
    pit_tires = 100000
    loop_progress = 0
    race_progress = 0
    loops = 1
    first_place = 1
    active_status = '    Is starting'


    pit_stop = PitStop(pit_fuel, pit_tires, "not busy")
    pit_stop.start()

    Cars = [Car.Car(Names[i], fuel, tires, loop_progress, active_status, round(random.uniform(2, 3), 2), pit_stop, 0) \
            for i in range(number_of_cars)]

    for car in Cars:
        car.start()

    def clear():
        if os.name == 'posix':
            os.system('clear')
        elif(os.name == 'nt'):
            os.system('cls')
    
    #time.sleep(3)
    while True:

        if time.time() > timeout:
            break   

        clear()

        for car in Cars:
            print(car.active_status + ": " + car.name + "\t" + "Fuel: {:.2f}".format(car.fuel) + "\t" + "Tires: {:.2f}".format(car.tires) + "\t" + "Speed: {:.2f}".format(car.car_speed) + "\t" + "Loop progress: {:.2f}".format(car.loop_progress) + "\t" + "Loops finished: {}".format(car.loop_counter))

        print("\n")
        print("PitStop")
        print("Fuel: {:.2f}".format(pit_stop.fuel))
        print("Tires: {:.2f}".format(pit_stop.tires))
        print("PitStop status: " + pit_stop.status)
        print("\n")

        time.sleep(0.2)

    winner = Cars[0].loop_counter * 100 + Cars[0].loop_progress 

    for car in Cars:
        if car.loop_counter * 100 + car.loop_progress >= winner:
            winner = car.loop_counter * 100 + car.loop_progress
            winner_name = car.name

    print("The winner is: " + winner_name)

    

