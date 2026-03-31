s = input().strip()
stack = []
pairs = []

for i, c in enumerate(s):
    if c == '[':
        stack.append(i)
    elif c == ']':
        if not stack:
            pass  # Invalid string with unmatched ]
        else:
            j = stack.pop()
            pairs.append((j, i))

def is_valid(sub_str):
    stack_sub = []
    for char in sub_str:
        if char == '[':
            stack_sub.append(char)
        elif char == ']':
            if not stack_sub:
                return False
            stack_sub.pop()
    return len(stack_sub) == 0

found = False
for start, end in pairs:
    substr = s[start + 1:end]
    if is_valid(substr):
        found = True
        break

print("True" if found else "False")