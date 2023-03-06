import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = np.array([1, 0.5, 0, 0.5, 2])
t = np.array([-1, -0.5, 0, 0.5, 1])

def polynomial(t, a1, a2, a3):
    return ((a1 * (t*t)) + (a2 * t) + a3)

coefficients, covariance = curve_fit(polynomial, t, y)
a1, a2, a3 = coefficients

plt.scatter(t, y, label='Observed Points')
plt.title('Question 1')
x = np.linspace(-1, 1, num=100)
plt.plot(x, polynomial(x, a1, a2, a3), label='Least Square')
plt.ylabel('y')
plt.xlabel('t')
plt.legend()
plt.show()
