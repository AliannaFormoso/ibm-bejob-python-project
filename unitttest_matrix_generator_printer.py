import unittest
from matrix_generator_printer import gen_matrix, add_row_column

class TestMatrixGeneratorPrinter(unittest.TestCase):

    def test_gen_matrix(self):
        matrix = gen_matrix(5)
        self.assertEqual(len(matrix),5)
        for row in matrix:
            self.assertEqual(len(row), 5)

    def test_gen_matrix_notequal(self):
        matrix = gen_matrix(2)
        self.assertNotEqual(len(matrix),3)
        for row in matrix:
            self.assertNotEqual(len(row), 4)

    def test_add_row_column(self):
        matrix = [[1,2,3,4], [4,3,2,1],[5,6,7,8], [8,7,6,5]]
        add_rows, add_columns = add_row_column(matrix)
        self.assertEqual(add_rows, [10, 10, 26, 26])
        self.assertEqual(add_columns, [18, 18, 18, 18])

    def test_add_row_column_notequal(self):
        matrix = [[1,2,3,4], [4,3,2,1],[5,6,7,8], [8,7,6,5]]
        add_rows, add_columns = add_row_column(matrix)
        self.assertNotEqual(add_rows, [20, 30, 16, 46])
        self.assertNotEqual(add_columns, [38, 11, 88, 19])

if __name__ == "__main__":
    unittest.main()

