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

    # Define a dictionary to map note representations to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes (assuming they are space-separated)
    notes = music_string.split()

    # Initialize an empty list to store the beat durations of the parsed notes
    beat_durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Check if the note matches any of the defined note representations (with and without trailing space)
        if note in note_durations:
            beat_durations.append(note_durations[note])
        elif note.rstrip() in note_durations:  # Handle notes with trailing spaces
            beat_durations.append(note_durations[note.rstrip()])
        else:
            raise ValueError(f"Unknown note representation: '{note}'")

    return beat_durations