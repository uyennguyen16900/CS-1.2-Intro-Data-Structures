import sys, random


def get_sentence(num):
    list_words = []

    for i in range(int(nums)):
        word = random.choice(open("/usr/share/dict/words").readlines()).rstrip()
        list_words.append(word)

    return " ".join(list_words)


if __name__ == "__main__":
    nums = sys.argv[1]
    print(get_sentence(nums))
