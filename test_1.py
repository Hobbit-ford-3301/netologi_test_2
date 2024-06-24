import unittest
from p import flatiterator

class TestNextItem(unittest.TestCase):

    def test_next_item(self):
        list_of_lists = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]
        flat_iter = flatiterator(list_of_lists)

        for check_item in ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]:
            self.assertEqual(next(flat_iter), check_item)

if __name__ == '__main__':
    unittest.main()
     # проверка получения следующего элемента 