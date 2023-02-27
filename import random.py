import random
import time
print("ширина марицы:")
user_m = int(input())
print("длина марицы:")
user_n = int(input())
print("минимальное число марицы:")
user_min_limit = int(input())
print("максимальное число марицы:")
user_max_limit = int(input())
matrix=[]
b=[]
n=0
m=user_m
start_time = time.time()
print("МАТРИЦА:")
for i in range(user_m):
    for j in range(user_n):
        b.append(random.randint(user_min_limit, user_max_limit)) # генирация матрицы
    matrix.append(b[n:m]) # составление матрицы
    n += user_m
    m += user_m
print(matrix)

def sort(matrix): #встроенная сортировка
    for i in range(user_m):
        matrix[i]=sorted(matrix[i])
    return matrix

def selection_sort(matrix):  #сортировка выбором
    start = time.time()
    for p in range(user_n):
        for i in range(0, user_m):
            min_index =0
            for j in range(0, user_n-1):
                if matrix[i][j+1] < matrix[i][j]:
                    min_index = matrix[i][j]
                    matrix[i][j] = matrix[i][j+1]
                    matrix[i][j + 1]=min_index
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

def insertion_sort(matrix): # вставка
    start = time.time()
    for p in range(user_m):
        for i in range(1, user_n):
            key = matrix[p][i]
            j = i - 1
            while j >= 0 and matrix[p][j] > key:
                matrix[p][j + 1] = matrix[p][j]
                j -= 1
            matrix[p][j + 1] = key
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

def bubble_sort(matrix): # пузырчатая сортировка
    start = time.time()
    for p in range(user_m):
        for i in range(user_m - 1):
            for j in range(user_n - 1 - i):
                if matrix[p][j] > matrix[p][j + 1]:
                    matrix[p][j], matrix[p][j + 1] = matrix[p][j + 1], matrix[p][j]
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

def shell_sort(matrix): # сортировка шелла
    start = time.time()
    gap = user_n // 2
    while gap > 0:
        for p in range(user_m):
            for i in range(gap, user_m):
                temp = matrix[p][i]
                j = i
                while j >= gap and matrix[p][j - gap] > temp:
                    matrix[p][j] = matrix[p][j - gap]
                    j -= gap
                matrix[p][j] = temp
        gap //= 2
    print("--- {0} ms ---".format(round((time.time() - start)*1000)))
    return matrix

print("встроенная сортировка")
print(sort(matrix)[:10])

print("Отсортированная матрица с использованием сортировки выбором:")
print(selection_sort(matrix)[:10])

print("сортировка вставкой")
print(insertion_sort(matrix)[:10])

print("пузырчатая сортировка")
print(bubble_sort(matrix)[:10])

print("сортировка шелла")
print(shell_sort(matrix)[:10])