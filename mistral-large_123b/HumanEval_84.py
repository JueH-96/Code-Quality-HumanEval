def solve(N):
    sum_of_digits = sum(int(d) for d in str(N))
    return bin(sum_of_digits)[2:]