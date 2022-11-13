def word_breaks(s, words):
	memo = {}
	def dfs(i):
		print("dfs called with {}".format(i))
		if i==len(s):
			print("exit!")
			return True
		if i in memo:
			print("{} in memo".format(i))
			return memo[i]

		ok = False
		for word in words:
			if s[i:].startswith(word):
				if dfs(i+len(word)):
					ok = True
					break
		memo[i] = ok
		print("{} added to memo".format(i))
		return ok
	return dfs(0)

inputs = "aaaaaaaaaaaaaab"
inputs2 = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa"
word_breaks(inputs, inputs2.split())


# naive solution
#def word_break(s, words):
#	def dfs(i):
#		# exit condition
#		if i == len(s):
#			return True
#		# else
#		for word in words:
#			if s[i:].startswith(word):
##				if dfs(i+len(word)):
#					return True
#		return False
#
#	return dfs(0)
