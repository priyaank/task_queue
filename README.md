TaskQueue - Python Task Queue
==============================

Task_Queue is a Python based task queue implementation that uses a worker pool to execute tasks in parallel. 
Workers can run in a single process, multiple processes, single thread or multi threaded mode. 


	Task.
	It's an abstract base class, from which you have to derive your own task classes
	by overriding the run() - method like in the following example.

        
    class MultiplyTask(Task):

        """docstring for MultiplyTask"""

        def __init__(self, a, b):
            super(Task, self).__init__()
            self.a = a
            self.b = b

        def run(self):
            print self.a*self.b


	WorkerPool.
	It creates pool of workes to execute our task that we add.

    WorkerPool Provided options

    is_thread=True       	WorkerPool would be multithreaded, By default it create multiprocessed
    pool_size=3          	You can define number of process and threads to run in parellel, By Default its value is 3.
    wait_time=1          	You can specify wait time for next pool if TaskQueue is Empty, By Default its value s 1.
    max_try=12           	You can specify max_try a worker would try to find task in queue else die.
    				By Default its value is 12.
    default_start=True   	You can also just initialize WorkerPool without starting workers to start working.
				By default its value is True.


Example to Create Multithreaded WorkerPool

	test_worker = WorkerPool(is_thread=True)


Example to Create MultiProcessed WorkerPool

	test_worker = WorkerPool()


Example to Add Multiple Task in TaskQueue
     
	task1 = MultiplyTask(5,7)
	task2 = MultiplyTask(5,7)
	test_worker.add_tasks([task1, tas2])


To Test TaskQueue, Try Running try_it.py

