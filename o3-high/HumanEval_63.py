def fibfib(n: int):
    """Compute the n-th term of the FibFib sequence.
    The sequence is defined by:
        fibfib(0) = 0
        fibfib(1) = 0
        fibfib(2) = 1
        fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)  (for n >= 3)
    The implementation uses fast exponentiation of the companion
    matrix, achieving O(log n) time.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Companion matrix for the recurrence:
    # [s(n)  ]   [1 1 1] [s(n-1)]
    # [s(n-1)] = [1 0 0] [s(n-2)]
    # [s(n-2)]   [0 1 0] [s(n-3)]
    M = [[1, 1, 1],
         [1, 0, 0],
         [0, 1, 0]]

    def mat_mult(a, b):
        """Multiply two 3x3 matrices."""
        return [[a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]
                 for j in range(3)] for i in range(3)]

    def mat_pow(mat, power):
        """Raise matrix to the given power using binary exponentiation."""
        result = [[1 if i == j else 0 for j in range(3)] for i in range(3)]  # Identity
        while power:
            if power & 1:
                result = mat_mult(result, mat)
            mat = mat_mult(mat, mat)
            power >>= 1
        return result

    # fibfib(n) is the first element of M^(n-2) * [1,0,0]^T,
    # which equals the (0,0) element of M^(n-2).
    power_matrix = mat_pow(M, n - 2)
    return power_matrix[0][0]