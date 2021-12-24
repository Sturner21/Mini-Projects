print("Welcome to text based Hang-man!")

hangman_pics = ["""
+---+
    |
    |
    |
   ===""", """
+---+
0   |
    |
    |
   ==="""]

print(hangman_pics)

word = input("Player 1, please enter in what you would like Player 2 to guess:")
for i in range(0, 45):
    print("#")
rletters = list(word.strip())
guesses = 8
board = ["-"] * len(word)
print("Player 2, you have {} guesses before you are hung.".format(guesses))
print(board)
guessed = []
while guesses > 0:
    if "-" not in board:
        print("Player 2 wins!")
        break
    msg = "Guess a letter:"
    char = input(msg)
    if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = "#"
    else:
        guesses -= 1
        guessed.append(char)
    
    print("You have {} guesses remaining!".format(guesses))
    print(board)
    print("Letters already guessed:", guessed)
if guesses == 0:
    print("Player 1 wins!")
    print("The correct word was {}".format(word))