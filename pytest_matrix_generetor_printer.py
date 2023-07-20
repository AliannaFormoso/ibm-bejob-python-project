import pytest
from matrix_generator_printer import gen_matrix, add_row_column

def test_gen_matrix():
    matrix = gen_matrix(6)
    assert len(matrix) == 6
    for row in matrix:
        assert len(row) == 6


def test_add_row_column():
    matrix = [[9, 9, 3], [4, 1, 5], [2, 7, 6]]
    add_row, add_column = add_row_column(matrix)
    assert add_row == [21, 10, 15]
    assert add_column == [13, 17, 14]


if __name__ == "__main__":
    pytest.main()