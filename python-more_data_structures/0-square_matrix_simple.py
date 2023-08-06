def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = [elem ** 2 for elem in row]
        result.append(squared_row)
    return result