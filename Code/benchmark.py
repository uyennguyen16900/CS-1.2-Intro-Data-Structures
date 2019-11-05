import timeit
# maybe make this an offical test file :)

# from sys import argv

#
# stmt = "histogram_list(words.txt)"
# setup = "from histogram import histogram_list"
# timer_list = timeit.Timer(stmt, setup=setup)
#
# stmt = "histogram_tuple(words.txt)"
# setup = "from histogram import histogram_tuple"
# timer_tuple = timeit.Timer(stmt, setup=setup)
#
# stmt = "histogram_dictionary(words.txt)"
# setup = "from histogram import histogram_dictionary"
# timer_dictionary = timeit.Timer(stmt, setup=setup)
#
#
# # iterations = int(argv[1])
# result = round(timer_list.timeit(number=1) * 1000 / iterations)
# print("Average time for histogram_list: " + str(timer_list) + " ms")
#
# result = round(timer_tuple.timeit(number=1) * 1000 / iterations)
# print("Average time for histogram_tuple: " + str(histogram_tuple) + " ms")
#
# result = round(timer_dictionary.timeit(number=1) * 1000 / iterations)
# print("Average time for histogram_dictionary: " + str(histogram_dictionary) + " ms")


print("Average time for histogram_list: " + timeit.Timer(setup = "from histogram import histogram_list", stmt = "histogram_list(words.txt)").timeit(number=1000) * 1000 / 1000)
print("Average time for histogram_tuple: " + timeit.Timer(setup = "from histogram import histogram_tuple", stmt = "histogram_tuple(words.txt)").timeit(number=1000) * 1000 / 1000)
print("Average time for histogram_dictionary: " + timeit.Timer(setup = "from histogram import histogram_dictionary", stmt = "histogram_dictionary(words.txt)").timeit(number=1000) * 1000 / 1000)
