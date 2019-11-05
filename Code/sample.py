import histogram
import random
# To many if statment for a main
# test file or a function :)
def stochastic_sampling(histogram):
    """Return a random word by frequency"""
    tokens = sum(histogram.values())
    num = 0
    dart = random.randrange(tokens)
    for k, v in histogram.items():
        num += v
        if dart < num:
            return k

if __name__ == "__main__":
    # print(stochastic_sampling(histogram.histogram_dictionary("words.txt")))
    count = 0
    count_t = 0
    count_f = 0
    count_o = 0
    count_g = 0
    count_b = 0
    count_r = 0
    for i in range(10000):
        word = stochastic_sampling(histogram.histogram_dictionary("words.txt"))
        if word == "fish":
            count_f += 1
        elif word == "green":
            count_g += 1
        elif word == "one":
            count_o += 1
        elif word == "two":
            count_t += 1
        elif word == "blue":
            count_b += 1
        else:
            count_r += 1

    print(f'Fish: {count_f}\nGreen: {count_g}\nOne: {count_o}\nTwo: {count_t}\nRed: {count_r}\nBlue: {count_b}')
