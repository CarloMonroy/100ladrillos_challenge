## import diagonalDifference
from challenges.diagonalDifference import diagonalDifference


def test_diagonalDifference():
    assert diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]) == 2
    assert diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]) == 15
    assert diagonalDifference([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 0
    assert diagonalDifference([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == 0
