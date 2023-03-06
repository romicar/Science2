import numpy as np
import matplotlib.pyplot as plt


# a = - (Roll Number % 5 + 1);
# my roll no: 2021101053 
# so a = -4

trials = 10000
max_steps = 100


def prob_return_origin(N):
    all_walks = np.cumsum((2*(np.random.randint(0,2, size=(trials, N)))-1),axis=1)
    # print(all_walks)
    returnedtoorigin=0
    for i in range(trials):
        if all_walks[i][N-1]==4:
            returnedtoorigin = returnedtoorigin + 1
    return returnedtoorigin/trials
        

probs = [prob_return_origin(i) for i in range(1, max_steps)]
plt.plot( range(1, max_steps), probs)
plt.xlabel('Number of Steps (N)')
plt.ylabel('Probability of returning to origin')
plt.title('Probability of returning to origin vs Number of Steps')
plt.show()
