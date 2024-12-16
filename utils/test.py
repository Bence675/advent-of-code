
import unittest
from utils import *

class TestShape(unittest.TestCase):
    def test_tuple_shape(self):
        self.assertEqual(shape((1, 2, 3)), (3,))
        self.assertEqual(shape((1, 2, 3, 4)), (4,))

    def test_list_shape(self):
        self.assertEqual(shape([1, 2, 3]), (3,))
        self.assertEqual(shape([1, 2, 3, 4]), (4,))
        self.assertEqual(shape([[1, 2, 3], [4, 5, 6]]), (2, 3))
        self.assertEqual(shape([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]), (2, 3, 3))

    def test_np_shape(self):
        self.assertEqual(shape(np.array([1, 2, 3])), (3,))
        self.assertEqual(shape(np.array([1, 2, 3, 4])), (4,))
        self.assertEqual(shape(np.array([[1, 2, 3], [4, 5, 6]])), (2, 3))
        self.assertEqual(shape(np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])), (2, 3, 3))

    def test_str_shape(self):
        self.assertEqual(shape("abc"), (3,))
        self.assertEqual(shape("abcd"), (4,))

        

class TestIsIndexInMatrix(unittest.TestCase):
    def test_tuple_index(self):
        self.assertTrue(is_index_in_matrix((1, 1), [[1, 2], [3, 4]]))
        self.assertTrue(is_index_in_matrix((1, 1), ((1, 2), (3, 4))))
        self.assertFalse(is_index_in_matrix((1, 2), [[1, 2], [3, 4]]))
        self.assertFalse(is_index_in_matrix((2, 1), [[1, 2], [3, 4]]))
        self.assertFalse(is_index_in_matrix((2, 2), [[1, 2], [3, 4]]))
        self.assertFalse(is_index_in_matrix((0, -1), [[1, 2], [3, 4]]))
        self.assertFalse(is_index_in_matrix((-1, 0), [[1, 2], [3, 4]]))
        self.assertFalse(is_index_in_matrix((-1, -1), [[1, 2], [3, 4]]))

    def test_int_index(self):
        self.assertTrue(is_index_in_matrix(1, [1, 2, 3]))
        self.assertFalse(is_index_in_matrix(3, [1, 2, 3]))
        self.assertFalse(is_index_in_matrix(-1, [1, 2, 3]))

    def test_invalid_index(self):
        with self.assertRaises(ValueError):
            is_index_in_matrix("a", [[1, 2], [3, 4]])



if __name__ == "__main__":
    unittest.main()