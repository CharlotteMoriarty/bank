words = {
        "merry": "God",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "år"
        }


def lexicon():
    single_word = input("Translator : ..")
    if single_word in words:
        your_word = words[single_word]
        print(your_word)


def translator_english_to_swedish(english_words):
    english = []
    word = ""
    for i in english_words:
        if i == " ":
            english.append(word)
            word = ""
        else:
            word += i
    return list(map(lambda trans: words[trans], english))


def english_swedish():
    translator_version = input("Write A for single word translation or B for sentence translation")
    if translator_version == "A" :
        lexicon()
    elif translator_version == "B":
        card = input("Write your christmas card: ")
        print(translator_english_to_swedish(card))


english_swedish()
