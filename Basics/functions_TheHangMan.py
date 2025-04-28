import random
from functions_TheHangMan_Wordslist import words

# Dictionary of key:()
# to print forward slah, \\
hangman_art = {0 : ("   ",
                   "   ",
                   "   "),
              1 : (" o ",
                   "   ",
                   "   "),
              2 : (" o ",
                   " | ",
                   "   "),
              3 : (" o ",
                   "/| ",
                   "   "),
              4 : (" o ",
                   "/|\\",
                   "   "),
              5 : (" o ",
                   "/|\\",
                   "/  "),
              6 : (" o ",
                   "/|\\",
                   "/ \\")}

def dispaly_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrongguesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        dispaly_man(wrongguesses)
        display_hint(hint)
        guess = input("Enter a letter : ").lower()
    
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already gussed")
            continue

        guessed_letters.add(guess)
 
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrongguesses += 1

        if '_' not in hint:
            dispaly_man(wrongguesses)
            display_answer(answer)
            print("You won")
            is_running = False
        elif wrongguesses  >= len(hangman_art) - 1:
            dispaly_man(wrongguesses)
            print("The answer is : ", end="")
            display_answer(answer)
            print("You lost")
            is_running = False



if __name__ == "__main__":
    main()