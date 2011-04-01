import unittest

def book_calculator(basket):
    if basket == None:
        return 0
    elif len(basket) == 1:
        return 8
    elif  len(basket) == 2:
        return 2*8*0.95
    elif len(basket) == 3:
        return 3*8*0.9


class Book_calculator(unittest.TestCase):

    def test_empty_basket(self):
        basket = None
        self.assertEqual(0, book_calculator(basket))

    def test_one_book(self):
        basket = { "Book 1": 1 }
        self.assertEqual(8, book_calculator(basket))

    def test_two_different_books(self):
        basket = { "Book 1": 1, "Book 2": 1 }
        self.assertEqual(2*8*0.95, book_calculator(basket))

    def test_three_different_books(self):
        basket = { "Book 1": 1, "Book 2": 1, "Book 3": 1 }
        self.assertEqual(3*8*0.9, book_calculator(basket))

if __name__ == '__main__':
    unittest.main()
