import threading
import time

class MyNewThread(threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print "\nStarting: %s " % self.name #we are printing the start of the thread
        DoXY(self.name, self.counter)
        print "\nExiting: %s " % self.name #we are printing the end of the thread
                                     
                                     
                                     
def DoXY(threadname, threadcounter):
    for i in range(0,threadcounter*2):
        Var = threadcounter * i
        print "Here is the result: %s, for thread: %s \n" % (Var, threadname) ##so the results show that the new line is implemented after the method has been done for all 
                                                                              ## three threads.
                                                                               
        

                                   
thread1 = MyNewThread(1001, "Thread1", 5)
thread2 = MyNewThread(1002, "Thread2", 5)
thread3 = MyNewThread(1003, "Thread3", 5)



thread1.start()
thread2.start()
thread3.start()
