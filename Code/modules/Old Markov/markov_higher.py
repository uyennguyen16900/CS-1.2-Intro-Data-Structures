from nltk.tokenize import sent_tokenize
from random import randrange
from dictogram import Dictogram
from dictionary_words import open_file
import random
# text = "God is Great! I won a lottery. Mr. Nguyen is awesome."
# print(sent_tokenize(text))

class Markov():
    def __init__(self, word_file, n):
        self.word_list = open_file(word_file)
        self.n = n
        self.markov = self.make_chain(self.get_words_with_start_stop_tokens(self.get_sentences()))

    def get_sentences(self):
        """Split text into sentences"""
        return sent_tokenize(self.word_list)

    def get_words_with_start_stop_tokens(self, sentences):
        list_words = []
        for sentence in sentences:
            words = sentence.split()
            words.insert(0, "[START]")
            words.append("[STOP]")
            list_words.extend(words)

        return list_words

    # def get_pairs(self, words):
    #     """Make a list of tuples of adjacent words."""
    #     list = []
    #     for i in range(len(words) - 1):
    #         tuple = words[i], words[i+1]
    #         list.append(tuple)
    #     return list

    def make_chain(self, word_list):
        """Create and return a markov chain from a given list of words"""
        markov = {}
        q = Queue()
        for i in range(len(word_list)):
            if i < self.n:
                q.enqueue(word_list[i])
            else:
                key = str(q)
                q.dequeue()
                q.enqueue(word_list[i])
                if markov.get(key) is None:
                    markov[key] = []
                markov[key].append(str(q))

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    # def second_order_markov_chain(self, pairs, markov):
    #     """"""
    #     word_dict = {}
    #     i = 0
    #     while i < len(pairs) - 1:
    #         if pairs[i] in word_dict.keys():
    #             i += 1
    #         else:
    #             word_dict[pairs[i]] = markov[pairs[i][1]]
    #
    #     return word_dict

    # def second_order_markov_chain(self, )
    # def generate_sentences(self):
    #     sentences = []
    #     print(markov_chain)
    #     word = markov_chain["[START]""].sample()
    #     tuple_word = "[START]", word
    #     sentences.append(tuple_word[1])
    #     list_keys = list(markov_chain)
    #     while tuple_word[1] != "[STOP]":
    #         word = markov_chain[tuple_word].sample()
    #         sentences.append(word)
    #         previous_word = tuple_word[1]
    #         del tuple_word
    #         tuple_word = previous_word, word
    #
    #     return ' '.join(sentences)

if __name__ == '__main__':
    markov = Markov('story.txt', 20)
    print(markov.markov)
