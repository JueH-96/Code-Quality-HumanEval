def is_bored(S):
    boredom = 0
    for sentence in S.replace('?','.').replace('!',".").split("."):
        if sentence.strip().startswith("I"):
            boredom += 1
    return boredom