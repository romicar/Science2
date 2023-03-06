import matplotlib.pyplot as plt
import numpy as np


def expectation_value(I):
    return np.sum(I) / len(I)


expectation_values = []

for N in list(range(1, 2001, 10)):
    I = np.zeros(N)
    I[0] = 1
    for i in range(1, N):
        I[i] = (106 * I[i-1] + 1283) % 6075
    expectation_values.append(expectation_value(I))

plt.title("Plot of E(I_j) vs N")
plt.plot(list(range(1, 2001, 10)), expectation_values)
plt.xlabel('N')
plt.ylabel('Expectation value of I_j')
plt.show()

