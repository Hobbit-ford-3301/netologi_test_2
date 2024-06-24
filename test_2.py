import unittest
from p import flatiterator

class TestIteratorCreation(unittest.TestCase):

    def test_iterator_instance(self):
        list_of_lists = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]
        flat_iter = flatiterator(list_of_lists)
        self.assertIsInstance(flat_iter, flatiterator)

if __name__ == '__main__':
    unittest.main()
    # проверка создания итератора
