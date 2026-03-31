import re
from typing import List


def parse_music(music_string: str) -> List[int]:
    """Parse a string of ASCII music notation into a list of beat lengths."""
    # Mapping of note representations to their beat lengths
    beats = {'o': 4, 'o|': 2, '.|': 1}

    # Regex to capture valid notes in order of decreasing length to ensure proper matching
    tokens = re.findall(r'o\||\.\||o', music_string)

    # Verify that the entire non-whitespace part of the input was parsed into valid tokens
    stripped_input = re.sub(r'\s+', '', music_string)
    if ''.join(tokens) != stripped_input:
        raise ValueError("Invalid musical notation found.")

    # Convert tokens to their corresponding beat lengths
    return [beats[token] for token in tokens]