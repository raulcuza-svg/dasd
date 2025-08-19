secret = "apple"
tries = 6

print("Guess the 5-letter word. You have 6 tries.")
print("Uppercase = correct letter & position, lowercase = correct letter wrong position, _ = not in word")

while tries > 0:
    guess = input("Your guess: ").lower()
    if len(guess) != 5:
        print("Enter exactly 5 letters.")
        continue
    if guess == secret:
        print("You win!")
        break

    feedback = ""
    for i in range(5):
        if guess[i] == secret[i]:
            feedback += guess[i].upper()
        elif guess[i] in secret:
            feedback += guess[i].lower()
        else:
            feedback += "_"
    print("Feedback:", feedback)

    tries -= 1

if tries == 0:
    print("Game over! The word was:", secret)