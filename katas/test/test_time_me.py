import unittest
import time
from katas.time_me import measure_execution_time
from katas.time_me import quick_function
from katas.time_me import sample_function


class TestTimeFunc(unittest.TestCase):

    def test_sample_function_time(self):
        func_time = measure_execution_time(sample_function)
        self.assertAlmostEqual(func_time,500,None,None,50)

    def test_another_sample_function_time(self):
        func_time = measure_execution_time(lambda:time.sleep(1.0))
        self.assertAlmostEqual(func_time,1000,None,None,50)

    def test_quick_function_time(self):
        func_time = measure_execution_time(quick_function)
        self.assertLess(func_time, 1)