#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

# -----------------------------------------------------------------------------
# За основу взят код пузырьковой сортировки из примеров к уроку.
# Дубликат кода был изменен под сортировку чет-нечет.
# После многократных запусков было замечено ускорение сортировки в пределах пары процентов, что может быть погрешностью.
# Вынос из цикла и уменьшение всех возможных просчетов ускорило сортировку на 10-20%
# -----------------------------------------------------------------------------
#                                  Реализация
import random
import cProfile

ra_limin = -100
ra_limax = 100
ra_size = 5_000

# -----------------------------------------------------------------------------
#                                    Randomizer


def rnd(size, limit_1, limit_2):
    ra = []
    for i in range(size):
        ra.append(random.randint(limit_1, limit_2))
    return ra


# -----------------------------------------------------------------------------
#                                    Вариант 1
def bubble_sort_classique(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


# -----------------------------------------------------------------------------
#                                     Вариант 2
def bubble_sort_odd_even(array):
    done = False
    m = len(array) - 1
    n = m - 1
    while not done:
        done = True
        for i in range(0, m, 2):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                done = False
        for i in range(1, n, 2):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                done = False
    return array


# -----------------------------------------------------------------------------
#                                      main func
def main():
    ra_1 = rnd(ra_size, ra_limin, ra_limax)
    ra_2 = rnd(ra_size, ra_limin, ra_limax)
    print(bubble_sort_classique(ra_1))
    print(bubble_sort_odd_even(ra_2))


# -----------------------------------------------------------------------------
#


cProfile.run('main()')