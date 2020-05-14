import numpy as np


def govnoshape(massiv, a, b):
    odnomer = massiv.flatten()
    if (a * b) == odnomer.size:
        new = np.zeros((a, b))
        on = 0
        tw = 0
        for value in odnomer:
            if tw < b and on < a:
                new[on][tw] = value
                tw += 1
            else:
                tw = 0
                on += 1
                new[on][tw] = value
                tw += 1
    else:
        new = 'количество символов в сходном массиве не соответствует новым параметрам'
    return new


expert1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

po = np.array([[2, 5, 7],
               [4, 4, 6],
               [1, 2, 4],
               [4, 8, 4],
               [2, 3, 7],
               [4, 7, 3]])

heh = govnoshape(po, 3, 6)

print(heh)
