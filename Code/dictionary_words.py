import sys, random


# def get_sentence(num):
#     """Generate a sentence from random words."""
#     # list_words = []
#     file = open("/usr/share/dict/words", "r")
#     words = file.readlines()
#     file.close()
#     # for i in range(int(nums)):
#     #     word = random.choice(words).rstrip()
#     #     list_words.append(word)
#     #
#     # return " ".join(list_words)
#
#     list_words = [random.choice(words).rstrip() for i in range(int(num))]
#     return " ".join(list_words)
#
# if __name__ == "__main__":
#     nums = sys.argv[1]
#     print(get_sentence(nums))

# open the file and pick the words
# get sentence

def open_file(file_name):
    file = open(file_name, 'r')
    words = file.readlines()
    file.close()

    return words

def pick_word(file_name):
    word = random.choice(open_file(file_name)).rstrip()

    return word

def get_sentence(file_name, word_nums):
    list_words = []
    for i in range(int(word_nums)):
        list_words.append(pick_word(file_name))

    return " ".join(list_words)

if __name__ == "__main__":
    nums = sys.argv[1]
    print(get_sentence('/usr/share/dict/words', nums))
