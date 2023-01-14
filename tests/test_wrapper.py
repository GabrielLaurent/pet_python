# tests/test_wrapper.py

import unittest
from pet.wrapper import PetWrapper

class TestPetWrapper(unittest.TestCase):

    def setUp(self):
        self.wrapper = PetWrapper()

    def test_some_function(self):
        self.assertEqual(self.wrapper.some_function("test"), "test")

if __name__ == '__main__':
    unittest.main()