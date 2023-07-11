class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = (left+right)//2
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        # target이 그럼 첫번째 애보다 작은지, 큰지를 보고.
        # 첫번째 애보다 크면 k 이전
        # 첫번째 애보다 작으면 k 이후 --> binary search!
        # O logN이어야 한대
        
        
        
        def binary_search(left, right, target):
            left, right = left, right
            while left <= right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right = mid - 1
                else:
                    left = mid+1
            return -1
        
        if (answer := binary_search(0, left, target)) != -1:
            return answer
    
        return binary_search(left, len(nums)-1, target)