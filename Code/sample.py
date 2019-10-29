def stochastic_sampling(words):
    length = len(words)
    dict = {}
    for word in words:
        dict[word] = words.count(word)

    return dict

words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
print(stochastic_sampling(words))
