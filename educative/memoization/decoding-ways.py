def decode_ways(digits):
	prefixes = [str(i) for i in range(1, 27)]
	print(prefixes)
	memo = {}
	def dfs(i, memo):
		print("dfs called with i:{}, memo:{}".format(i, memo))
		# exit condition
		if i == len(digits):
			print("exit!")
			return 1
		if i in memo:
			print("i{} found in memo".format(i))
			return memo[i]
		# recursion
		ways = 0
		remaining = digits[i:]
		for prefix in prefixes:
			if remaining.startswith(prefix):
				ways += dfs(i+len(prefix), memo)
		memo[i] = ways
		print("ways updated with memo[{}]: {}".format(i, ways))
		return ways
	return dfs(0, memo)

print(decode_ways("123"))
