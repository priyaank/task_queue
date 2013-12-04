# threading queue test
# Priyaank Choubey - mail@priyaank.com

import time
import unittest2 as unittest
from unittest2 import TestCase
from task.thread import WorkerPool

class WorkerPool_TC(TestCase):

    def test_1init_worker_pass(self):
        try:
            WorkerPool(default_start=False)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_2_worker_size_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False)
            pool_size = worker.pool_size()
            self.assertEqual(pool_size,1)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_3_worker_start_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False)
            worker.start_processing()
            worker.stop_all()
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_queue_len_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False)
            queue_size = worker.task_in_queue()
            self.assertEqual(queue_size,0)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_task_add_pass(self):
        try:
            worker = WorkerPool(default_start=False)
            worker.add_tasks([(5,3),(6,4)])
            queue_size = worker.task_in_queue()
            self.assertEqual(queue_size,2)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_task_processing(self):
        try:
            worker = WorkerPool()
            worker.add_tasks([(5,3)])
            worker.stop_all()
            time.sleep(4)
            queue_size = worker.task_in_queue()
            self.assertEqual(queue_size,0)
        except RuntimeError as e:
            self.fail("Unexpected failure")





if __name__ == '__main__':
    unittest.main(verbosity=2)
