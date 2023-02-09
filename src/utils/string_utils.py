

def add_to_letter(letter, num):
    """Add a number to a letter to get the next letter in the alphabet.

    Args:
        letter (str): The letter to add to.
        num (int): The number to add to the letter.

    Returns:
        str: The next letter in the alphabet.
    """
    return chr(ord(letter) + num)