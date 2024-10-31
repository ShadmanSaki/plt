class PigLatin:

    def __init__(self, phrase: str):
        pass

    def get_phrase(self) -> str:
        pass

    def translate(self) -> str:
        pass




class PigLatinTranslator:
    def __init__(self, phrase: str):

        self._phrase = phrase

    def get_phrase(self) -> str:

        return self._phrase

import unittest
from PigLatinTranslator import PigLatinTranslator

class TestPigLatinTranslator(unittest.TestCase):
    def test_get_phrase(self):

        translator = PigLatinTranslator("hello world")

        self.assertEqual(translator.get_phrase(), "hello world")

if __name__ == "__main__":
    unittest.main()

from PigLatinTranslator import PigLatinTranslator

translator = PigLatinTranslator("This is a phrase")
phrase = translator.get_phrase()
print("Original Phrase:", phrase)
