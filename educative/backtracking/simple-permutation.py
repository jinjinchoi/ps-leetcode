def permutation(l):
	def dfs(path, used, res):
		# exit condition
		if len(path)==len(l):
			res.append(path[:]) # DEEP COPY
			# append(list)를 그냥 하게 되면, shallow copy
			# 이는 list의 reference를 붙여주는 셈이다!!
			# value를 copy해주는 deep copy를 해주고 싶다면? 
			# append(list[:])를 해줘야 한다!!! 이렇게 하면
			# list[:]는 새로운 리스트를 생성해주는 셈이고
			# 생성된 리스트를 append해주게 됨
			return
		# non-exit conditon
		for i, letter in enumerate(l):
			if used[i]:
				continue
			path.append(letter)
			used[i] = True
			dfs(path, used, res) # --> recursive call
			path.pop() # --> back tracking
			used[i] = False # --> back tracking

	result = []
	dfs([], [False]*len(l), result)
	return result

inputs = "abc"

permutation(inputs.split())
