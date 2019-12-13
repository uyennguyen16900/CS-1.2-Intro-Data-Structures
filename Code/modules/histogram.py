from . import dictionary_words

#
# class Histogram():
#     def __init__(self, source_text=None):
#         self.words = dictionary_words.open_file(source_text)
#
#     def get_pairs(self):
#         words = self.words.copy()
#         pairs = []
#         i = 0
#         while len(words) > 0 and i < len(words):
#             word = words[i]
#             count = 1
#             index = i + 1
#             while index < len(words):
#                 if words[index] == word:
#                     count += 1
#                     words.pop(index)
#                     index = index - 1
#                 index += 1
#
#             pairs.append(word.rstrip())
#             pairs.append(count)
#
#             i += 1
#         return pairs
#
#     def histogram_list(self):
#         """Using list of list"""
#         list_words = self.get_pairs()
#         list_histogram = []
#         i = 0
#         while i < len(list_words) - 1:
#             list = []
#             list.append(list_words[i])
#             list.append(list_words[i+1])
#             list_histogram.append(list)
#             i += 2
#
#         return list_histogram
#
#     def histogram_tuple(self):
#         """Using list of tuple"""
#         list_histogram = []
#         list_words = self.get_pairs()
#         i = 0
#         while i < len(list_words) - 1:
#             tuple = list_words[i], list_words[i+1]
#             list_histogram.append(tuple)
#             i += 2
#
#         return list_histogram
#
#     def histogram_dictionary(self):
#         """Using list of dictionary"""
#         dictionary_histogram = {}
#         list_words = self.get_pairs()
#         i = 0
#         while i < len(list_words) - 1:
#             dictionary_histogram[list_words[i]] = list_words[i+1]
#             i += 2
#
#         return dictionary_histogram
#
#
#     def histogram_list_count(self):
#         list = []
#         list_pairs = self.get_pairs()
#
#         while len(list_pairs) > 0:
#             i = 1
#             count = list_pairs[1]
#             list_words = []
#             while i < len(list_pairs):
#                 if list_pairs[i] == count:
#                     list_words.append(list_pairs[i-1])
#                     list_pairs.pop(i-1)
#                     list_pairs.pop(i-1)
#                     i -= 2
#                 i += 2
#             tuple = count, list_words
#             list.append(tuple)
#         return list
#
#
#     def unique_words(self, histogram):
#         """Return the total count of unique words"""
#         return len(histogram)
#
#
#     def frequency(self, word, histogram):
#         """Return the number of times word appears in a text."""
#         return histogram[word]
#



def get_pairs(words):
    pairs = []
    i = 0
    while len(words) > 0 and i < len(words):
        word = words[i]
        count = 1
        index = i + 1
        while index < len(words):
            if words[index] == word:
                count += 1
                words.pop(index)
                index = index - 1
            index += 1

        pairs.append(word.rstrip())
        pairs.append(count)

        i += 1
    return pairs

# Return a histogram data structure that stores each
# unique word along with the number of times the word appears.

def histogram_list(words):
    """Using list of list"""
    list_words = get_pairs(words)
    list_histogram = []
    i = 0
    while i < len(list_words) - 1:
        list = []
        list.append(list_words[i])
        list.append(list_words[i+1])
        list_histogram.append(list)
        i += 2

    return list_histogram

def histogram_tuple(words):
    """Using list of tuple"""
    list_histogram = []
    list_words = get_pairs(words)
    i = 0
    while i < len(list_words) - 1:
        tuple = list_words[i], list_words[i+1]
        list_histogram.append(tuple)
        i += 2

    return list_histogram

def histogram_dictionary(words):
    """Using list of dictionary"""
    dictionary_histogram = {}
    list_words = get_pairs(words)
    i = 0
    while i < len(list_words) - 1:
        dictionary_histogram[list_words[i]] = list_words[i+1]
        i += 2

    return dictionary_histogram


def histogram_list_count(words):
    list = []
    list_pairs = get_pairs(words)

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
    words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    print(histogram_list(words))
    # print(histogram_tuple("words.txt"))
    print(histogram_dictionary(words))
    # print(frequency('fish', 'one fish two fish red fish blue fish'))
    print(get_pairs(words))
    # print(get_pairs(words))
    # print(histogram_list_count('words.txt'))
