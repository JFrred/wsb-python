from multiprocessing import Process, Queue, Lock
import time

key_word = "exit"

def childProcess(queue, lock):
    while True:
        element = queue.get()
        print("Proces potomny:", element)

        if element == key_word:
            break
        lock.release()
       
lock = Lock()
queue = Queue()
child = Process(target=childProcess, args=(queue,lock))

child.start()
time.sleep(1)

while True:
    lock.acquire()

    word = input("Wpisz frazę: ")
    queue.put(word)
    if word == key_word:
        break

child.join()