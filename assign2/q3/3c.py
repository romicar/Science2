import matplotlib.pyplot as plt
import numpy as np
import random

trials = 10000
max_steps = 100

def avg_displacement(N):
    if N == 0:
        return 0
    steps = [(2*np.random.randint(0, 2, size=(N,))-1) for _ in range(trials)]
    positions = np.cumsum(steps, axis=1)
    return np.mean(np.abs(positions[:,-1]))

displacements = [avg_displacement(i) for i in range(max_steps)]
plt.plot(range(max_steps), displacements)
plt.title('Average Displacement vs Number of Steps')
plt.xlabel('Number of Steps - N')
plt.ylabel('Average Displacement')
plt.xticks(range(1, max_steps+1, 10))
plt.show()
