# threading queue test
# Priyaank Choubey - mail@priyaank.com

from multiprocessing import Process, Queue
import time


# Main process class - based on processing.process
# This class is cloned/used as a process template to spawn those processs.
# The class has a run function that gets a task out of the tasks queue
# And lets the queue object know when it has finished.


class Worker(Process):
    def __init__(self, tasks, max_try, wait_time):
        super(Worker, self).__init__()
        self.tasks = tasks
        # Variables setup
        self.curret_try = 0
        self.tasks = tasks
        self.max_try = max_try
        self.wait_time = wait_time
        self.is_stop = False

    def run(self):
        # run till max_try reached or stop called
        while 1:
            # Try and get a task out of the queue
            try:
                task = self.tasks.get(True,1)
                self.curret_try = 0
                print "Processing Task"
                print "Multiplication of {0} with {1} gives {2}".format(task[0],task[1],(task[0]*task[1]))
                time.sleep(0.5)
                # Let the queue know the task is finished.
            except Exception, e:
                print e
                if self.curret_try < self.max_try and not self.is_stop:
                    self.curret_try += 1
                    print self.is_stop
                    print "TRY {}: Since Nothing is there in Queue wait for {} sec".format(self.curret_try ,self.wait_time)
                    time.sleep(self.wait_time)
                else:
                    print "process Stopped"
                    break

    def stop(self):
        print "Stop process"
        self.is_stop = True   # No more jobs in the queue
