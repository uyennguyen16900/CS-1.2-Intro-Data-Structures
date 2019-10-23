import sys, random


def get_sentence(num):
    """Generate a sentence from random words."""
    list_words = []
    file = open("/usr/share/dict/words", "r")
    words = file.readlines()
    file.close()
    for i in range(int(nums)):
        word = random.choice(words).rstrip()
        list_words.append(word)

    return " ".join(list_words)


if __name__ == "__main__":
    nums = sys.argv[1]
    print(get_sentence(nums))
