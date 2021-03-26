import numpy as np
import matplotlib.pyplot as plt
from scipy import constants


def prob(ket, pos):
    norm = np.linalg.norm(ket) ** 2
    ket[pos][0] = np.linalg.norm(ket[pos][0]) ** 2 / norm
    return round(ket[pos][0].real, 2)


def prob2(ket, eigv):
    mult = np.inner(ket, eigv)
    return np.linalg.norm(mult) ** 2


def bra(ket):
    return ket.transpose().conjugate()


def transitionProb(ket, ket2):
    ket2Dagger = bra(ket2)
    result = np.dot(ket2Dagger, ket)
    return round(np.linalg.norm(result) ** 2, 2)


def expected(obs, ket):
    mult = np.matmul(obs, ket)  # Multiplication between observable and ket
    expected = np.dot(mult.transpose().conjugate(), ket)[0][0]
    return expected


def deltaOp(obs, mat):
    return obs - mat


def variance(obs, ket):
    exp = expected(obs, ket)
    mult = exp * np.identity(len(obs))  # Multiplication between expected and indentity matrix
    delta = deltaOp(obs, mult)
    mult2 = np.matmul(delta, delta)  # Multiplication between delta and delta
    var = expected(mult2, ket).real
    return var


def measures(obs):
    return np.linalg.eig(obs)[0]


def finalStates(obs):
    return np.linalg.eig(obs)[1]


def finalStateDin(ket, transformations):
    finalState = ket
    for i in range(len(transformations)):
        finalState = np.matmul(transformations[i], finalState)
    return finalState


transformations = np.array([np.array([[(1 + 1j)/2, (1 - 1j)/2], [(1 - 1j)/2, (1 + 1j)/2]]),
                            np.array([[1, 0], [0, 1j]])])
ket = np.array([1j, 2j])

print(finalStateDin(ket,transformations))

def ex1():
    spin_up = np.array([[1], [0]])
    spin_operators = constants.hbar / 2 * np.array([[0, 1], [1, 0]])
    states = finalStates(spin_operators)
    return states


def ex2():
    plot()


def plot():
    ket = np.array([[1], [0]])
    spin_operators = constants.hbar / 2 * np.array([[0, 1], [1, 0]])
    states = finalStates(spin_operators)
    p1 = np.linalg.norm(np.inner(ket, states[0])) ** 2
    p2 = np.linalg.norm(np.inner(ket, states[1])) ** 2
    l1 = measures(spin_operators)[0]
    l2 = measures(spin_operators)[1]
    x = [l1, l2]
    y = [p1, p2]
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.scatter(x, y, color='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plot')
    plt.grid()
    plt.show()


def isUnitary(mat):
    mult = np.matrix.round(np.matmul(mat, mat.transpose().conjugate()))
    iden = np.identity(len(mat))
    if mult.all() == iden.all():
        return True
    else:
        return False


def ex3():
    u1 = np.array([[0, 1], [1, 0]])
    u2 = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
    u12 = np.matmul(u1, u2)
    matrices = [u1, u2, u12]
    for matrix in matrices:
        print(isUnitary(matrix))


def ex4():
    mat = np.array([[0, 1 / np.sqrt(2), 1 / np.sqrt(2), 0],
                    [1j / np.sqrt(2), 0, 0, 1 / np.sqrt(2)],
                    [1 / np.sqrt(2), 0, 0, 1j / np.sqrt(2)],
                    [0, 1 / np.sqrt(2), -1 / np.sqrt(2), 0]])
    st1 = np.array([[1], [0], [0], [0]])
    res = st1
    for i in range(3):
        res = np.matmul(mat, res)
    return prob(res, 3)
