# threading queue test
# Priyaank Choubey - mail@priyaank.com

import threading
import Queue
import time


# Main thread class - based on threading.Thread
# This class is cloned/used as a thread template to spawn those threads.
# The class has a run function that gets a task out of the tasks queue
# And lets the queue object know when it has finished.

class TaskProcessor(threading.Thread):

    def __init__(self, tasks, singlelock, max_try, wait_time):
        # Variables setup
        threading.Thread.__init__(self)
        self.curret_try = 0
        self.tasks = tasks
        self.max_try = max_try
        self.wait_time = wait_time
        self.singlelock = singlelock
        self.is_stop = False

    def run(self):
        # run till max_try reached or stop called
        while 1:
            # Try and get a task out of the queue
            try:
                task = self.tasks.get(True,1)
                self.singlelock.acquire()        # Acquire the lock
                self.curret_try = 0
                print "Multiplication of {0} with {1} gives {2}".format(task[0],task[1],(task[0]*task[1]))
                time.sleep(0.5)
                self.singlelock.release()        # Release the lock
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


#
# optional to pass pool_size, wait_time and max_try

class WorkerPool():
    def __init__(self, pool_size=3,wait_time=1,max_try=6,default_start=True):
        print "WorkerPool created with {} tasks".format(pool_size)
        print "Each Thread will pool in {} sec for tasks".format(wait_time)
        print "Each Thread will maximum try {} times to take task then automaitically dies.".format(max_try)
        self.thread_pool_size = pool_size                # This is how many threads we want by Default
        self.thread_wait_time = wait_time        # This is how much time thread should wait if queue is empty
        self.max_try = max_try                          # This is maximum number of try a thread will and then go dead
        self.tasks = Queue.Queue(100)
        self.singlelock = threading.Lock()
        self.threads = []

        # Spawn the threads
        print "Spawning the {0} threads.".format(self.thread_pool_size)
        for x in xrange(self.thread_pool_size):
            print "Thread {0} created.".format(x)
            # This is the thread class that we instantiate.
            self.threads.append(TaskProcessor(self.tasks, self.singlelock, self.max_try, self.thread_wait_time))

        if default_start:
            self.start_processing()


    def pool_size(self):
        return len(self.threads)


    def start_processing(self):
        try:
            x = 1
            for thread in self.threads:
                print "Thread {0} started.".format(x)
                x += 1
                thread.start()
            self.tasks.join()
        except Exception, e:
            print "WorkerPool already Started"
            raise e


    def stop_all(self):
        try:
            x = 1
            for thread in self.threads:
                print "Thread {0} signaled Stop.".format(x)
                x += 1
                thread.stop()
        except Exception, e:
            print "WorkerPool already Stopped"
            raise e

    def add_tasks(self, input_tasks):
        # Put stuff in queue
        print "Putting tasks in queue"
        for i in input_tasks:
            # Block if queue is full, and wait 5 seconds. After 5s raise Queue Full error.
            try:
                self.tasks.put(i, block=True, timeout=5)
            except:
                print "The queue is full !"

        print "Inputlist received..."
        print input_tasks


    def add_task(self, input_task):
        # Put stuff in queue
        print "Putting tasks in queue"
        try:
            self.tasks.put(imput_task, block=True, timeout=5)
        except:
            print "The queue is full !"

    def task_in_queue(self):
        return self.tasks.qsize()


if __name__ == '__main__':
    # Call the mainfunction that sets up threading.
    inputlist_ori = [ (5,5),(10,4),(78,5),(87,2),(65,4),(10,10),(65,2),(88,95),(44,55),(33,3) ]
    process_test = WorkerPool()
    process_test.start_processing()
    process_test.add_tasks(inputlist_ori)
    process_test.stop_all()
    #time.sleep(10)
    #process_test.add_tasks(inputlist_ori)


