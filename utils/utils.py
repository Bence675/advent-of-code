
import numpy as np
from enum import Enum
from inspect import signature

class Neighbor(Enum):
    SIDE = 0,
    CORNER = 1,
    CORNER_AND_SIDE = 2



def shape(matrix):
    """
    Returns the shape of the given object.
    Parameters:
    matrix (list, tuple, np.ndarray, or str): The input matrix whose shape is to be determined. 
                                              It can be a list, tuple, numpy ndarray, or string.
    Returns:
    tuple: A tuple representing the shape of the matrix. For lists and tuples, it returns the dimensions 
           of the nested lists/tuples. For numpy ndarrays, it returns the shape attribute. For strings, 
           it returns a tuple with the length of the string.
    Raises:
    ValueError: If the input matrix is not of a supported type.
    """
    if type(matrix) == tuple:
        matrix = list(matrix)
    if type(matrix) == list:
        try:
            res = [len(matrix)] + list(shape(matrix[0]))
        except ValueError:
            res = [len(matrix)]
        if type(matrix) == str:
            res.append(len(matrix))
        return tuple(res)
        
    elif type(matrix) == np.ndarray:
        return matrix.shape
    elif type(matrix) == str:
        return (len(matrix),)
    else:
        raise ValueError("Invalid matrix type:", type(matrix))


def is_index_in_matrix(index, matrix, debug = False):
    if type(index) == tuple:
        try:
            return all([index[i] >= 0 and index[i] < shape(matrix)[i] for i in range(len(index))])
        except IndexError as e:
            if debug:
                print("Number of dimensions of index does not match the number of dimensions of the matrix"
                      "index:", index, "matrix:", matrix, "index shape:", shape(index), "matrix shape:", shape(matrix))
            return False
    elif type(index) == int:
        return index >= 0 and index < len(matrix)
    else:
        raise ValueError("Invalid index type")
    

def run_function_on_neighbors(matrix, i, j, function, debug = False, method = Neighbor.SIDE):
    res = []
    neighbors = []
    if method == Neighbor.SIDE:
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    elif method == Neighbor.CORNER:
        neighbors = [(i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)]
    elif method == Neighbor.CORNER_AND_SIDE:
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)]

    for i_, j_ in neighbors:
        if is_index_in_matrix((i_, j_), matrix, debug):
            if len(list(signature(function).parameters)) == 3:
                res.append(function(matrix, i_, j_))
            elif len(list(signature(function).parameters)) == 1:
                res.append(function(matrix[i_][j_]))
            elif len(list(signature(function).parameters)) == 2:
                res.append(function(i_, j_))
            else:
                raise ValueError("Invalid number of parameters for function")
    return res

def product(arr):
    res = 1
    for a in arr:
        res *= a
    return res