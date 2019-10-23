import sys, random

list_words = []

for word in sys.argv[1:]:
    list_words.append(word)

random.shuffle(list_words)
print(*list_words)
