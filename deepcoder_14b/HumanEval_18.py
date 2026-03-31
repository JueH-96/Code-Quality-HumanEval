def count_substring_occurrences(string, substring):
    if not substring:
        return 0
    len_sub = len(substring)
    count = 0
    for i in range(len(string) - len_sub + 1):
        if string[i:i+len_sub] == substring:
            count += 1
    return count

# Example usage:
print(count_substring_occurrences('aaaa', 'aa'))  # Output: 3