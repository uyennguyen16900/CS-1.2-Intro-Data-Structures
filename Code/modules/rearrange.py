import sys, random


def rearrange(words):
    """Rearrange words"""
    list_words = []
    copy_words = words.copy()

    for i in range(len(words)):
        rand_index = random.randrange(len(copy_words))
        list_words.append(copy_words[rand_index])
        copy_words.pop(rand_index)

    return " ".join(list_words)


if __name__ == "__main__":
    params = sys.argv[1:]
    print(rearrange(params))
