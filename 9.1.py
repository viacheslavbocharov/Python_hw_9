import string


def popular_words(text, words):
    text_list = (''.join(char for char in text if char not in string.punctuation)).lower().split()

    words_dict = {}
    for word in words:

        occurrences = filter(lambda text_word: word == text_word, text_list)
        words_dict.update({word: len(list(occurrences))})

    print(words_dict)
    return words_dict


popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
