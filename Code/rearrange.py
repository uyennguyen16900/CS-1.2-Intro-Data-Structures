import sys, random


def rearrange(words):
    list_words = []

    for word in words:
        list_words.append(word)

    random.shuffle(list_words)
    return " ".join(list_words)


if __name__ == "__main__":
    params = sys.argv[1:]
    print(rearrange(params))
