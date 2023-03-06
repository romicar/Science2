import random
import numpy as np
import matplotlib.pyplot as plt


# a = - (Roll Number % 5 + 1)
# b = - (Roll Number % 5 + 1);
# my roll no: 2021101053 
# so a = -4, b= 4

a = -4
b = 4

trials = 10000
max_steps = 100

def random_walk(N):
    pos_a = a
    pos_b = b
    for _ in range(N):
        pos_a+= random.choice([-1, 1])
        pos_b += random.choice([-1, 1])
    return pos_a, pos_b

def probability_meeting(N):
    cnt = 0
    for _ in range(trials):
        pos_a = random_walk(N)
        pos_b = random_walk(N)
        if pos_a == pos_b:
            cnt = cnt + 1
    return cnt / trials

probability = [probability_meeting(i) for i in range(max_steps)]


plt.title('Probability of both people meeting vs Number of steps')
plt.plot(range(max_steps), probability)
plt.xlabel('Number of Steps - N')
plt.ylabel('Probability')
plt.show()
