import threading
import time

#wspólna lista
#wspólna blokada
list = []
lock = threading.Lock()

#thread_id - identyfikator wątku w postaci liczbowej, który wykorzystany zostanie do odliczania (10*i + n), gdzie i = thread_id
#list - argumentem konstruktora będzie wspólna lista, do której to wątki będą wpisywały kolejno liczby
#self.starting_num - pierwszy wyraz, od którego wątek zacznie odliczanie
class thread(threading.Thread):    
    def __init__(self, thread_id, list):
        threading.Thread.__init__(self, name=thread_id)
        self.starting_num = 10*thread_id 
        self.list = list

#blokada, dzięki której operacja wykonywana na wspólnej liście może być wykonywana przez jeden wątek w tym samym czasie
    def run(self): 
        with lock:
            num0 = self.starting_num
            numN = num0 + 9

            while num0  <= numN:
                self.list.append(num0)
                num0  += 1
                time.sleep(1) #symulacja obliczania w celu sprawdzenia porpawności działania programu

t0 = thread(0, list)
t1 = thread(1, list)
t2 = thread(2, list)
t3 = thread(3, list)

t0.start()
t1.start()
t2.start()
t3.start()

t0.join()
t1.join()
t2.join()
t3.join()

print(list)