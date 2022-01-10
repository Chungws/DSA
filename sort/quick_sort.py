def quick_sort(arr):
    if len(arr) < 2:
        return arr
    left, right = [], []
    pivot = arr[len(arr)//2]
    
    for i in range(len(arr)):
        if i == len(arr)//2:
            continue
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    arr = quick_sort(left) + [pivot] + quick_sort(right)
    return arr

print(quick_sort([1,5,1,8,4,5,6,12,7]))