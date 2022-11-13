from typing import List
def letter_combinations_of_phone_number(digits:str) -> List[str]:
		def dfs(path, res):
			# exit
			if len(path) == len(digits):
				res.append(''.join(path))
				return
			# recursion
			next_number = digits[len(path)]
			for letter in KEYBOARD[next_number]:
				path.append(letter)
				dfs(path, res)
				path.pop()

		results = []
		dfs([], results)
		return results


letter_combinations_of_phone_number("56")
# ["jm","jn","jo","km","kn","ko","lm","ln","lo"]
