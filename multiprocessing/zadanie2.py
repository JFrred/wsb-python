from multiprocessing import Process
import os

def pid(name):
    print(f"Pid for {name}: {os.getpid()}")

print(os.getpid())
p0 = Process(target=pid, args=(0,))
p1 = Process(target=pid, args=(1,))
p0.start()
p1.start()