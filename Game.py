secret_word="salt"
guess = ""
guess_count = 0
guess_limit = 3
Out_of_guesses = False

print("Hint : Without this ingredient your meal will not have a taste")

while guess!= secret_word and not(Out_of_guesses):
        if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        Out_of_guesses = True
if Out_of_guesses:
    print("Out Of guesses, You Lose !")
else:
    print("You Win!!!")