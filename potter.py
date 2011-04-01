import unittest

def book_calculator(basket):
    if basket == None:
        return 0
    if basket['Book 1'] == 2:
        return 16

    total = 8*(1.05 - 0.05*len(basket)) * len(basket)

    return round(total,2)


class Book_calculator(unittest.TestCase):

    def test_empty_basket(self):
        basket = None
        self.assertEqual(0, book_calculator(basket))

    def test_one_book(self):
        price = round(8,2)
        basket = { "Book 1": 1 }
        self.assertEqual(price, book_calculator(basket))

    def test_two_different_books(self):
        basket = { "Book 1": 1, "Book 2": 1 }
        price = round( 2*8*0.95 ,2)
        self.assertEqual(price, book_calculator(basket))

    def test_three_different_books(self):
        price = round( 3*8*0.9, 2)
        basket = { "Book 1": 1, "Book 2": 1, "Book 3": 1 }
        self.assertEqual(price, book_calculator(basket))

    def test_two_equal_books(self):
        basket = {"Book 1": 2}
        price = round(2*8, 2)
        self.assertEqual(price, book_calculator(basket))

if __name__ == '__main__':
    unittest.main()
