def find_max_sum_sub_array(nums, n):
	curr_max = nums[0]
	global_max = nums[0]
	for i in range(1, len(nums)):
		if curr_max < 0:
			curr_max = nums[i] # nums[i]가 음수여도 음수 + 음수 보단 음수 가 낫고. 양수면 더더욱.
		else:
			curr_max = curr_max + nums[i] # curr_max가 양수일 경우. nums[i]가 음수면 그래도 이전꺼까지 더하는 게 낫고. 양수면 더더욱 더하는 게 나음
		if global_max < curr_max:
			global_max = curr_max
	return global_max

def main():
    nums_list = [[-4, 2, -5, 1, 2, 3, 6, -5, 1],
                 [5, -2, 1, -3, 4, -2, 1, -3, 7]]
    for i in range(len(nums_list)):
        nums_size = len(nums_list[i])
        print(str(i+1) + ". Input array: " + str(nums_list[i]))
        print("   Sum of largest subarray: ",
              find_max_sum_sub_array(nums_list[i], nums_size))
        print("------------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()
