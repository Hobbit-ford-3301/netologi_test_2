import unittest
from p import flatiterator

class TestListConversion(unittest.TestCase):

    def test_list_conversion(self):
        list_of_lists = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]
        flat_iter = flatiterator(list_of_lists)

        self.assertEqual(list(flat_iter), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None])

if __name__ == '__main__':
    unittest.main()
    # проверка преобразования итератора в список.