import numpy as np
import matplotlib.pyplot as plt

def relative_error(x0,x):
     return np.abs(x0-x)/np.abs(x0)

def plot_error(x0,err):
    epsilon=np.finfo(np.double).eps
    plt.loglog(x0,err, '.k')
    plt.loglog(x0,np.full(x0.shape, epsilon), '--r')
    plt.xlabel("$Аргумент$")
    plt.ylabel("$Относительная\,погрешность$")
    plt.legend(["$Минимальная\,погр.$","$Машинная\,погр.$"])
    plt.show()

# 1 solution with devision
def log_by_devide(x, eps=2.71e-3):
    u = np.log(x)
    i = 0
    while u >= eps:
        u = u / 2
        i += 1
    if eps >= u >= eps / 2:
        b = True
    return 1 + u, i

def value_by_devide(values):
    assert len(values) == 2
    u = values[0]
    i = values[1] 
    return (2 ** i) * (u - 1)

eps = 2.71e-2
x = np.logspace(-3,3,100)

numbers1 = [value_by_devide(log_by_devide(elem, eps)) for elem in x]
x = np.log(x)

errors = relative_error(x, numbers1)
plot_error(x, errors)



# 2 solution with suntraction
def log_by_subtr(x, eps=2.71e-3):
    u = np.log(x)
    i = 0
    j = 0
    while u >= np.log(2):
        u = u - np.log(2)
        i += 1
    while u < 1 + eps / 2:
        u = u + eps
        j += 1
    return u, i, j

def value_by_subtr(values, eps=2.71e-3):
    assert len(values) == 3
    x = values[0]
    i = values[1]
    j = values[2]
    return (x - (j * eps)) + i * np.log(2)  

x = np.logspace(-3,3,100)

numbers2 = [value_by_subtr(log_by_subtr(elem)) for elem in x]
x = np.log(x)

errors = relative_error(x, numbers2)
plot_error(x, errors)