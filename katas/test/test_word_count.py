import unittest
from katas.word_count import count_words

class TestWordsCounter(unittest.TestCase):
    def test_empty_string(self):

        self.assertEqual(count_words("                 "), 0)


    def test_symbols_string(self):

        self.assertEqual(count_words(" @#@$!@#$@%#$^$%&%*^&(^&(&*)*+___"), 0)

    def test_number_string(self):

        self.assertEqual(count_words("453 5255 45823 48522 5455"), 0)

    def test_single_word(self):

        self.assertEqual(count_words("Hello"), 1)

    def test_multiple_underscores(self):

        self.assertEqual(count_words("Hello_world_my_name_is_mohammad"), 6)

    def test_complete_sentence(self):
        self.assertEqual(count_words("I have 99 problems, but a code ain't one!"), 8)

    def test_hello_word(self):

        self.assertEqual(count_words("Hello world"), 2)

    def test_another_complete_sentence(self):
        self.assertEqual(count_words("Hi,my name is mohammad! and this my email address mohammad.eek@gmail.com"), 14)


