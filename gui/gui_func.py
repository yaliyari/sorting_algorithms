import tkinter as tk
from tkinter import messagebox
from algorithms import sort_algorithms


def option_one():
    messagebox.showinfo("Insertion Sort", "Insertion sort is selected")
    array = sort_algorithms.gen_list()
    print("The unsorted array is: ", array)
    print(sort_algorithms.insertion_sort(array))


def option_two():
    messagebox.showinfo("Bubble Sort", "Bubble sort is selected")
    array = sort_algorithms.gen_list()
    print("The unsorted array is: ", array)
    print(sort_algorithms.bubble_sort(array))


def option_three():
    messagebox.showinfo("Merge Sort", "Merge sort is selected")
    array = sort_algorithms.gen_list()
    print("The unsorted array is: ", array)
    print(sort_algorithms.merge_sort(array))


def close_app():
    root.destroy()


root = tk.Tk()
root.title("Choose sorting algorithm")
root.geometry('500x800')
button_one = tk.Button(root, text="Insertion sort", command=option_one)
button_one.pack(pady=5)

button_two = tk.Button(root, text="Bubble sort", command=option_two)
button_two.pack(pady=5)

button_three = tk.Button(root, text="Merge sort", command=option_three)
button_three.pack(pady=5)

close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack(pady=80)

root.mainloop()