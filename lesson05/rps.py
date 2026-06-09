import sys
import random
from enum import Enum, IntEnum, auto

long_line = "This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. This is a very long line. "


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RPS_BETTER(IntEnum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()
    # WELL = auto()


print("")
playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

# player_choice = "Enter ...\n"
# for item in RPS:
#     player_choice = f"{player_choice}{item.value} for {item.name},\n"
# player_choice = f"{player_choice}\n"

player = int(playerchoice)

# allowed_values = [item.value for item in RPS]
# if player not in allowed_values:
#     sys.exit(f"You must enter one of these values: {allowed_values}")

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS .", "") + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win! 💕")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")
