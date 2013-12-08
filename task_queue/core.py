# threading queue test
# Priyaank Choubey - mail@priyaank.com
#
#
#  WorkerPool.
#  It creates pool of workes to execute our task that we add.

#  WorkerPool Provided options
#  is_thread=True        #WorkerPool would be multithreaded, By default it create multiprocessed
#  pool_size=3           #You can define number of process and threads to run in parellel, By Default its value is 3.
#  wait_time=1           #You can specify wait time for next pool if TaskQueue is Empty, By Default its value s 1.
#  max_try=12            #You can specify max_try a worker would try to find task in queue else die.
                         #By Default its value is 12.
#  default_start=True    #You can also just initialize WorkerPool without starting workers to start working.
                         #By default its value is True.


from pool.thread import Worker as ThreadWorker
from pool.process import Worker as ProcessWorker
from queue.inmemory import TaskQueue
from task import Task


class WorkerPool():
    def __init__(self, is_thread=False, pool_size=3,
        wait_time=1, max_try=12, default_start=True):

        print "WorkerPool created with {} tasks".format(pool_size)
        self.pool_size = pool_size
        self.wait_time = wait_time
        self.max_try = max_try
        self.tasks = TaskQueue()
        self.workers = []
        self._type = "process"
        self.worker = ProcessWorker
        self.default_start = default_start

        # Spawn the threads
        if is_thread:
            self.worker = ThreadWorker
            self._type = "Thread"

        self.__init_worker() # Initialize Workers

    def __init_worker(self):
        print "Spawning the {} {}.".format(self.pool_size, self._type)
        for x in xrange(self.pool_size):
            print "{} {} created.".format(self._type, x)
            self.workers.append(self.worker(self.tasks, self.max_try, self.wait_time))

        if self.default_start:
            self.start_processing()  # Start Workers

    def start_processing(self):
        try:
            x = 1
            for worker in self.workers:
                print "{} {} started.".format(self._type, x)
                x += 1
                worker.start()
        except Exception, e:
            print "Workers already Started"
            raise e


    def stop_all(self):
        try:
            x = 1
            for worker in self.workers:
                print "{} {} started.".format(self._type, x)
                x += 1
                worker.stop()
        except Exception, e:
            print "Workers already Stopped"
            raise e

    def add_tasks(self, input_tasks):
        # Put stuff in queue
        print "Inputlist received..."
        print "Putting tasks in queue"
        for task in input_tasks:
            # Block if queue is full, and wait 5 seconds. After 5s raise Queue Full error.
            if isinstance(task, Task):
                try:
                    self.tasks.put(task, block=True, timeout=5)
                except Exception,e:
                    print e
                    print "The queue is full !"
            else:
                print "Given Task is not as Instance of Abstract Task, Cannot be added in Task Queue"



    def add_task(self, input_task):
        # Put stuff in queue
        print "Putting task in queue"
        if isinstance(imput_task, Task):
            try:
                self.tasks.put(imput_task, block=True, timeout=5)
            except:
                print "The queue is full !"

    def task_is_empty(self):
        return self.tasks.empty()
