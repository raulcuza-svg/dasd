import random

words = ["apple", "shame", "german", "ghost", "tractor", "hangman", "shark", "slot", "flame", "brick"]
tries = 5

print("Welcome to HANGMAN! Find out the word or phrase by guessing one letter at a time. But be careful. You can only guess 5 letters incorrectly")


random_word = random.choice(words)
display = []
for _ in random_word:
    display.append("_")

print(" ".join(display))

while tries > 0 and "_" in display:
    guess = input("Enter a letter: ").lower()

    if len(guess)!= 1 or guess.isdigit():
        print("Please enter a single letter. Not multiple or a number")
        continue

    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                display[i] = guess
        print("Good job! The letter is in the word.")
    else:
        tries = tries - 1
        print(f"Wrong guess. You have {tries} tries left.")

    print(" ".join(display))

if "_" not in display:
    print("Congratulations! You won!")
else:
    print(f"Game over! The word was: {random_word}")




    



