def print_upper_words(words, must_start_with):
    """Accepts a list of words and a list of of letters.
    If the word in the list of words starts with a letter in the list of letters,
    the word will be returned in uppercase"""
    for word in words:
        # if word.startswith('h'):
        #     print(word.upper())
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())