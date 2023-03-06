import matplotlib.pyplot as plt
import numpy as np

I = np.zeros(1000)
I[0] = 1

for i in range(1, 1000):
    I[i] = (106 * I[i-1] + 1283) % 6075

plt.scatter(I[:-1], I[1:], s=2)
plt.title("Plot of I_j+1 vs I_j for N = 1000")
plt.xlabel('I_j')
plt.ylabel('I_j+1')
plt.show()
