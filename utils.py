
import numpy as np



def shape(matrix):
    if type(matrix) == list:
        res = []
        while type(matrix) == list:
            res.append(len(matrix))
            matrix = matrix[0]
        return tuple(res)
        
    elif type(matrix) == np.ndarray:
        return matrix.shape
    else:
        raise ValueError("Invalid matrix type")


def is_index_in_matrix(index, matrix):
    if type(index) == tuple:
        try:
            return all([index[i] >= 0 and index[i] < shape(matrix)[i] for i in range(len(index))])
        except IndexError:
            print("Number of dimensions of index does not match the number of dimensions of the matrix")
    elif type(index) == int:
        return index >= 0 and index < len(matrix)
    else:
        raise ValueError("Invalid index type")