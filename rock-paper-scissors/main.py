from random import randint


header = "=" * 50


def get_player_choice():
    error = True
    while error:
        error = False
        print("Hello, pick your choice by typing the number")
        print("[1]: Rock")
        print("[2]: Paper")
        print("[3]: Scissors")
        choice = input("choice: ")
        try:
            choice = int(choice)
            if not 1 <= choice <= 3:
                error = True
        except ValueError:
            error = True

        if error:
            print(header)
            print(f"You must pick an option 1, 2, or 3 - you picked {choice}")
            print("Try Again.")
            print(header)

    print(header)
    return choice


def get_computer_choice():
    return randint(1, 3)


round = 1
player_wins = 0
computer_wins = 0
while player_wins < 3 and computer_wins < 3:
    print(f"============= Round {round} =============")
    print(f"=== player [{player_wins}] vs computer [{computer_wins}] ===")
    round += 1
    player = get_player_choice()
    computer = get_computer_choice()

    # tie
    if player == computer:
        print("It's a tie!")

    # player wins: rock vs scissors
    if player == 1 and computer == 3:
        print("You win! the computer picked scissors")
        player_wins += 1

    # player loses: rock vs paper
    if player == 1 and computer == 2:
        print("You lose! the computer picked paper")
        computer_wins += 1

    # player wins: paper vs rock
    if player == 2 and computer == 1:
        print("You win! the computer picked rock")
        player_wins += 1

    # player loses: paper vs scissors
    if player == 2 and computer == 3:
        print("You lose! the computer picked scissors")
        computer_wins += 1

    # player wins: scissors vs paper
    if player == 3 and computer == 2:
        print("You win! the computer picked scissors")
        player_wins += 1

    # player loses: scissors vs rock
    if player == 3 and computer == 1:
        print("You lose! the computer picked rock")
        computer_wins += 1


print(header)
if player_wins > computer_wins:
    print("YOU WON!!")
else:
    print("YOU LOST!!")

print(f"final score is player {player_wins} and computer {computer_wins}")
