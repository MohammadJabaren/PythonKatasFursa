
def swap(matrix,i,j):
    tmp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = tmp





def rotate_matrix(matrix):
    """
    Rotates the given square matrix 90 degrees clockwise in place.

    Args:
        matrix: the 2D square matrix to rotate
    """
    row = len(matrix)
    matrix[:] = matrix[::-1]

    for i in range(row):
        for j in range(i+1,row):
            swap(matrix,i,j)
    return matrix


def print_matrix(matrix):
    """
    Helper function to print a 2D matrix.

    Args:
        matrix: the matrix to print
    """
    for row in matrix:
        print(' '.join(str(value) for value in row))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)
    rotate_matrix(matrix)
    print("Matrix after 90-degree clockwise rotation:")
    print_matrix(matrix)

    # Expected output:
    # Original Matrix:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Matrix after 90-degree clockwise rotation:
    # 7 4 1
    # 8 5 2
    # 9 6 3
