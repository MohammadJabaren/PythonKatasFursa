
import unittest
from io import StringIO
from unittest.mock import patch
from katas.do_n_times import do_n_times,say_hello,print_message


class TestDoFuncNTime(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_n_times_say_hello(self,mock_stdout):

        do_n_times(say_hello, 5)
        output = mock_stdout.getvalue().strip().split('\n')

        self.assertEqual(len(output), 5)
        self.assertEqual(output[0], "Hello!")
        self.assertEqual(output[1], "Hello!")
        self.assertEqual(output[2], "Hello!")
        self.assertEqual(output[3], "Hello!")
        self.assertEqual(output[4], "Hello!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_n_times_print_message(self,mock_stdout):


        do_n_times(print_message, 4)
        output = mock_stdout.getvalue().strip().split('\n')

        self.assertEqual(len(output), 4)
        self.assertEqual(output[0], "Python is fun!")
        self.assertEqual(output[1], "Python is fun!")
        self.assertEqual(output[2], "Python is fun!")
        self.assertEqual(output[3], "Python is fun!")

