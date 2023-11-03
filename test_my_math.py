# test_my_math.py
import unittest
import my_math  # Import modul yang ingin diuji

class TestMyMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_math.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(my_math.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(my_math.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(my_math.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            my_math.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
