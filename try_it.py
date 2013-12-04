# threading queue test
# Priyaank Choubey - mail@priyaank.com

import time
from task.thread import WorkerPool

#
# Executes if the program is started normally, not if imported
#

SAMPLE_INPUT_TASKS = [ (5,5),(10,4),(78,5),(87,2),(65,4),(10,10),(65,2),(88,95),(44,55),(33,3) ]
def sample_run1():
    test_worker = WorkerPool()
    print "Tasks in Queue before adding Sample Tasks {}".format(test_worker.task_in_queue())
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    print "Tasks in Queue after adding Sample Tasks {}".format(test_worker.task_in_queue())
    time.sleep(3)
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    #worker_test.add_tasks(inputlist_ori)
    #worker_test.stop_all()

def sample_run2():
    test_worker = WorkerPool()
    print "Tasks in Queue before adding Sample Tasks {}".format(test_worker.task_in_queue())
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    print "Tasks in Queue after adding Sample Tasks {}".format(test_worker.task_in_queue())
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    time.sleep(8)
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    #worker_test.stop_all()

def sample_run3():
    test_worker = WorkerPool()
    print "Tasks in Queue before adding Sample Tasks {}".format(test_worker.task_in_queue())
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    print "Tasks in Queue after adding Sample Tasks {}".format(test_worker.task_in_queue())
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    time.sleep(8)
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    print "Stopped Tasks Processing."
    print "Tasks in Queue {}".format(test_worker.task_in_queue())
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    test_worker.add_tasks(SAMPLE_INPUT_TASKS)
    print "Tasks in Queue {}".format(test_worker.task_in_queue())

if __name__ == '__main__':
    #sample_run1()
    #sample_run2()
    sample_run3()
