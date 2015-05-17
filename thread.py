import threading
import time
import os

def doChord():
    time.sleep(0.5)

def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()
	if i != 0:
	    i = i - 1
	    print tid,':now left:',i
	    doChord()
	else:
	    print 'threadid:',tid,'no more tickets'
	    os._exit(0)
	lock.release()
	doChord()

i = 100
lock = threading.Lock()

for k in range(10):
    newthread = threading.Thread(target = booth, args=(k,))
    newthread.start()

