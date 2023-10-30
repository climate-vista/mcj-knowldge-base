import unittest
from src import main

class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_sample(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()