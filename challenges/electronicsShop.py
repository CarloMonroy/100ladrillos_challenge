



def electronicsShop(keyboards, drives, b):

    spent = -1

    for i in keyboards:
        for j in drives:
            if i+j <= b:
                spent = max(spent, i+j)

    return spent