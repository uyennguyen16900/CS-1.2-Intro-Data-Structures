from random import randrange
from dictogram import Dictogram
from dictionary_words import open_file

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
            word_dict[pair[0]] = dict

    for key in word_dict:
        word_dict[key] = Dictogram(word_dict[key])

    return word_dict

def second_order_markov_chain(pairs):
    """"""
    word_dict = {}
    for pair in pairs:
        for tuple in tuples:
            if pair in word_dict.keys():
                if pair[1] == tuple[0]:
                    word_dict[pair][pair[1]] += 1
                else:
                    word_dict[pair][pair[1]] = 1

            else:
                dict = {pair[1]: 1}
                word_dict[pair] = dict

    return word_dict


def generate_sentences(markov_chain, word_num):
    sentences = []
    list_keys = list(markov_chain)
    rand_num = randrange(len(list_keys))
    sentences.append(list_keys[rand_num])
    for i in range(word_num):
        sentences.append(markov_chain[sentences[i]].sample())

    return ' '.join(sentences)


if __name__ == "__main__":
    # words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    words = open_file('words.txt')
    print(markov_chain(get_pairs(words)))
    # print(second_order_markov_chain(get_pairs(words)))
    print(generate_sentences(markov_chain(get_pairs(words)), 20))
