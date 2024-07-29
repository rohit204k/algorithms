# Python program for implementation of Selection Sort
import random


# Function for Selection sort
def selection_sort(arr: list[int]):
    n = len(arr)

    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():

    n = 10
    A = random.choices(list(range(1, 100)), k=n)
    print("Input Array, A = ")
    print(A)
    print()

    B = selection_sort(A)
    print("Selection Sort - Sorted array")
    print(B)


if __name__ == "__main__":
    main()
