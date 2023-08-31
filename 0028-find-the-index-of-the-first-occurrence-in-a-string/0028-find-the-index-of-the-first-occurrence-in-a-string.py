class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        for i in range(len_haystack - len_needle+1):
            for j in range(len_needle):
                if needle[j] != haystack[i+j]:
                    break
                if j == len_needle - 1:
                    return i
        return -1