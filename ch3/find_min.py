from random import randrange
import time


def find_min_quadratic(a_list):
    smallest = 0

    for i in a_list:
        is_smallest = True
        for j in a_list:
            if i > j:
                is_smallest = False
                break
        if is_smallest:
            smallest = i

    return smallest


def find_min_linear(a_list):
    smallest = a_list[0]
    for num in a_list:
        if num < smallest:
            smallest = num
    return smallest


for list_size in range(1000, 10001, 1000):
    a_list = [randrange(100000) for x in range(list_size)]
    print(list_size)
    start = time.time()
    print(find_min_linear(a_list), end=' ')
    end = time.time()
    print(end - start)
    start = time.time()
    print(find_min_quadratic(a_list), end=' ')
    end = time.time()
    print(end - start)
