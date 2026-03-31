def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]  # Remove the '0b' prefix
    return "db" + binary_str + "db"