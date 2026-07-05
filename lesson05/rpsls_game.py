"""RpslsGame module for Rock Paper Scissors Lizard Spock."""

from __future__ import annotations

from enum import IntEnum, auto

from lesson05.rpsls import Rpsls


class RpslsGame:
    """Xyz Game"""

    class Result(IntEnum):
        """Result of an evaluation"""

        TIE = auto()
        PLAYER_A = auto()
        PLAYER_B = auto()

    def evaluate(self, player_a: Rpsls, player_b: Rpsls) -> RpslsGame.Result:
        """Evaluates a game of Xyz."""

        assert isinstance(player_a, Rpsls), player_a
        assert isinstance(player_b, Rpsls), player_b

        if player_a == player_b:
            return RpslsGame.Result.TIE

        if Rpsls.ROCK == player_a and Rpsls.SCISSORS == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.ROCK == player_a and Rpsls.LIZARD == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.PAPER == player_a and Rpsls.ROCK == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.PAPER == player_a and Rpsls.SPOCK == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.SCISSORS == player_a and Rpsls.PAPER == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.SCISSORS == player_a and Rpsls.LIZARD == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.LIZARD == player_a and Rpsls.SPOCK == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.LIZARD == player_a and Rpsls.PAPER == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.SPOCK == player_a and Rpsls.SCISSORS == player_b:
            return RpslsGame.Result.PLAYER_A

        if Rpsls.SPOCK == player_a and Rpsls.ROCK == player_b:
            return RpslsGame.Result.PLAYER_A

        return RpslsGame.Result.PLAYER_B

    def evaluate_with_table(
        self,
        player_a: Rpsls,
        player_b: Rpsls
    ) -> RpslsGame.Result:

        """Evaluates a game of Xyz using a 5x5 decision table."""

        assert isinstance(player_a, Rpsls), player_a
        assert isinstance(player_b, Rpsls), player_b

        # Decision table: table[player_a][player_b] -> Result
        # Rows: ROCK, PAPER, SCISSORS, LIZARD, SPOCK
        # Cols: ROCK, PAPER, SCISSORS, LIZARD, SPOCK
        A = RpslsGame.Result.PLAYER_A
        B = RpslsGame.Result.PLAYER_B
        T = RpslsGame.Result.TIE

        table = {
            Rpsls.ROCK: {
                Rpsls.ROCK: T,
                Rpsls.PAPER: B,
                Rpsls.SCISSORS: A,
                Rpsls.LIZARD: A,
                Rpsls.SPOCK: B,
            },
            Rpsls.PAPER: {
                Rpsls.ROCK: A,
                Rpsls.PAPER: T,
                Rpsls.SCISSORS: B,
                Rpsls.LIZARD: B,
                Rpsls.SPOCK: A,
            },
            Rpsls.SCISSORS: {
                Rpsls.ROCK: B,
                Rpsls.PAPER: A,
                Rpsls.SCISSORS: T,
                Rpsls.LIZARD: A,
                Rpsls.SPOCK: B,
            },
            Rpsls.LIZARD: {
                Rpsls.ROCK: B,
                Rpsls.PAPER: A,
                Rpsls.SCISSORS: B,
                Rpsls.LIZARD: T,
                Rpsls.SPOCK: A,
            },
            Rpsls.SPOCK: {
                Rpsls.ROCK: A,
                Rpsls.PAPER: B,
                Rpsls.SCISSORS: A,
                Rpsls.LIZARD: B,
                Rpsls.SPOCK: T,
            },
        }

        return table[player_a][player_b]
