import matplotlib.pyplot as plt
import random
import math

# according to the ques, since my roll number is 2021101053
# I have to use 2021101053 % 5 + 1 function
# so my function  is e^x cosx


## part B: plotting graph
results = []
for i in range(1, 100001, 1000):
    sum = 0

    for j in range(1,100001):
        randomNumber = random.uniform(-math.pi/2, math.pi/2)
        sum+=(math.exp(randomNumber) * math.cos(randomNumber))
    
    average =sum/100000
    answer = average*(math.pi)
    results.append(answer)

plt.title("Graph for Q2")
plt.plot(range(1, 100001, 1000), results)
plt.xlabel('Number of Samples')
plt.ylabel('Integral Value')
plt.show()
