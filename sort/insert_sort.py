def insert_sort(arr):
    for i in range(1, len(arr)):
        select = arr[i]
        count = i
        for j in reversed(range(i)):
            if arr[j] <= select:
                break
            count -= 1
            arr[j+1] = arr[j]
        arr[count] = select
        print(arr)
    return arr

print(insert_sort([2,0,2,1,1,0]))