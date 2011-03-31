import unittest

def book_calculator(basket):
    return 0

class Book_calculator(unittest.TestCase):
    def test_empty_basket(self):
        self.assertEqual(0, book_calculator(None))

if __name__ == '__main__':
    unittest.main()
