def find_first_occurrence(arr, target):
  left, right = 0, len(arr)
  occurence_index = -1
  while left <= right:
    mid = (left+right)//2
    if arr[mid] == target:
      occurence_index = mid
      right = mid - 1
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return occurence_index
