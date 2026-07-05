"""Rock Paper Scissors Lizard Spock interactive game."""

from __future__ import annotations

import sys
import random
from enum import StrEnum

from lesson05.rpsls import Rpsls
from lesson05.rpsls_game import RpslsGame

prompt = []
prompt.append("Enter:")

for i in Rpsls:
    prompt.append(f"{i.value} for {i.name}")
prompt.append("\n")

print("")
player_choice = input("\n".join(prompt))

values_as_string = [str(i.value) for i in Rpsls]
OPTIONS = ", ".join(values_as_string)
STATUS = f"You must enter: {OPTIONS}"

if not player_choice.isdigit() or player_choice not in values_as_string:
    sys.exit(STATUS)

player = int(player_choice)
computer_choice = random.choice("".join(values_as_string))
assert computer_choice.isdigit(), computer_choice

computer = int(computer_choice)

print("")
print(f"You chose '{Rpsls(player).name}'.")
print(f"Python chose '{Rpsls(computer).name}'.")
print("")


class WinMessage(StrEnum):
    """Message that describes who wins."""

    PLAYER = "🎉 You win! 💕"
    COMPUTER = "🐍 Python wins!"
    TIE = "😲 Tie game!"


game = RpslsGame()
result = game.evaluate(Rpsls(player), Rpsls(computer))

if RpslsGame.Result.PLAYER_A == result:
    print(WinMessage.PLAYER)
elif RpslsGame.Result.PLAYER_B == result:
    print(WinMessage.COMPUTER)
else:
    print(WinMessage.TIE)
