# Modules
import random
from string import ascii_lowercase


def play_hangman():
    # Setup
    words = ["python", "java", "kotlin", "javascript"]
    random.seed()
    random_word = random.choice(words)
    lives = 8

    correct_answer = tuple(random_word)
    user_answers = set()
    hidden_word = ["-" for char in random_word]
    hidden_word = "".join(hidden_word)
    current_string = hidden_word

    has_won = False
    is_playing = True

    # Game Loop
    while is_playing:
        # Input
        print()
        print(hidden_word)
        print("Input a letter: ", end="")
        guess = input()

        # Errors
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if guess not in ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue
        if guess in user_answers:
            print("You've already guessed this letter")
            continue

        if guess not in user_answers:
            user_answers.add(guess)

        if guess not in correct_answer:
            print("That letter doesn't appear in the word")
            lives -= 1
        else:
            if guess not in hidden_word:
                new_string = ""
                index = 0
                for _ in range(len(correct_answer)):
                    if hidden_word[index] == "-":
                        if guess == correct_answer[index]:
                            new_string += guess
                        else:
                            new_string += "-"
                    else:
                        new_string += current_string[index]
                    index += 1

                hidden_word = new_string
                current_string = hidden_word
            else:
                print("No improvements")

        # Conditions
        if hidden_word.count("-") <= 0:
            print("You guessed the word!")
            is_playing = False
            has_won = True
        if lives <= 0:
            is_playing = False
            has_won = False

    # Victory condition
    if has_won:
        print("You survived!")
    else:
        print("You lost!")


# Entry
is_running = True

while is_running:
    print("H A N G M A N")
    print("Type \"play\" to play the game, \"exit\" to quit: ", end="")
    user_input = input()
    if user_input == "play":
        play_hangman()
    elif user_input == "exit":
        is_running = False
