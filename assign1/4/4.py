import numpy as np
from scipy.linalg import lstsq
b = np.array([1.23, 4.45, 1.61, 3.21, 0.45, -2.75, 2.95, 1.74, -1.45, 1.32])
b = b.reshape(-1, 1)
A = np.array([
    [1, -1, 0, 0],
    [1, 0, -1, 0],
    [1, 0, 0, -1],
    [0, 1, -1, 0],
    [0, 1, 0, -1],
    [0, 0, 1, -1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
ans,w1,w2,w3=lstsq(A, b)
print(ans)
