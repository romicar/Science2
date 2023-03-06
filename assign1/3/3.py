import numpy as np
import matplotlib.pyplot as plt

colors = ['red', 'blue', 'green', 'purple']

N = 500
D = [0, 1, 5, 10]

def create_matrix(N, d):
    M = np.random.normal(0, 1, (N, N))
    np.fill_diagonal(M, -d)
    return M

def get_eigenvalues(M):
    return np.linalg.eigvals(M)

def plot_eigenvalues(eigenvalues, color, label):
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues), c=color, label=label)

def main(N, D):
    for i, d in enumerate(D):
        M = create_matrix(N, d)
        eigenvalues = get_eigenvalues(M)
        plot_eigenvalues(eigenvalues, color=colors[i], label=f"D = {d}")
    plt.xlabel('Real(λ)')
    plt.ylabel('Imag(λ)')
    plt.title('Question 3')
    plt.legend()
    plt.show()


main(N, D)
