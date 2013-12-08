# threading queue test
# Priyaank Choubey - mail@priyaank.com

import time
import unittest2 as unittest
from unittest2 import TestCase
from task_queue.task import Task
from task_queue.core import WorkerPool

class MultiplyTask(Task):
    """docstring for MultiplyTask"""
    def __init__(self, a, b):
        super(Task, self).__init__()
        self.a = a
        self.b = b

    def run(self):
        print self.a*self.b

class WorkerPool_TC(TestCase):

    def test_11_init_process_worker_pass(self):
        try:
            WorkerPool(default_start=False)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_12_process_worker_size_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, max_try=1)
            pool_size = len(worker.workers)
            self.assertEqual(pool_size,1)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_13_process_worker_start_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0, max_try=1)
            worker.start_processing()
            worker.stop_all()
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_14_process_queue_len_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0,max_try=1)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_15_process_task_add_pass(self):
        try:
            worker = WorkerPool(default_start=False, wait_time=0, max_try=3)
            worker.add_tasks([MultiplyTask(5,6), MultiplyTask(20,10)])
            time.sleep(3)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,False)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_16_process_task_processing(self):
        try:
            worker = WorkerPool(wait_time=0, max_try=3)
            worker.add_tasks([MultiplyTask(5,6)])
            worker.stop_all()
            time.sleep(4)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_21_threaded_init_worker_pass(self):
        try:
            WorkerPool(default_start=False, is_thread=True)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_22_threaded_worker_size_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, is_thread=True)
            pool_size = len(worker.workers)
            self.assertEqual(pool_size,1)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_23_threaded_worker_start_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0, max_try=1, is_thread=True)
            worker.start_processing()
            worker.stop_all()
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_24_threaded_queue_len_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0, is_thread=True)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_25_threaded_task_add_pass(self):
        try:
            worker = WorkerPool(default_start=False, wait_time=0, is_thread=True)
            worker.add_tasks([MultiplyTask(5,6)])
            time.sleep(3)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,False)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_26_threaded_task_processing(self):
        try:
            worker = WorkerPool(wait_time=0, is_thread=True, max_try=2)
            worker.add_tasks([(5,3),(6,4)])
            worker.stop_all()
            time.sleep(4)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")



if __name__ == '__main__':
    unittest.main(verbosity=2)
