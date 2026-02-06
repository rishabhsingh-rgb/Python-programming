import random
hangman = [r'''          
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
❤️
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
❤️ ❤️
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
❤️ ❤️ ❤️
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
❤️ ❤️ ❤️ ❤️
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
❤️ ❤️ ❤️ ❤️ ❤️
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
❤️ ❤️ ❤️ ❤️ ❤️ ❤️
  +---+
  |   |
      |
      |
      |
      |
=========''']
word_list = ['python', 'java', 'kohli', 'thala', 'sachin', 'coding', 'hangman', 'school','lamp','camera','laptop','brush','paint','home']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives = 6

print("\nWelcome to Hangman!🤗")
print(f"\nYou have {lives} ❤️  lives to guess the word.")
print("The word has", word_length, "letters.")
display = ['_'] * word_length
print(display)
while not game_over:
    guess = input("Guess a letter 🤔: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life 💔.")
        if lives == 0:
            game_over = True
            print("You lose 😭.\nThe word was " + chosen_word)
    if '_' not in display:
        game_over = True
        print("You win! 🎉")
    print(hangman[lives])