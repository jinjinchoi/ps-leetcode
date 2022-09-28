# arr[index] > arr[index+1]
# F F F T T T T
def peak_of_mountain_array(arr):
  left, right = 0, len(arr)-1
  largest_index = -1

  while left <= right:
    mid = (left+right)//2
    if arr[mid]>=arr[mid+1]:
      largest_index = mid
      right = mid - 1
    else:
      left = mid + 1

  return largest_index
