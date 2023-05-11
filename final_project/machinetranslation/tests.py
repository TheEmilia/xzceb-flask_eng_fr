import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), "Invalid submission") # test when None (A null value) is given as input the output is "Invalid submission"
        self.assertEqual(english_to_french(""), "Invalid submission") # test when an empty string is given as input the output is "Invalid submission"
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when "Hello" is given as input the output is "Bonjour"
        self.assertEqual(english_to_french("Restaurant"), "Restaurant") # test when "Restaurant" is given as input the output is "Restaurant"

        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), "Invalid submission") # test when None (A null value) is given as input the output is "Invalid submission"
        self.assertEqual(french_to_english(""), "Invalid submission") # test when an empty string is given as input the output is "Invalid submission"
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when "Bonjour" is given as input the output is "Hello"
        self.assertEqual(french_to_english("Restaurant"), "Restaurant") # test when "Restaurant" is given as input the output is "Restaurant"
        

unittest.main()