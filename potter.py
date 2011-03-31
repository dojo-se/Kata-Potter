import unittest
BOOK_1 = 0

def book_calculator(basket):
    if basket == None:
        return 0
    return 8

class Book_calculator(unittest.TestCase):
    def test_empty_basket(self):
        self.assertEqual(0, book_calculator(None))
    def test_one_book(self):
        self.assertEqual(8, book_calculator({ BOOK_1: 1 }))

if __name__ == '__main__':
    unittest.main()
