# threading queue test
# Priyaank Choubey - mail@priyaank.com

import time
from task_queue.task import Task
from task_queue.core import WorkerPool

#
# Executes if the program is started normally, not if imported
#


class MultiplyTask(Task):
    """docstring for MultiplyTask"""
    def __init__(self, a, b):
        super(Task, self).__init__()
        self.a = a
        self.b = b

    def run(self):
        print self.a*self.b


a = MultiplyTask(10,20)

SAMPLE_INPUT_TASKS = [ (5,5),a ]

test_worker = WorkerPool(is_thread=True)
test_worker.add_tasks(SAMPLE_INPUT_TASKS)
