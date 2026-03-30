def decimal_to_binary(decimal):
    binary_representation = bin(decimal)[2:]  # Convert to binary and remove '0b' prefix
    return f"db{binary_representation}db"