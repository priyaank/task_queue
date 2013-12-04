# threading queue test
# Priyaank Choubey - mail@priyaank.com

import time
from task.worker_pool import WorkerPool

#
# Executes if the program is started normally, not if imported
#

SAMPLE_INPUT_TASKS = [ (5,5),(10,4),(78,5),(87,2),(65,4),(10,10),(65,2),(88,95),(44,55),(33,3) ]
def sample_run1():
    test_worker = WorkerPool(is_threaded=True)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    time.sleep(3)
    #worker_test.add_tasks(inputlist_ori)
    #worker_test.stop_all()

def sample_run2():
    test_worker = WorkerPool()
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    time.sleep(8)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    #worker_test.stop_all()

def sample_run3():
    test_worker = WorkerPool(is_threaded=True, wait_time=0, pool_size=2, max_try=1)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)


def sample_run4():
    test_worker = WorkerPool(max_try=1, wait_time=0, pool_size=2)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)

if __name__ == '__main__':
    #sample_run1()
    #sample_run2()
    print "Try running Threaded WorkerPool"
    sample_run3()
    time.sleep(25)
    print "Try running Process WorkerPool"
    sample_run4()

