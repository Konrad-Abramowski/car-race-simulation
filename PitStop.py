import threading as thr
import Car
import time

class PitStop(thr.Thread):

    def __init__(self, fuel, tires):
        thr.Thread.__init__(self)
        self.__flag = thr.Event()
        self.__flag.set()
        self.__running = thr.Event()
        self.__running.set()
        self.fuel = fuel
        self.tires = tires

