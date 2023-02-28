



def electronicsShop(keyboards, drives, b):

    not_enough_money = -1

    for i in keyboards:
        for j in drives:
            if i+j <= b:
                not_enough_money = max(not_enough_money, i+j)

    return not_enough_money


print(electronicsShop([3, 1], [5, 2, 8], 10))
