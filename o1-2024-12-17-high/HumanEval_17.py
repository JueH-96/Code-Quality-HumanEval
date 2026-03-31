def parse_music(music_string: str) -> List[int]:
    beats_map = {
        "o": 4,
        "o|": 2,
        ".|": 1
    }
    tokens = music_string.strip().split()
    return [beats_map[token] for token in tokens]