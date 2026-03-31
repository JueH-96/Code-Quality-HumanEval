import re

def count_sentences_starting_with_i(text):
    # Split the text into parts based on sentence terminators
    parts = re.split(r'[.!?]+', text)
    count = 0
    for part in parts:
        stripped_part = part.strip()
        if not stripped_part:
            continue
        words = stripped_part.split()
        if not words:
            continue
        # Check if the first word is 'i' or 'I'
        if words[0].lower() == 'i':
            count += 1
    return count

# Example usage:
text = "I am happy. How are you? I think."
print(count_sentences_starting_with_i(text))  # Output: 2