import numpy as np

expert1 = np.array([[True, False, False, True, True],
                    [False, True, False, False, True],
                    [True, True, True, False, False]])

expert2 = np.array([[True, False, False, False, True],
                    [False, False, False, False, False],
                    [True, False, True, False, False]])

one = (expert1 == True) & (expert2 == True)

sum = one[one == True]

print(sum.size)

two = expert1 & expert2
print(two.sum())
