# @param {String} s
# @return {Integer}
def remove_palindrome_sub(s)
    if s.length == 0 
        return 0
    end
    for i in 0..s.length/2 do
        return 2 if s[i] != s[-i-1]
    end
    return 1
end