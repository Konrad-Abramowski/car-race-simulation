import threading as thr

class PitStop(thr.Thread):

    running = True

    def __init__(self, pit_fuel, pit_tires):
        thr.Thread.__init__(self)
        self.__flag = thr.Event()
        self.__flag.set()
        self.__running = thr.Event()
        self.__running.set()
        self.pit_fuel = pit_fuel
        self.pit_tires = pit_tires

    def run(self):
        print("Pitstop running")