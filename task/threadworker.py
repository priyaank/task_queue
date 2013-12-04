# threading queue test
# Priyaank Choubey - mail@priyaank.com

import threading
import Queue
import time


# Main thread class - based on threading.Thread
# This class is cloned/used as a thread template to spawn those threads.
# The class has a run function that gets a task out of the tasks queue
# And lets the queue object know when it has finished.

class Worker(threading.Thread):

    def __init__(self, tasks, max_try, wait_time):
        # Variables setup
        threading.Thread.__init__(self)
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
                task.task_done()
            except:
              if self.curret_try < self.max_try and not self.is_stop:
                  self.curret_try += 1
                  print "TRY {}: Since Nothing is there in Queue wait for {} sec".format(self.curret_try ,self.wait_time)
                  time.sleep(self.wait_time)
              else:
                print "Thread Stopped"
                break

    def stop(self):
        print "Stop Thread"
        self.is_stop = True   # No more jobs in the queue



if __name__ == '__main__':
    # Call the mainfunction that sets up threading.
    #inputlist_ori = [ (5,5),(10,4),(78,5),(87,2),(65,4),(10,10),(65,2),(88,95),(44,55),(33,3) ]
    #process_test = WorkerPool()
    #process_test.start_processing()
    #process_test.add_tasks(inputlist_ori)
    #process_test.stop_all()
    #time.sleep(10)
    #process_test.add_tasks(inputlist_ori)
    pass


