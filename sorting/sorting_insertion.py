# Python program for implementation of Insertion Sort
import random


# Function for Insertion sort
def insertionSort(arr: list[int]):
    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def main():

    n = 10
    A = random.choices(list(range(1, 100)), k=n)
    print("Input Array, A = ")
    print(A)
    print()

    B = insertionSort(A)
    print("Insertion Sort - Sorted array")
    print(B)


if __name__ == "__main__":
    main()
