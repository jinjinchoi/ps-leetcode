def fib(n, memo):
	print("fib({}, {}) called".format(n, memo))
	if n in memo:
		print("{} is in memo".format(n))
		return memo[n]
	if n==0 or n==1:
		print("return! exit condition")
		return n
	res = fib(n-1, memo) + fib(n-2, memo)
	print("memo[{}] = {}".format(n, res))
	memo[n] = res
	return res

memo = {}
print(fib(10, memo))
