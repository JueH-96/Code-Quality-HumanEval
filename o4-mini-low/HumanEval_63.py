def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # 3x3 matrix multiplication
    def mat_mul(A, B):
        return [
            [
                A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0],
                A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1],
                A[0][0]*B[0][2] + A[0][1]*B[1][2] + A[0][2]*B[2][2],
            ],
            [
                A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0],
                A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1],
                A[1][0]*B[0][2] + A[1][1]*B[1][2] + A[1][2]*B[2][2],
            ],
            [
                A[2][0]*B[0][0] + A[2][1]*B[1][0] + A[2][2]*B[2][0],
                A[2][0]*B[0][1] + A[2][1]*B[1][1] + A[2][2]*B[2][1],
                A[2][0]*B[0][2] + A[2][1]*B[1][2] + A[2][2]*B[2][2],
            ],
        ]

    # fast exponentiation of matrix
    def mat_pow(M, power):
        # identity matrix
        result = [[1,0,0],[0,1,0],[0,0,1]]
        base = M
        while power > 0:
            if power & 1:
                result = mat_mul(result, base)
            base = mat_mul(base, base)
            power >>= 1
        return result

    # transformation matrix
    M = [
        [1,1,1],
        [1,0,0],
        [0,1,0],
    ]

    # we want M^(n-2) * [T2, T1, T0]^T = M^(n-2) * [1,0,0]^T
    M_n2 = mat_pow(M, n-2)
    # result is first row dot initial vector
    return M_n2[0][0]*1 + M_n2[0][1]*0 + M_n2[0][2]*0