import random
import timeit

from matplotlib import pyplot as plt


def randomized_quick_sort(array):
    if len(array) < 2:
        return array

    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(array):
    if len(array) < 2:
        return array

    pivot_index = random.choice([0, len(array) // 2, -1])
    pivot = array[pivot_index]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


lns = (10_000, 50_000, 100_000, 500_000)
arrays = {
    ln: [random.randint(0, ln) for _ in range(ln)]
    for ln in lns
}

rand_results = []
det_results = []

for ln, array in arrays.items():
    rand_time = timeit.timeit(lambda: randomized_quick_sort(array), number=5)
    det_time = timeit.timeit(lambda: deterministic_quick_sort(array), number=5)

    rand_results.append(rand_time)
    det_results.append(det_time)

for i in range(len(lns)):
    print('\nРозмір масиву:', lns[i])
    print(f'Рандомізований QuickSort: {rand_results[i]:.4f} секунд')
    print(f'Детермінований QuickSort: {det_results[i]:.4f} секунд')

plt.plot(lns, rand_results, '-o', label='Рандомізований QuickSort')
plt.plot(lns, det_results, '-s', label='Детермінований QuickSort')

plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.legend()
plt.grid()
plt.show()
