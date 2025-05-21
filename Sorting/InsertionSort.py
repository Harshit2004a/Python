# Insertion Sorting
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    insertion_sort(data)
    print("Sorted array:", data)
    
# Code by Harshit