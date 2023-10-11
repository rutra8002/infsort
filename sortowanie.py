import time
import random

numbers = [random.randint(1, 1000) for _ in range(10000)]
def swap(list, i, k):
    temp = list[i]
    list[i] = list[k]
    list[k] = temp

def bubble_sort(list):
    n = len(list)
    for r in range(1, n):
        for i in range(n - r):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
    return list

def bubble_sort_better(list):
    n = len(list)
    for r in range(1, n):
        is_sorted = True
        for i in range(n - r):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                is_sorted = False
        if is_sorted:
            break
    return list

def selection_sort(list):
    lenght = len(list)
    for first in range(lenght):
        min = first
        for i in range(first, lenght):
            if list[i] < list[min]:
                min = i
        swap(list, first, min)
    return list

start_time = time.time()
print(bubble_sort_better(numbers))
print("bubble_sort_better execution time: {:.6f} seconds".format(time.time() - start_time))

start_time = time.time()
print(bubble_sort(numbers))
print("bubble_sort execution time: {:.6f} seconds".format(time.time() - start_time))

start_time = time.time()
print(selection_sort(numbers))
print("selection_sort execution time: {:.6f} seconds".format(time.time() - start_time))

start_time = time.time()
print(sorted(numbers))
print("sort execution time: {:.6f} seconds".format(time.time() - start_time))
