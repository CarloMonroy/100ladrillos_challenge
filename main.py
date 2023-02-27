import numpy as np ##For matrix manipulation



def diagonalDifferente(matrix):
    '''
    PYTHONIC
    takes: matrix list of lists
    returns: absolute value of difference between sum of diagonal and sum of inverse diagonal
    '''
    diag = np.diag(matrix)
    inverseDiag = np.diag(np.fliplr(matrix)) ##Diag of flipped matrix
    diag = [int(i) for i in diag] ##Convert to int
    inverseDiag = [int(i) for i in inverseDiag]

    return abs(sum(diag)-sum(inverseDiag)) ##Return absolute value of difference


def diagonalDifferente2(matrix):
    '''
    NON-PYTHONIC
    NON-NUMPY
    takes: matrix list of lists
    returns: absolute value of difference between sum of diagonal and sum of inverse diagonal
    '''
    diag = []
    inverseDiag = []
    for i in range(len(matrix)):
        diag.append(matrix[i][i]) ##Get diagonal
        inverseDiag.append(matrix[i][len(matrix)-i-1]) ##Get inverse diagonal

    return abs(sum(diag)-sum(inverseDiag)) ##Return absolute value of difference


array = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print(diagonalDifferente(array))
print(diagonalDifferente2(array))