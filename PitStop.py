import threading as thr

class PitStop(thr.Thread):

    def __init__(self, fuel, tires, status):
        thr.Thread.__init__(self)
        self.__flag = thr.Event()
        self.__flag.set()
        self.__running = thr.Event()
        self.__running.set()
        self.lock = thr.Lock()
        self.fuel = fuel
        self.tires = tires
        self.status = status

    def pit_stop_block(self):
        self.lock.acquire()

    def pit_stop_unblock(self):
        self.lock.release()
