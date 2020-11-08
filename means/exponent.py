import numpy as np
import matplotlib.pyplot as plt


def exp_taylor(x, N=None):
    """N-ая частичная сумма ряда Тейлора для экспоненты."""
    acc = 1  # k-ая частичная сумму. Начинаем с k=0.
    xk = 1  # Степени x^k.
    inv_fact = 1  # 1/k!.
    for k in range(1, N+1):
        xk = xk*x
        inv_fact /= k
        acc += xk*inv_fact
    return acc


def exp_horner(x, N=None):
    """N-ая частичная сумма ряда Тейлора для экспоненты методом Горнера."""
    if N <= 0:
        return 1  # Избегаем деления на ноль.
    acc = 1  # Выражение во вложенных скобках в схеме Горнера
    for k in range(N, 0, -1):
        acc = acc/k*x + 1
    return acc

# 9
# При использовании свойства a^-x= (a^x)^-1


def exp_taylor_imp(x, N=None):
    acc = 1  # k-ая частичная сумму. Начинаем с k=0.
    xk = 1  # Степени x^k.
    inv_fact = 1  # 1/k!.
    x_abs = np.abs(x)
    for k in range(1, N + 1):
        xk = xk * x_abs
        inv_fact /= k
        acc += xk * inv_fact

    if x < 0:
        acc = 1 / acc
    return acc

# При использовании свойства a^-x= (a^x)^-1


def exp_horner_imp(x, N=None):
    """N-ая частичная сумма ряда Тейлора для экспоненты методом Горнера."""
    # avoid 0 devision
    if N <= 0:
        return 1 
    acc = 1
    x_abs = np.abs(x)
    for k in range(N, 0, -1):
        acc = acc / k * x_abs + 1

    if x < 0:
        return 1 / acc
    return acc


def make_exp_test(fns, args={}, xmin=-1, xmax=1):
    """Проводит тест приближения fn показательной функции."""
    x = np.linspace(xmin, xmax, 10)
    standard = np.exp(x)
    N = 10
    theoretical_relative_error = (np.abs(x)/2+1)*np.finfo(float).eps
    theoretical_absolute_error = theoretical_relative_error * standard

    fig, ax1 = plt.subplots(1, 1, figsize=(10, 5))
    ax2 = plt.twinx(ax1)
    ax1.set_xlabel("Argument")
    ax1.set_ylabel("Absolute error")
    ax2.set_ylabel("Relative error")

    ax1.semilogy(x, theoretical_absolute_error, '-r')

    line, = ax2.semilogy(x, theoretical_relative_error, '--r')
    line.set_label("theory (relative)")

    for fn in fns:
        subject = [fn(elem, N) for elem in x]
        absolute_error = np.abs(standard-subject)
        relative_error = absolute_error/standard

        ax1.semilogy(x, absolute_error, '-')

        line,  = ax2.semilogy(x, relative_error, '--')
        line.set_label("{} (relative)".format(fn.__name__))

    plt.legend()
    plt.show()


make_exp_test([exp_taylor_imp, exp_taylor_imp], args={
              "N": 3}, xmin=-0.001, xmax=0.001)
make_exp_test([exp_taylor_imp, exp_taylor_imp], args={"N": 3}, xmin=-1, xmax=1)
make_exp_test([exp_taylor_imp, exp_taylor_imp], args={"N": 3}, xmin=-10, xmax=10)
