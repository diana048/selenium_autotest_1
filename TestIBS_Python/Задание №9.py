from threading import Thread
from time import sleep
import datetime

def func1():
    for i in range(10, 0, -1):
        if i == 10:
            print("Поток 1: ", i, "start datetime: ", datetime.datetime.now())
        elif i == 1:
            print("Поток 1: ", i, "finish datetime: ", datetime.datetime.now())
        else:
            print("Поток 1: ", i)
            sleep(1)

def func2():
    for i in range(10, 0, -1):
        if i == 10:
            print("Поток 2: ", i, "start datetime: ", datetime.datetime.now())
        elif i == 1:
            print("Поток 2: ", i, "finish datetime: ", datetime.datetime.now())
        else:
            print("Поток 2: ", i)
            sleep(1)

th1 = Thread(target=func1)
th2 = Thread(target=func2)
th1.start()
th2.start()
th1.join()
th2.join()
print("--- stop ---")