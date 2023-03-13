
def letter_to_index(letter):
    letter = letter.lower()
    return ord(letter) - ord('a')

def index_to_letter(index):
    return chr(index + ord('a'))

