def lexicon():
    words = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "år"}
    card = input("Write your christmas card")

    if card in words:
        your_card = words[card]
        print(your_card)


lexicon()