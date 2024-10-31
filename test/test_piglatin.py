import unittest
from piglatin import PigLatin
from error import PigLatinError


import unittest
from PigLatinTranslator import PigLatinTranslator

class TestPigLatinTranslator(unittest.TestCase):
    def test_get_phrase(self):

        translator = PigLatinTranslator("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_translate_empty_phrase(self):

        translator = PigLatinTranslator("")
        self.assertEqual(translator.translate(), "nil")

if __name__ == "__main__":
    unittest.main()

