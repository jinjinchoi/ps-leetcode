class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # data 에 있는 1의 총 갯수 N
        N = sum(data)
        # 사이즈 N 짜리 sliding window -> 이 안에 1이 최대로 있는 경우 = max_one_count
        left = 0
        right = 0
        max_one_count = 0
        current_one_count = 0
        while right < len(data):
            current_one_count += data[right]
            right += 1
            if right - left > N:
                current_one_count -= data[left]
                left += 1
            max_one_count = max(max_one_count, current_one_count)
            
        return N - max_one_count