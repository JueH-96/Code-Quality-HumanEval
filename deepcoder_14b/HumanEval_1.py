s = input().strip()
# Remove all spaces from the string
s = s.replace(" ", "")

result = []
current_group = []
balance = 0

for char in s:
    current_group.append(char)
    if char == '(':
        balance += 1
    else:
        balance -= 1
    
    # If balance is zero, we've found a complete group
    if balance == 0:
        result.append(''.join(current_group))
        current_group = []

# Print each group on a new line
print('
'.join(result))