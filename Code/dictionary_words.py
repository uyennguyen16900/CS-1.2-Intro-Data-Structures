import sys, random

nums = sys.argv[1]
list_words = []

for i in range(int(nums)):
    word = random.choice(open("/usr/share/dict/words").readlines()).rstrip()
    list_words.append(word)

print(*list_words)
