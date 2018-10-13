correct_word = list("tiger")
user_shoot = 1

while user_shoot == 1:
    user_guess = input("Write your guess: ")
    user_guess = list(user_guess)

    if len(user_guess) > 5:
        print("To long word, hidden word got only 5 letter")
    if len(user_guess) == 5:

        # correct letter in good spot
        guess_word = user_guess
        for letter in range(0, len(correct_word)):

            if correct_word[letter] == user_guess[letter]:
                current_pass = ("[", user_guess[letter], "]")
                current_pass = "".join(current_pass)
                guess_word[letter] = current_pass

                # user_shoot = 1

        # print(current_pass)

        for letter in range(0, len(correct_word)):
            for another_letter in range(0, len(correct_word)):
                if user_guess[letter] == correct_word[another_letter]:
                    another_pass = ("(", user_guess[letter], ")")
                    another_pass = "".join(another_pass)
                    guess_word[letter] = another_pass
        print(guess_word)
