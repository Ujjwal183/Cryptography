def caeser(plaintext:str, key: int)->str:
    """
    Caesar cipher encryption function.

    This function takes a plaintext string and a key (integer) as inputs,
    and returns the ciphertext by shifting each letter in the plaintext by
    the key value, according to the Caesar cipher algorithm.

    Parameters:
    ----------
    plaintext : str
        The input string to be encrypted.
    key : int
        The number of positions to shift each letter in the plaintext.

    Returns:
    -------
    ciphertext : str
        The encrypted string where each letter is shifted by the key value.

    Notes:
    ------
    - The function works only for alphabetic characters (A-Z).
    - The input plaintext is automatically converted to uppercase.
    - Non-alphabetic characters are ignored (this could be extended if needed).
    - The alphabet is treated in a circular manner, so shifting past 'Z' wraps back to 'A'.
    - Example: caeser("hello", 15) will return "WTAAD".
    """
    ciphertext = ""
    result = 0
    plaintext = plaintext.upper()
    for i in plaintext:
        result = (ord(i) - 65 + key) % 26
        ciphertext += chr(result + 65)
    return ciphertext


def main():
    print(caeser("hello", 15))


if __name__ == "__main__":
    main()
