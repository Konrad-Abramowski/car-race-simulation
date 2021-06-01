import threading as thr
import random
import time

# Filozofowie nie czekaja na drugi widelec trzymajac jeden. - zakleszczenie
# Jesli nie uda sie zdobyc drugiego widelca, filozof odklada pierwszy, zamienia
# ich kolejnosc i znow probuje zdoby dwa widelce.

class Filozof(thr.Thread):
 
    running = True
 
    def __init__(self, xname, forkOnLeft, forkOnRight, active_status):
        thr.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
        self.active_status = active_status
 
    def run(self):
        while(self.running):
            self.active_status = '%s mysli' % self.name
            self.status()
            time.sleep(random.uniform(2.5,3.5)) # mysli okolo 3 sekundy
            self.active_status = '%s jest glodny' % self.name
            self.status()
            time.sleep(random.uniform(2.5, 3.5))
            self.dine()
            time.sleep(random.uniform(2.5, 3.5))
 
    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
 
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            self.active_status = '%s zmienia widelce' % self.name
            self.status()
            time.sleep(random.uniform(2.5, 3.5))
            fork1, fork2 = fork2, fork1
        else:
            return
 
        self.dining()
        fork2.release()
        fork1.release()
 
    def dining(self):			
        self.active_status = '%s je' % self.name
        self.status()
        time.sleep(random.uniform(2.5,3.5)) # je okolo 3 sekundy
        self.active_status = '%s konczy jesc, zaczyna myslec' % self.name
        self.status()
        time.sleep(random.uniform(2.5, 3.5))
        
    def status(self):
        for p in thr.enumerate():
            if p is not thr.main_thread():
                print (p.active_status)
        print ('\n\n\n\n\n\n\n')

def DiningFilozofs():
    number_of_Filozofs = 5
    random.seed(10)

    forks = [thr.Lock() for n in range(number_of_Filozofs)]
    FilozofNames = ('Filozof 1','Filozof 2','Filozof 3','Filozof 4','Filozof 5')
 
    Filozofs = [Filozof(FilozofNames[i], forks[i%number_of_Filozofs], forks[(i+1)%number_of_Filozofs], 'Mysli') \
            for i in range(number_of_Filozofs)]
 
    Filozof.running = True
    for p in Filozofs: 
        p.start()
 
DiningFilozofs()