def is_palindrome(s):
    slow, fast = 0, len(s)-1
    while slow<=fast:
        # print("slow{}/s[slow]{}, fast{}/s[fast]{}".format(slow, s[slow], fast, s[fast]))
        if not s[slow].isalnum():
            slow += 1
            continue
        if not s[fast].isalnum():
            fast -= 1
            continue
        if s[slow].lower()!=s[fast].lower():
            return False
        else:
            slow += 1
            fast -= 1
    return True

inputs = ["Do geese see God","Was it a car or a cat I saw?","A brown fox jumping over"]
for i in range(len(inputs)):
      print("Is palindrome : ",is_palindrome(inputs[i]))
