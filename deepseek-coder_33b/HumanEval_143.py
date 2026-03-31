def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
def words_in_sentence(sentence):
    """You are given a string representing a sentence, the sentence contains some words separated by a space, and you have to return a string that contains the words from the original sentence, whose lengths are prime numbers, the order of the words in the new string should be the same as the original one."""
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)