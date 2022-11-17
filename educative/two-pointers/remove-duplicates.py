def remove_duplicates(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


# Driver code

inputs = ["0 0 1 1 1 2 2","1 2 3","1 1 1 1 1 1 1 1 1 1 1 1"]

for i in range(len(inputs)):
    arr = list(map(int, (inputs[i].split())))
    print("Remove duplicates : ",str(arr[: remove_duplicates(arr)]))

