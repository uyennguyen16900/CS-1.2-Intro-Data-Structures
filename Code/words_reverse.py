import sys

i = -1
list_words = []
while i >= (len(sys.argv[1:]) * -1):
    list_words.append(sys.argv[1:][i])
    i = i - 1

print(*list_words)
