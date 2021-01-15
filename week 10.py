def create_dictionary(file_name):
    """
    read the content of file_name
    and create & return a dictionary object
    with the first column as key, and remained columned as value
    """
    file = open(file_name, 'r')
    dict = {}
    for line in file:
        word = line.split()
        key = word[0]
        value = ' '.join(word[1:])
        dict[key] = value
    file.close()
    return dict

def translate(dict, word):
    """use the dictionary object to look up word and return the translated word"""
    return dict.get(word, word)

def translate_sentence(dict,sentence):
    """
    translate a whole sentence using the dictionary obj dict
    (call translate)
    """
    words = sentence.split()
    trans = []
    for word in words:
        trans.append(translate(dict, word))
    return ' '.join(trans)

# 4) MAIN PROGRAM:
dict = create_dictionary("C:\\Users\\s3877991\\PycharmProjects\\untitled\\eng2pirate.txt")
english_sentence = input('Enter a sentence: ')
new_sentence = translate_sentence(dict, english_sentence)
print('The new sentence is: ', new_sentence)