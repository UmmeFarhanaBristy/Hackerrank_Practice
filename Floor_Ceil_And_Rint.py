import numpy as np
np.set_printoptions(sign=' ')

ar = np.array(input().split(' '), float)

print(np.floor(ar))
print(np.ceil(ar))
print(np.rint(ar))
