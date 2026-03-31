def words_in_sentence(sentence):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    words = sentence.split()
    result = []
    for word in words:
        length = len(word)
        if is_prime(length):
            result.append(word)
    return ' '.join(result)