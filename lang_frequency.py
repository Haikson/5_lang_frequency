import sys
import re
import codecs
import operator

def remove_punctuation(text):
    return re.sub(r"\W+", " ", text).lower()

def load_data(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as fd:
        text = fd.read()
    return text


def get_most_frequent_words(text):
    words_dict = {}
    for word in text.split():
        if word == '':
            pass
        words_count = 1 + words_dict.get(word, 0)
        words_dict[word] = words_count
    sorted_words = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    
    for dict_item in sorted_words[:10]:
        print(u"{}".format(dict_item[0]))
        


if __name__ == '__main__':
    text = load_data(sys.argv[1])
    text = remove_punctuation(text)
    get_most_frequent_words(text)