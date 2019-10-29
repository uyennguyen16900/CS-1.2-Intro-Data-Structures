import dictionary_words, string
from utils import time_it

def get_pair(words):
    pairs = []
    i = 0
    while len(words) > 0 and i < len(words) - 1:
        word = words[i]
        count = 1
        index = i + 1
        while index < len(words):
            if words[index] == word:
                count += 1
                words.remove(word)
                index = index - 1
            index += 1
        i += 1

        pairs.append(word.rstrip())
        pairs.append(count)

    return pairs

# Return a histogram data structure that stores each
# unique word along with the number of times the word appears.
def histogram_list(source_text):
    """Using list of list"""
    words = dictionary_words.open_file(source_text)
    list_words = get_pair(words)
    list_histogram = []
    i = 0
    while i < len(list_words) - 1:
        list = []
        list.append(list_words[i])
        list.append(list_words[i+1])
        list_histogram.append(list)
        i += 2

    return list_histogram

def histogram_tuple(source_text):
    """Using list of tuple"""
    words = dictionary_words.open_file(source_text)
    list_histogram = []
    list_words = get_pair(words)
    i = 0
    while i < len(list_words) - 1:
        tuple = list_words[i], list_words[i+1]
        list_histogram.append(tuple)
        i += 2

    return list_histogram

def histogram_dictionary(source_text):
    """Using list of dictionary"""
    words = dictionary_words.open_file(source_text)
    dictionary_histogram = {}
    list_words = get_pair(words)
    i = 0
    while i < len(list_words) - 1:
        dictionary_histogram[list_words[i]] = list_words[i+1]
        i += 2

    return dictionary_histogram


def histogram_list_count(source_text):
    words = dictionary_words.open_file(source_text)
    list = []
    list_pairs = get_pair(words)

    while len(list_pairs) > 0:
        i = 1
        count = list_pairs[1]
        list_words = []
        while i < len(list_pairs):
            if list_pairs[i] == count:
                list_words.append(list_pairs[i-1])
                list_pairs.pop(i-1)
                list_pairs.pop(i-1)
                i -= 2
            i += 2
        tuple = count, list_words
        list.append(tuple)
    return list


def unique_words(histogram):
    """Return the total count of unique words"""
    return len(histogram)


def frequency(word, histogram):
    """Return the number of times word appears in a text."""
    return histogram[word]


if __name__ =="__main__":
    print(histogram_list('words.txt'))
    print(histogram_tuple("words.txt"))
    print(histogram_dictionary("words.txt"))
    # print(frequency('fish', 'one fish two fish red fish blue fish'))
    words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    print(get_pair(words))
    print(histogram_list_count('words.txt'))
