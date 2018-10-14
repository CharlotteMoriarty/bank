def lexicon():
    words = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "år"}
    card = input("Translator : ..")

    if card in words:
        your_card = words[card]
        print(your_card)


lexicon()


def translator_english_to_swedish(english_words):
    words = {
        "merry": "God",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "år"}

    english = []
    word = ""

    for i in english_words:
        if i == " ":
            english.append(word)
            word = ""
        else:
            word += i
    return list(map(lambda trans: words[trans], english))


card = input("Write your christmas card: ")
#translator_english_to_swedish(card)

print(translator_english_to_swedish(card))





