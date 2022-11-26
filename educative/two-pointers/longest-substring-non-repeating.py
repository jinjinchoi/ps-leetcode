def longest_substring_without_repeating_characters(s):
    n = len(s)
    longest = 0
    l = r = 0
    window = set()
    while r < n:
        if s[r] not in window:
            window.add(s[r])
            r += 1
        else:
            window.remove(s[l])
            l += 1
        longest = max(longest, r - l)
    return longest

#Driver code
inputs = ["abcdbea","aba","abccabcabcc","aaaabaaa"]
for i in range(len(inputs)):
    print("Longest substring without repeating characters :",longest_substring_without_repeating_characters(inputs[i]))
