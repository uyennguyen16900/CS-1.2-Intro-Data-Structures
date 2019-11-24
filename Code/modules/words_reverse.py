import sys

def reverse_words(words):
    i = -1
    list_words = []
    while i >= (len(words) * -1):
        list_words.append(words[i])
        i = i - 1

    return " ".join(list_words)


if __name__ == "__main__":
    params = sys.argv[1:]
    print(reverse_words(params))
