def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", data)
    bubble_sort(data)
    print("Sorted array:", data)

# Code by Harshit