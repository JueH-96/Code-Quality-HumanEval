def parse_patterns(pattern_string):
    patterns = pattern_string.split()
    result = []
    for token in patterns:
        if token == 'o':
            result.append(4)
        elif token == 'o|':
            result.append(2)
        else:
            result.append(1)
    return result

# Example usage
music_string = "o o| .| o| o| .| .| .| .| o o"
print(parse_patterns(music_string))