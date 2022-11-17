from typing import List
def move_zeros(nums: List[int]) -> None:
      slow = 0
      for fast in range(len(nums)):
          if nums[fast] != 0:
              nums[slow], nums[fast] = nums[fast], nums[slow]
              slow += 1
              
# Driver code
inputs = ["1 0 2 0 0 7", "3 1 0 1 3 8 9"]
for i in range(len(inputs)):
    arr = [int(x) for x in inputs[i].split()]
    move_zeros(arr)
    print("Move zeros : ",' '.join(str(x) for x in arr))
