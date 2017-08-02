

import time, multiprocessing
from multiprocessing import freeze_support


def doWork():
    name = multiprocessing.current_process()
    print "%s start..." % name
    time.sleep(3)
    print "%s stop..." % name

if __name__ == '__main__':
    freeze_support()
    print time.time()
    aThread = multiprocessing.Process(target=doWork, name="aThread")
    aThread.start()
    bThread = multiprocessing.Process(target=doWork, name="bThread")
    bThread.start()
    aThread.join()  #current thread is waiting a thread
    bThread.join()  #current thread is waiting b thread

print time.time()
