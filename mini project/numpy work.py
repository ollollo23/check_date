import numpy as np


def jakkar(expert1, expert2):
    one = (expert1 == True) & (expert2 == True)
    all_true = one[one == True]
    e1_true = expert1[expert1 == True]
    e2_true = expert2[expert2 == True]
    A_B = all_true.size
    A = e1_true.size
    B = e2_true.size
    return A_B / (A + B - A_B)


expert1 = np.array([[True, False, False, True, True],
                    [False, True, False, False, True],
                    [True, True, True, False, False]])

expert2 = np.array([[True, False, False, False, True],
                    [False, False, False, False, False],
                    [True, False, True, False, False]])

essay = np.array([["pass", "not pass", "not pass", "not pass", "pass"],
                  ["not pass", "not pass", "not pass", "not pass", "not pass"],
                  ["pass", "not pass", "pass", "not pass", "not pass"]])

Jakkarta = jakkar(expert1, expert2)

print(Jakkarta)
