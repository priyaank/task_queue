# threading queue test
# Priyaank Choubey - mail@priyaank.com

import time
import unittest2 as unittest
from unittest2 import TestCase
from task.worker_pool import WorkerPool


class WorkerPool_TC(TestCase):

    def test_11_init_process_worker_pass(self):
        try:
            WorkerPool(default_start=False)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_12_process_worker_size_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False)
            pool_size = len(worker.processors)
            self.assertEqual(pool_size,1)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_13_process_worker_start_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0)
            worker.start_processing()
            worker.stop_all()
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_14_process_queue_len_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_15_process_task_add_pass(self):
        try:
            worker = WorkerPool(default_start=False, wait_time=0)
            worker.add_tasks([(5,3),(6,4)])
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,False)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_16_process_task_processing(self):
        try:
            worker = WorkerPool(wait_time=0)
            worker.add_tasks([(5,3)])
            worker.stop_all()
            time.sleep(4)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_21_threaded_init_worker_pass(self):
        try:
            WorkerPool(default_start=False, is_threaded=True)
        except RuntimeError as e:
            self.fail("Unexpected failure")


    def test_22_threaded_worker_size_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, is_threaded=True)
            pool_size = len(worker.processors)
            self.assertEqual(pool_size,1)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_23_threaded_worker_start_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0, is_threaded=True)
            worker.start_processing()
            worker.stop_all()
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_24_threaded_queue_len_pass(self):
        try:
            worker = WorkerPool(pool_size=1, default_start=False, wait_time=0, is_threaded=True)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_25_threaded_task_add_pass(self):
        try:
            worker = WorkerPool(default_start=False, wait_time=0, is_threaded=True)
            worker.add_tasks([(5,3),(6,4)])
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,False)
        except RuntimeError as e:
            self.fail("Unexpected failure")

    def test_26_threaded_task_processing(self):
        try:
            worker = WorkerPool(wait_time=0, is_threaded=True)
            worker.add_tasks([(5,3)])
            worker.stop_all()
            time.sleep(4)
            is_empty = worker.task_is_empty()
            self.assertEqual(is_empty,True)
        except RuntimeError as e:
            self.fail("Unexpected failure")



if __name__ == '__main__':
    unittest.main(verbosity=2)
