from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split()
    beat_lengths = []

    for note in notes:
        if note == 'o':
            beat_lengths.append(4)
        elif note == 'o|':
            beat_lengths.append(2)
        elif note == '.|':
            beat_lengths.append(1)
            
    return beat_lengths