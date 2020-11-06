import numpy as np
import matplotlib.pyplot as plt


def relative_error(x0, x):
    return np.abs(x0-x)/np.abs(x0)


eps = np.finfo(np.double).eps
print("Машинная точность:", eps)


def plot_error(x0, err):
    mask = np.logical_and(err > 0, err < np.inf)
    plt.loglog(x0[mask], err[mask], ".k")
    plt.loglog(x0, [eps]*len(err), "--rs")  # машинная точность для сравнения
    plt.xlabel("$Значение\;аргумента$")
    plt.ylabel("$Относительная\;погрешность$")
    plt.show()


#############################################################
def f_div_mult(x, d=np.pi, n=52):
    for k in range(n):
        x = x/d
    for k in range(n):
        x = x*d
    return x


x0 = np.logspace(-4, 4, 1000, dtype=np.double)
x = f_div_mult(x0)
err = relative_error(x0, x)
print("Ошибки", err[:4], "...")
plot_error(x0, err)
#############################################################


#############################################################
class LogNumber(object):
    def __init__(self, value):
        self.res = np.log(value)

    def __float__(self):
        return np.exp(self.res)

    def __pow__(self, other):
        self.res = self.res * other
        return self

    def from_float(value):
        return LogNumber(value)


def f_sqrt_sqr(x, n=52):
    numbers = [LogNumber.from_float(el) for el in x0]
    for el in numbers:
        for _ in range(n):
            el = el ** (1 / 2)

    for el in numbers:
        for _ in range(n):
            el = el ** (2)

    return [el.__float__() for el in numbers]


x = f_sqrt_sqr(x)
err = relative_error(x0, x)
plot_error(x0, err)
#############################################################


#############################################################
class PowNumber(object):
    def __init__(self, num):
        self.num = num
        # power of a 2 (x^(2^power))
        self.power = 0

    def __str__(self):
        return "{}".format(self.to_float())

    def to_float(self):
        return pow(self.num, 2**self.power)

    def from_float(x):
        return PowNumber(x)

    def square(self):
        self.power += 1

    def root(self):
        self.power -= 1


def f_sqrt_sqr_my(x0, n=52):
    arr = np.array([PowNumber(el) for el in x0])

    for _ in range(n):
        for el in arr:
            el.root()
    for _ in range(n):
        for el in arr:
            el.square()

    arr = np.array([el.to_float() for el in arr])
    return arr


x = f_sqrt_sqr_my(x0)
err = relative_error(x0, x)
plot_error(x0, err)
#############################################################


#############################################################
def f_sqrt_sqr(x, n=52):
    for k in range(n):
        x = np.sqrt(x)
    for k in range(n):
        x = x*x
    return x


x = f_sqrt_sqr(x0)
err = relative_error(x0, x)
plot_error(x0, err)
#############################################################


#############################################################
def f_sqrt_sqr_interleave(x, n=52):
    for k in range(n):
        x = np.sqrt(x)
        x = x*x
    return x


x = f_sqrt_sqr_interleave(x0)
err = relative_error(x0, x)
plot_error(x0, err)
#############################################################
