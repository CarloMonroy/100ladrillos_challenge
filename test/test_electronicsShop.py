from challenges.electronicsShop import electronicsShop

def test_electronicsShop():
    assert electronicsShop([3,1], [5,2,8], 10) == 9
    assert electronicsShop([4], [4], 5) == -1
    assert electronicsShop([4], [5], 4) == -1
    assert electronicsShop([40, 50, 60], [5, 8, 12], 60) == 58