import unittest

class TestExercises(unittest.TestCase):
    def test_bool(self):
        self.assertTrue(101 % 2 != 0)

    def test_assert(self):
        self.assertEqual('XYZ'.lower(), 'xyz')

    def test_none(self):
        self.assertIsNone(None)

    def test_list(self):
        self.assertIn('xyz',['xyz'])

    def test_not_list(self):
        self.assertNotIn('xyz',[])

    def test_is(self):
        self.assertIs([1], [1])

    # def test_instance(self):
    #     self.assertIsInstance(1, Numeric)

    # def test_error(self):
    #     with self.assertRaises(NoExperienceError):
    #         employee.hire()

if __name__ == '__main__':
    unittest.main()