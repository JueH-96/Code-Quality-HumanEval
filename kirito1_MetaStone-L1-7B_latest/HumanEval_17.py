from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Parse the input string representing musical notes and return a list of integers indicating the beats each note lasts."""
    tokens = music_string.split()
    result = []
    for token in tokens:
        if len(token) == 1:
            result.append(4)
        elif len(token) == 2 and token[0] == 'o':
            result.append(2)
        else:
            result.append(1)
    return result