import random
import time

print("ширина марицы:")
m = int(input())
print("длина марицы:")
n = int(input())
print("минимальное число марицы:")
min_limit = int(input())
print("максимальное число марицы:")
max_limit = int(input())
a=[]
def generate_random_matrix(m, n, min_limit, max_limit):
    return [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]

matrix = generate_random_matrix(m, n, min_limit, max_limit)

def sorted_matrix(a):

    for p in range(0,m,1):
        s=sorted(matrix[m])
        a.append(s)
    return a

def selection_sort(matrix):
    start = time.time()
    for i in range(len(matrix)):
        min_index = i
        for j in range(i + 1, len(matrix)):
            if matrix[0][j] < matrix[0][min_index]:
                min_index = j
                matrix[i], matrix[min_index] = matrix[min_index], matrix[j]
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

def insertion_sort(matrix):
    start = time.time()
    for i in range(1, len(matrix)):
        key = matrix[i]
        j = i - 1
        while j >= 0 and matrix[j][0] > key[0]:
            matrix[j + 1] = matrix[j]
            j -= 1
        matrix[j + 1] = key
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

def bubble_sort(matrix):
    start = time.time()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 1 - i):
            if matrix[j][0] > matrix[j + 1][0]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

def shell_sort(matrix):
    start = time.time()
    gap = len(matrix) // 2
    while gap > 0:
        for i in range(gap, len(matrix)):
            temp = matrix[i]
            j = i
            while j >= gap and matrix[j - gap][0] > temp[0]:
                matrix[j] = matrix[j - gap]
                j -= gap
            matrix[j] = temp
        gap //= 2
    end = time.time()
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

print("МАТРИЦА:")
print(matrix)

print("Отсортированная матрица с помощью sorted():")
print(sorted_matrix)

print("Отсортированная матрица с использованием сортировки выбором:")
print(selection_sort(matrix)[:10])

print("Отсортированная матрица с использованием сортировки вставками:")
print(insertion_sort(matrix)[:10])

print("Отсортированная матрица с использованием пузырьковой сортировки:")
print(bubble_sort(matrix)[:10])

print("Отсортированная матрица с использованием сортировки оболочки:")
print(shell_sort(matrix)[:10])
