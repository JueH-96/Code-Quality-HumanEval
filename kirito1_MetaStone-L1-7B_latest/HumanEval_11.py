def my_xor(a, b):
    num_a = int(a, 2)
    num_b = int(b, 2)
    xor_num = num_a ^ num_b
    return bin(xor_num)[2:]