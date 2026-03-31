def compare(game, guess):
    return [abs(g - h) for g, h in zip(game, guess)]