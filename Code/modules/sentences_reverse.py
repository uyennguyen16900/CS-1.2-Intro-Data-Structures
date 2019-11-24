import sys, random

def reverse_sentences(sentences):
    sentences_reversed = []
    copy_sentences = sentences.split('.')
    copy_sentences.pop(-1)
    length = len(copy_sentences)

    for i in range(length):
        rand_num = random.randrange(copy_sentences)
        sentences_reversed.append(copy_sentences[rand_num].strip())
        copy_sentences.pop(rand_num)

    return ". ".join(sentences_reversed) + "."


if __name__ == "__main__":
    sentences = "Hello. My name is Uyen. I'm a junior at Make School. I'm Vietnamese."
    # params = sys.argv[1:]
    print(reverse_sentences(sentences))
