def compare(game, guess):
    """Return a list containing the absolute difference between each pair of
    actual scores (`game`) and corresponding guesses (`guess`). A value of 0
    indicates a correct guess.
    """
    if len(game) != len(guess):
        raise ValueError("Both input lists must be of the same length.")
    return [0 if g == h else abs(g - h) for g, h in zip(game, guess)]