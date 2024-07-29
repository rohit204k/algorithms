# Optimized Python program for implementation of Bubble Sort
import random


# Function for Bubble sort
def bubbleSort(arr: list[int]):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

    return arr


def main():

    n = 10
    A = random.choices(list(range(1, 100)), k=n)
    print("Input Array, A = ")
    print(A)
    print()

    B = bubbleSort(A)
    print("Bubble Sort - Sorted array")
    print(B)


if __name__ == "__main__":
    main()
