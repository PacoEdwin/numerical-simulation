import math
import numpy as np
import matplotlib.pyplot as plt

eps = np.finfo(np.double).eps


def LSE(x):
    return np.log(1+np.exp(x))


def max0(x):
    return np.maximum(x, 0)


def improvedLSE(values):
    boundary = np.log(1/(np.exp(eps) - 1))
    arr = np.copy(values)
    for i in range(len(arr)):
        if abs(arr[i]) < math.ceil(boundary):
            arr[i] = LSE(arr[i])
        else:
            arr[i] = arr[i] if arr[i] > 0 else 0

    return arr


def ex1():
    xs = np.linspace(-40, 40, 1000)
    plt.plot(xs, max0(xs))
    plt.plot(xs, LSE(xs))
    plt.plot(xs, improvedLSE(xs))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend(["$\max(0,x)$", "$LSE(x)$"])
    plt.show()


def ex2():
    xs = np.linspace(-1000, 1000, 1000)
    plt.plot(xs, max0(xs))
    plt.plot(xs, LSE(xs))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend(["$\max(0,x)$", "$LSE(x)$"])
    plt.show()


def solution():
    xs = np.linspace(-1000, 1000, 1000)
    plt.plot(xs, max0(xs))
    plt.plot(xs, improvedLSE(xs))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend(["$\max(0,x)$", "$LSE(x)$"])
    plt.show()


ex1()
