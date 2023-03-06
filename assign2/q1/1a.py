import matplotlib.pyplot as plt
import numpy as np


I = np.zeros(1000)
I[0] = 1

for i in range(1, 1000):
    I[i] = (106 * I[i-1] + 1283) % 6075

plt.title("Plot of I_j vs j for N = 1000")
plt.plot(range(1000), I)
plt.xlabel('Value of j')
plt.ylabel('Value of I_j')
plt.show()
