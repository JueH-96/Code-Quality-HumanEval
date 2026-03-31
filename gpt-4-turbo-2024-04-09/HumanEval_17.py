from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beats = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            if i + 1 < len(music_string) and music_string[i + 1] == '|':
                beats.append(2)
                i += 2  # Skip the next character as it's part of the current note
            else:
                beats.append(4)
        elif music_string[i] == '.':
            if i + 1 < len(music_string) and music_string[i + 1] == '|':
                beats.append(1)
                i += 2  # Skip the next character as it's part of the current note
        i += 1  # Move to the next character
    return beats