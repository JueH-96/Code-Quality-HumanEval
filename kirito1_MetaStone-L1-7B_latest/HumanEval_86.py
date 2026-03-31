import re

def process_string(s):
    # Split the input string into words and non-words parts
    tokens = list(re.split(r'(\W+)', s))
    
    result = []
    for token in tokens:
        if not token.strip():  # Skip empty strings from splitting
            continue
        if token.isalpha():
            processed_token = ''.join(sorted(token, key=lambda x: ord(x)))
            result.append(processed_token)
        else:
            result.append(token)
    return ''.join(result)

# Example usage
input_str = "Hello World!!!"
output_str = process_string(input_str)
print(f"Input: {input_str}")
print(f"Output: {output_str}")