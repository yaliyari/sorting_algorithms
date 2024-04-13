import pandas as pd
import numpy as np
import os
import random
""" A simple implementation of the Insertion sort"""

def gen_list():
    # n is length of list
    n = 10
    rand_list = [random.randint(0,100) for _ in range(n)]
    return rand_list


def insertion_sort(array):
    n = len(array)
    if n <= 1:
        return array  # array of length 0 or 1 is already sorted

    for i in range(0, n):
        key = array[i]
        j = i-1
        while j > -1 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def bubble_sort(array):
    n = len(array)
    if n <= 1:
        return array  # array of length 0 or 1 is already sorted
    for i in range(0, n):
        swap_flag = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap_flag = True
        if not swap_flag:
            break
    return array


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged
