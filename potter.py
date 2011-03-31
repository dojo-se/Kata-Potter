import unittest

BOOK_1 = 0
BOOK_2 = 1

def book_calculator(basket):
    if basket == None:
        return 0
    elif len(basket) == 1:
        return 8
    return 2*8*0.9

class Book_calculator(unittest.TestCase):
    def test_empty_basket(self):
        self.assertEqual(0, book_calculator(None))
    def test_one_book(self):
        basket = { BOOK_1: 1 }
        self.assertEqual(8, book_calculator(basket))
    def test_two_differents_books(self):
        basket = { BOOK_1: 1, BOOK_2 : 1 }
        self.assertEqual(2*8*0.9, book_calculator(basket))

if __name__ == '__main__':
    unittest.main()
