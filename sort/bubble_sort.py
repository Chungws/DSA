def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            temp = 0;
            if arr[j] < arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            else:
                continue
    return arr

print(bubble_sort([1,5,1,8,4,5,6,12]))