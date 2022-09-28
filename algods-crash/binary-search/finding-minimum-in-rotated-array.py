def find_min_rotated(arr):
  left, right = 0, len(arr)-1
  n = len(arr)
  min_index = -1

  while left <= right:
    mid = (left+right)//2
    if arr[mid] <= arr[-1]:
      right = mid-1
      min_index = mid
    else:
      left = mid + 1
    
  return min_index
