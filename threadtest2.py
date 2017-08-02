

import time, threading, random

A = []


def doWork():
    global A
    for i in range(10000):
        A.append(i)


aThread = threading.Thread(target=doWork, name="aThread")
aThread.start()
bThread = threading.Thread(target=doWork, name="bThread")
bThread.start()


aThread.join()
bThread.join()

print len(A)