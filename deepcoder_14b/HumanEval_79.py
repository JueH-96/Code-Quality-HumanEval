def decimal_to_binary(decimal):
    """Converts a decimal number to binary string with 'db' at both ends."""
    binary = bin(decimal)[2:]
    return f"db{binary}db"