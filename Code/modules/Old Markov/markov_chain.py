from random import randrange
from dictogram import Dictogram
from dictionary_words import open_file
import random
# import nltk
# nltk.download('punkt')

from nltk.tokenize import sent_tokenize
text = "God is Great! I won a lottery. Mr. Nguyen is awesome."
print(sent_tokenize(text))

def get_pairs(words):
    """Make a list of tuples of adjacent words."""
    list = []
    for i in range(len(words) - 1):
        tuple = words[i], words[i+1]
        list.append(tuple)
    return list

def markov_chain(pairs):
    """Make a dictionary of markov chains."""
    word_dict = {}
    for pair in pairs:
        if pair[0] in word_dict.keys():
            if pair[1] in word_dict[pair[0]].keys():
                word_dict[pair[0]][pair[1]] += 1
            else:
                word_dict[pair[0]][pair[1]] = 1
        else:
            dict = {pair[1]: 1}
            word_dict[pair[0]] = Dictogram(dict)

    # for key in word_dict:
    #     word_dict[key] = Dictogram(word_dict[key])

    return word_dict

def get_count(words, target_word):
    count = 0
    for word in words:
        if word == target_word:
            count += 1

    return count

def second_order_markov_chain(pairs, markov):
    """"""
    word_dict = {}
    i = 0
    while i < len(pairs) - 1:
        if pairs[i] in word_dict.keys():
            i += 1
        else:
            word_dict[pairs[i]] = markov[pairs[i][1]]

    return word_dict

def walk(second_markov_chain, word_num):
    """"""
    sentences = []
    list_keys = list(second_markov_chain)
    rand_num = randrange(len(list_keys))
    # word1, word2 = list_keys[rand_num][0], list_keys[rand_num][1]
    tuple_word = list_keys[rand_num]
    sentences.append(tuple_word[0])
    sentences.append(tuple_word[1])
    # sentences.append(word2)
    for _ in range(word_num):
        word = second_markov_chain[tuple_word].sample()
        sentences.append(word)
        previous_word = tuple_word[1]
        print(tuple_word)
        del tuple_word
        tuple_word = previous_word, word

    return ' '.join(sentences)

def generate_sentences(markov_chain, word_num):
    sentences = []
    # return markov_chain
    list_keys = list(markov_chain)
    rand_num = randrange(len(list_keys))
    word = list_keys[rand_num]
    sentences.append(word)
    for _ in range(word_num):
        print(word)
        word = markov_chain[word].sample()
        print(word)
        sentences.append(word)

    return ' '.join(sentences)

# class Markov():
#     [START] = "[START]"
#     [STOP] = "[STOP]"
#
#     def __init__(self):
#         self.state = {}
#
#     def get_sentences(self, corpus):
#         """Split text into sentences"""
#         return sent_tokenize(corpus)
#
#     def get_words_with_start_stop_tokens(self, sentences):
#         list_words = []
#         for sentence in sentences:
#             words = sentence.split()
#             words.insert(0, "[START]")
#             words.append("[STOP]")
#             list_words.extend(words)
#
#         return list_words
#
#     def get_pairs(self, words):
#         """Make a list of tuples of adjacent words."""
#         list = []
#         for i in range(len(words) - 1):
#             tuple = words[i], words[i+1]
#             list.append(tuple)
#         return list
#
#     def markov_chain(self, pairs):
#         """Make a dictionary of markov chains."""
#         word_dict = {}
#         for pair in pairs:
#             if pair[0] in word_dict.keys():
#                 if pair[1] in word_dict[pair[0]].keys():
#                     word_dict[pair[0]][pair[1]] += 1
#                 else:
#                     word_dict[pair[0]][pair[1]] = 1
#             else:
#                 dict = {pair[1]: 1}
#                 word_dict[pair[0]] = Dictogram(dict)
#
#         # for key in word_dict:
#         #     word_dict[key] = Dictogram(word_dict[key])
#
#         return word_dict
#
#     def second_order_markov_chain(self, pairs, markov):
#         """"""
#         word_dict = {}
#         i = 0
#         while i < len(pairs) - 1:
#             if pairs[i] in word_dict.keys():
#                 i += 1
#             else:
#                 word_dict[pairs[i]] = markov[pairs[i][1]]
#
#         return word_dict
#
#     # def second_order_markov_chain(self, )
#     def generate_sentences(self, markov_chain):
#         sentences = []
#         print(markov_chain)
#         word = markov_chain["[START]""].sample()
#         tuple_word = "[START]", word
#         sentences.append(tuple_word[1])
#         list_keys = list(markov_chain)
#         while tuple_word[1] != "[STOP]":
#             word = markov_chain[tuple_word].sample()
#             sentences.append(word)
#             previous_word = tuple_word[1]
#             del tuple_word
#             tuple_word = previous_word, word
#
#         return ' '.join(sentences)


class MarkovChain(dict):
    def __init__(self, word_list=None):
        #intialize the super class
        super(MarkovChain, self).__init__()

        #if word list is passed, create a markov chain
        if word_list is not None:
            self.create_markov(word_list)


    def get_text(self, path = 'story.txt'):
        text = open_file(path)

        return text

    def create_markov(self, word_list):

        num_words = len(word_list)

        for index, key1 in enumerate(word_list):
            if num_words > index + 2:
                key2 = word_list[index + 1]
                word = word_list[index + 2]

                if (key1, key2) not in self:
                    self[(key1, key2)] = Dictogram([word])
                else:
                    self[(key1, key2)].add_count(word)


    def sentence(self, word_list, num_words):
        sentence = ""

        random_index = random.randint(0, len(word_list) - 1)
        key = (word_list[random_index], word_list[random_index + 1])

        while len(sentence) < num_words:

            word = self[key].sample()

            sentence += " " + word

            key = (key[1], word)

        return sentence

def run_generator():
    word_list = MarkovChain.get_text("story.txt")
    markov_chain = MarkovChain(word_list)
    return(markov_chain.sentence(word_list, 60))

if __name__ == "__main__":
    print(run_generator())

# if __name__ == "__main__":
#     # words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
#     words = open_file('story.txt').split()
#
#     # markov = Markov()
#     # sentences = markov.get_sentences(words)
#     # start_stop_tokens = markov.get_words_with_start_stop_tokens(sentences)
#     # print(start_stop_tokens)
#
#     # print(markov_chain(get_pairs(words)))
#     # print(markov.second_order_markov_chain(get_pairs(words), markov_chain(get_pairs(words))))
#     print(generate_sentences(second_order_markov_chain(get_pairs(words), markov_chain(get_pairs(words))), 20))
#     # pairs = get_pairs(words)
#     # markov = markov_chain(pairs)
#     # markov = second_order_markov_chain(pairs, markov)
#     # print(walk(markov, 20))
