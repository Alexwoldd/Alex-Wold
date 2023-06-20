# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Alexandra Wold>
<MTH 420>
<4/28>
"""

import numpy as np
def prob1():
    A = np.array([[3,-1,4],[1,5,-9]])
    B = np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
    return(A@B)


def prob2():
    A = np.array([[3,1,4],[1,5,9],[-5,3,1]])
    B = -1*((A@A)@A)
    C = 9*(A@A)
    D = -15*A
    return(B+C+D)


def prob3():
    A = np.ones((7,7))
    A = np.triu(A)
    print(A)
    B1 = np.full((7,7),-1)
    B2 = np.full((7,7),5)
    B = np.tril(B1) + np.triu(B2) + -5*np.eye(7,7)
    print(B)
    C = ((A@B)@A)
    return C.astype(np.int64)



def prob4(A):
    AC = np.copy(A)
    negatives = AC<0
    AC[negatives] = 0
    return(AC)


def prob5():
    A=np.array([[0,2,4],[1,3,5]])
    B=np.array([[3,0,0],[3,3,0],[3,3,3]])
    C=np.array([[-2,0,0],[0,-2,0],[0,0,-2]])
    AT=A.T

    return C


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    raise NotImplementedError("Problem 6 Incomplete")


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")
