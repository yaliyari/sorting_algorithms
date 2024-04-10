import pandas as pd
import numpy as np
import os
""" A simple implementation of the Insertion sort"""


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
    return array


def merge_sort(array):
    return array