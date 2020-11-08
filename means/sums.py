import numpy as np
import matplotlib.pyplot as plt

# параметр, может принимать любые целые значения > 1
base = 10


def exact_sum(K):
    """Точное значение суммы всех элементов."""
    return 1.


def samples(K):
    """"Элементы выборки"."""
    # создаем K частей из base^k одинаковых значений
    parts = [np.full((base**k,), float(base)**(-k)/K) for k in range(0, K)]
    # создаем выборку объединяя части
    samples = np.concatenate(parts)
    # перемешиваем элементы выборки и возвращаем
    return np.random.permutation(samples)


def direct_sum(x):
    """Последовательная сумма всех элементов вектора x"""
    s = 0.
    for e in x:
        s += e
    return s


def number_of_samples(K):
    return np.sum([base**k for k in range(0, K)])


def exact_mean(K):
    """Значение среднего арифметического по выборке с близкой к машинной точностью."""
    return 1./number_of_samples(K)


def exact_variance(K):
    """Значение оценки дисперсии с близкой к машинной точностью."""
    # разные значения элементов выборки
    values = np.asarray(
        [float(base)**(-k)/K for k in range(0, K)], dtype=np.double)
    # сколько раз значение встречается в выборке
    count = np.asarray([base**k for k in range(0, K)])
    return np.sum(count*(values-exact_mean(K))**2)/number_of_samples(K)


def relative_error(x0, x):
    """Погрешность x при точном значении x0"""
    return np.abs(x0-x)/np.abs(x)


def Kahan_sum(x):
    # частичная сумма
    s = 0.0
    # сумма погрешностей
    c = 0.0
    for i in x:
        # первоначально y равно следующему элементу последовательности
        y = i-c
        # сумма s может быть велика, поэтому младшие биты y будут потеряны
        t = s+y
        # (t-s) отбрасывает старшие биты, вычитание y восстанавливает младшие биты
        c = (t-s)-y
        # новое значение старших битов суммы
        s = t
    return s


def sum_sin(n):
    return (1 / 2) * (np.sin(n) - np.cos(n) / np.tan(1 / 2) + 1 / np.tan(1 / 2))


def create_sin_seq(n):
    return np.sin(np.arange(N + 1))


# Number of elements
N = 6
#N = 1000

# Create sequence
x = create_sin_seq(N)

# Sorted arrays
sorted_x = sorted(x)
sorted_x_abs = sorted(x, key=abs)

# Get sums
sum_sin = sum_sin(N)
d_sum = direct_sum(x)
direct_sorted_sum = direct_sum(sorted_x)
direct_sorted_abs_sum = direct_sum(sorted_x_abs)

# Kahan sums
kahan_sum = Kahan_sum(x)
kahan_sorted_sum = Kahan_sum(sorted_x)
kahan_sorted_abs_sum = Kahan_sum(sorted_x_abs)

print("Direct sum error: {}".format(
    relative_error(sum_sin, d_sum)))
print("Kahan sum error: {}".format(
    relative_error(sum_sin, kahan_sum)))
print()

print("Error of sum of ascending values: {}".format(
    relative_error(sum_sin, direct_sorted_sum)))
print("Error of Kahan sum of ascending values: {}".format(
    relative_error(sum_sin, kahan_sorted_sum)))
print()

print("Error of sum of absolute ascending values: {}".format(
    relative_error(sum_sin, direct_sorted_abs_sum)))
print("Error of Kahan sum of absolute ascending values: {}".format(
    relative_error(sum_sin, kahan_sorted_abs_sum)))
print()
