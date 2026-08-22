def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):#used to control the range of the inner loop in the bubble sort algorithm
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [43, 54, 8, 90, 88, 44, 21, 11, 43, 76, 52, 188]
bubble_sort(arr)
print("Sorted array:", arr)





