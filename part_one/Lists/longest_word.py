def find_longest_word():

    words_bank = ["tea", "time", "cat", "computer", "largest_word"]

    print(list(map(lambda x: (len(x), x), words_bank))[-1][-1])


find_longest_word()
