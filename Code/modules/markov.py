from .queue import *
from .dictogram import *
from .histogram import *
from random import choice
from .dictionary_words import open_file


class SecondOrderMarkovChain():
    def __init__(self, word_file, n):
        self.word_list = open_file(word_file)
        self.n = n
        self.markov = self.make_chain(self.word_list)

    def make_chain(self, word_list):
        queue = Queue()
        markov = {}
        n = self.n
        if queue.length() == 0:
            for i in range(n):
                queue.enqueue(word_list[i])
        for words in word_list:
            key = str(queue)
            queue.enqueue(words)
            queue.dequeue()

            if key not in markov:
                markov[key] = []
            markov[key].append(str(queue))

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    def generate_sentences(self):
        output = []
        output.append(choice(tuple(self.markov.keys())))

        while output[0][0].islower():
            output[0] = choice(tuple(self.markov.keys()))
        i = 0
        while output[-1][-1] != ".":
            output.append(self.markov[output[i]].sample())
            i += 1

        string = ""
        for word in output:
            if output.index(word) == 0:
                string += word + " "
            else:
                string += word.split()[-1] + " "
        return string

if __name__ == '__main__':
    # words = open_file().split()

    markov = SecondOrderMarkovChain('dan-brown.txt', 20)
    print(markov.generate_sentences())
