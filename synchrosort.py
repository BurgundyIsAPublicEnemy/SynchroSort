import time
from threading import Thread
import threading
import sys
import random

k = False

class M(threading.Thread):
    def __init__(self, num):
        super(M, self).__init__()
        self.num = num

    def run(self):
        global k
        s = time.time
        print (s)
        while (time.time  - s) < (self.num) :
            if k:
                break
        print (str(self.num) + "\n")

NumList = random.sample(range(1,100),10)
for index in range (len(NumList)):
    t = M(NumList[index])
    t.start()
