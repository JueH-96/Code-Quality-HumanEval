def xor_binary_strings(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)
    result = []
    for i in range(max_len):
        bit_a = int(a_padded[i])
        bit_b = int(b_padded[i])
        xor_bit = 1 if (bit_a != bit_b) else 0
        result.append(str(xor_bit))
    return ''.join(result)