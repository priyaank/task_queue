from multiprocessing import Queue
from threadworker import Worker as ThreadWorker
from processworker import Worker as ProcessWorker
# optional to pass pool_size, wait_time and max_try

class WorkerPool():
    def __init__(self, is_process=True, is_threaded=False, pool_size=3,
        wait_time=1, max_try=6, default_start=True):

        print "WorkerPool created with {} tasks".format(pool_size)
        print "Each Thread will pool in {} sec for tasks".format(wait_time)
        print "Each Thread will maximum try {} times to take task then automaitically dies.".format(max_try)
        self.pool_size = pool_size                # This is how many threads we want by Default
        self.wait_time = wait_time        # This is how much time thread should wait if queue is empty
        self.max_try = max_try                          # This is maximum number of try a thread will and then go dead
        self.tasks = Queue(100)
        self.processors = []
        self._type = ""

        # Spawn the threads
        if is_process and not is_threaded:
            self.worker = ProcessWorker
            self._type = "process"
        else:
            self._type = "thread"
            self.worker = ThreadWorker

        print "Spawning the {} {}.".format(self.pool_size, self._type)
        for x in xrange(self.pool_size):
            print "{} {} created.".format(self._type, x)
            # This is the thread class that we instantiate.
            self.processors.append(self.worker(self.tasks, self.max_try, self.wait_time))

        if default_start:
            self.start_processing()

    def start_processing(self):
        try:
            x = 1
            for processor in self.processors:
                print "{} {} started.".format(self._type, x)
                x += 1
                processor.start()
        except Exception, e:
            print "WorkerPool already Started"
            raise e


    def stop_all(self):
        try:
            x = 1
            for processor in self.processors:
                print "{} {} started.".format(self._type, x)
                x += 1
                processor.stop()
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

    def task_is_empty(self):
        return self.tasks.empty()
