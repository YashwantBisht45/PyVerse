def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


print("Valid:", is_valid("({[]})"))
print("Invalid:", is_valid("({[})"))
