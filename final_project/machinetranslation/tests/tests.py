import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english_null(self):
        self.assertIsNone(french_to_english(None))

    def test_english_to_french_null(self):
        self.assertIsNone(english_to_french(None))

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    

if __name__ == '__main__':
    unittest.main()