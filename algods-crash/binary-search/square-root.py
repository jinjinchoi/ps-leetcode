def square_root(n):
	left, right = 1, n
	root = -1
	while left <= right:
		mid = (left+right)//2
		if mid*mid <= n:
			root = mid
			left = mid+1
		else:
			right = mid-1
	return res
