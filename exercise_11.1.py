n = open('words.txt')

def create_word_dict():
    word_dict = dict()
    for line in n:
        word = line.strip()
        word_dict[word] = word
    return word_dict
