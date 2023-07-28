# Guess Game Small Project

# Sample Questions and Options
Questions = {
    "What is the capital of France?": "A",
    "Which planet is known as the Red Planet?": "B",
    "What is the largest mammal in the world?": "C",
}

options = [
    ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"],
]

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in Questions:
        question_num += 1
        print("__________________________________")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(Questions.get(key), guess)

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT! ")
        return 1
    else:
        print("WRONG! ")
        return 0

def display_score(correct_guesses, guesses):
    print("__________________________________")
    print("RESULTS ")
    print("__________________________________")

    print("Answer: ", end=" ")
    for key in Questions:
        print(Questions.get(key), end=" ")
    print()

    print("Guesses: ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

new_game()

# Rock Paper and Scissor Game
import random
while True:

    choices =["rock","paper","scissor"]

    computer = random.choice(choices)
    player = None
    while   player not in choices:
        player = input("rock,paper or scissor?").lower()
    if player == computer:
        print("computer: ",computer)
        print("Player: ",player)
        print("Tie! ")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("Player: ",player)
            print("You lose😢! ")
        if computer == "scissor":
            print("computer: ",computer)
            print("Player: ",player)
            print("You Win🙌! ")
    elif player == "scissor":
        if computer == "rock":
            print("computer: ",computer)
            print("Player: ",player)
            print("You lose😢! ")
        if computer == "paper":
            print("computer: ",computer)
            print("Player: ",player)
            print("You Win🙌! ")
    elif player == "paper":
        if computer == "scissor":
            print("computer: ",computer)
            print("Player: ",player)
            print("You lose😢! ")
        if computer == "rock":
            print("computer: ",computer)
            print("Player: ",player)
            print("You Win🙌! ")
    play_again = input("You want to Play again,(yes/no)")
    if play_again != "yes":
        break
print("Bye!")


