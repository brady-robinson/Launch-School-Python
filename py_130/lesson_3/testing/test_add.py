import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    @unittest.skip
    def test_add_fail(self):
        self.assertEqual(add(1, 2), 4)

if __name__ == '__main__':
    unittest.main()