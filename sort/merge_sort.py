def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    leftpointer, rightpointer = 0, 0
    merged_array = []
    while leftpointer < len(left) or rightpointer < len(right):
        if rightpointer >= len(right) or leftpointer >= len(left):
            if rightpointer >= len(right):
                merged_array.append(left[leftpointer])
                leftpointer += 1
            else:
                merged_array.append(right[rightpointer])
                rightpointer += 1
        else:
            if left[leftpointer] < right[rightpointer]:
                merged_array.append(left[leftpointer])
                leftpointer += 1
            elif left[leftpointer] >= right[rightpointer]:
                merged_array.append(right[rightpointer])
                rightpointer += 1
    return merged_array
print(merge_sort([1,5,1,8,4,5,6,12,7]))