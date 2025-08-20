I'm Raul Cuza and this is my CODE for SE_01

Today I tried to build the game HANGMAN!

The way I approached it is create a list of 10 words. The code would then pick one at random.

I then created a list named 'display' that contains '_'. Using a for command, every time the code detacts a letter in the 'random_word', a ('_') is added using the command append('_')

As it is a list and we don't want the players to be shown display as ["_',"_',"_',"_',"_'], I used the command : " ".join(display) to combine all the elements of the list into a single string. In order for the player to see each dash clearer I added a space between them " ".

'display' is then showed to the player, for example: in the form '_ _ _ _ _'. Now the player knows the word has 5 letters.

The player has 5 tries.

The player will then chose a letter. If the player writes something longer then a letter or a digit, a message saying that they're not allowed to introduce anything but a singular letter will be shown.

After a letter is selected, a for loop runs the guess trough every letter of random_word. If the letter is part of the word, the game will show the letter in the display like this: Example: random_word = apple, guess: a
display = a _ _ _ _

By running a for loop even if the letter appears multiple times in the word, the letter will be introduced in every space it appears. Example: apple, guess: p,
display = _ p p _ _

If the letter chosen isn't part of random_word, the player will try again and have one less try.

After each try, display will be shown for the player to keep track of how many letters are left and where the correct letters are in the word, once again using: 
" ".join(display)

If the word is guessed correctly after 5 tries or after display doesn't contain any more "_", the player won and its showed a congratulations message.

Else: the player is told they lost and shown the word.

