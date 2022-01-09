def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i;
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j;
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr

print(selection_sort([1,5,1,8,4,5,6,12]))
                