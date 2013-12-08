# threading queue test
# Priyaank Choubey - mail@priyaank.com

from multiprocessing import Queue

TaskQueue = Queue
#class TaskQueue(Queue):

    #def __init__(self):
    #    Queue.__init__(self)
    #    self.all_tasks_done = threading.Condition(self.mutex)
    #    self.unfinished_tasks = 0

    #def _put(self, item):
    #    Queue._put(self, item,)
    #    self.unfinished_tasks += 1

    #def _get():
    #    Queue._get(True)
    #    self.unfinished_tasks -= 1


    #def task_done(self):
    #    self.all_tasks_done.acquire()
    #    try:
    #        unfinished = self.unfinished_tasks - 1
    #        if unfinished <= 0:
    #            if unfinished < 0:
    #                raise ValueError('task_done() called too many times')
    #            self.all_tasks_done.notifyAll()
    #        self.unfinished_tasks = unfinished
    #    finally:
    #        self.all_tasks_done.release()

    #def join(self):
    #    self.all_tasks_done.acquire()
    #    try:
    #        while self.unfinished_tasks:
    #            self.all_tasks_done.wait()
    #    finally:
    #        self.all_tasks_done.release()

    #def _get():
        #if Queue._get(False)
        #    self.unfinished_tasks -= 1
        #else:
        #    getTaskFromPE()

    #def getTaskFromPE():
        #peNum = getPENum()
        #queue = getQueue(peNum)
        #queue._getFromTail(True)
