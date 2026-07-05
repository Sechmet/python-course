"""Tests for the XyzGame evaluate and evaluate_with_table methods."""

# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

import unittest
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from lesson05.rpsls import Rpsls
from lesson05.rpsls_game import RpslsGame

if TYPE_CHECKING:
    _Base = unittest.TestCase
else:
    _Base = object


class TestXyzGameEvaluateBase(ABC, _Base):
    """Abstract base class with shared test cases for both evaluate methods."""

    @abstractmethod
    def get_result(self, player_a: Rpsls, player_b: Rpsls) -> RpslsGame.Result:
        """Call the evaluation method under test."""

    # --- Tie cases ---

    def test_tie_rock(self):
        self.assertEqual(self.get_result(Rpsls.ROCK, Rpsls.ROCK), RpslsGame.Result.TIE)

    def test_tie_paper(self):
        self.assertEqual(
            self.get_result(Rpsls.PAPER, Rpsls.PAPER), RpslsGame.Result.TIE
        )

    def test_tie_scissors(self):
        self.assertEqual(
            self.get_result(Rpsls.SCISSORS, Rpsls.SCISSORS), RpslsGame.Result.TIE
        )

    def test_tie_lizard(self):
        self.assertEqual(
            self.get_result(Rpsls.LIZARD, Rpsls.LIZARD), RpslsGame.Result.TIE
        )

    def test_tie_spock(self):
        self.assertEqual(
            self.get_result(Rpsls.SPOCK, Rpsls.SPOCK), RpslsGame.Result.TIE
        )

    # --- Player A wins ---

    def test_rock_beats_scissors(self):
        self.assertEqual(
            self.get_result(Rpsls.ROCK, Rpsls.SCISSORS), RpslsGame.Result.PLAYER_A
        )

    def test_rock_beats_lizard(self):
        self.assertEqual(
            self.get_result(Rpsls.ROCK, Rpsls.LIZARD), RpslsGame.Result.PLAYER_A
        )

    def test_paper_beats_rock(self):
        self.assertEqual(
            self.get_result(Rpsls.PAPER, Rpsls.ROCK), RpslsGame.Result.PLAYER_A
        )

    def test_paper_beats_spock(self):
        self.assertEqual(
            self.get_result(Rpsls.PAPER, Rpsls.SPOCK), RpslsGame.Result.PLAYER_A
        )

    def test_scissors_beats_paper(self):
        self.assertEqual(
            self.get_result(Rpsls.SCISSORS, Rpsls.PAPER), RpslsGame.Result.PLAYER_A
        )

    def test_scissors_beats_lizard(self):
        self.assertEqual(
            self.get_result(Rpsls.SCISSORS, Rpsls.LIZARD), RpslsGame.Result.PLAYER_A
        )

    def test_lizard_beats_spock(self):
        self.assertEqual(
            self.get_result(Rpsls.LIZARD, Rpsls.SPOCK), RpslsGame.Result.PLAYER_A
        )

    def test_lizard_beats_paper(self):
        self.assertEqual(
            self.get_result(Rpsls.LIZARD, Rpsls.PAPER), RpslsGame.Result.PLAYER_A
        )

    def test_spock_beats_scissors(self):
        self.assertEqual(
            self.get_result(Rpsls.SPOCK, Rpsls.SCISSORS), RpslsGame.Result.PLAYER_A
        )

    def test_spock_beats_rock(self):
        self.assertEqual(
            self.get_result(Rpsls.SPOCK, Rpsls.ROCK), RpslsGame.Result.PLAYER_A
        )

    # --- Player B wins (mirrors of all Player A wins) ---

    def test_scissors_beats_rock_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.SCISSORS, Rpsls.ROCK), RpslsGame.Result.PLAYER_B
        )

    def test_lizard_beats_rock_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.LIZARD, Rpsls.ROCK), RpslsGame.Result.PLAYER_B
        )

    def test_rock_beats_paper_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.ROCK, Rpsls.PAPER), RpslsGame.Result.PLAYER_B
        )

    def test_spock_beats_paper_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.SPOCK, Rpsls.PAPER), RpslsGame.Result.PLAYER_B
        )

    def test_paper_beats_scissors_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.PAPER, Rpsls.SCISSORS), RpslsGame.Result.PLAYER_B
        )

    def test_lizard_beats_scissors_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.LIZARD, Rpsls.SCISSORS), RpslsGame.Result.PLAYER_B
        )

    def test_spock_beats_lizard_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.SPOCK, Rpsls.LIZARD), RpslsGame.Result.PLAYER_B
        )

    def test_paper_beats_lizard_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.PAPER, Rpsls.LIZARD), RpslsGame.Result.PLAYER_B
        )

    def test_scissors_beats_spock_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.SCISSORS, Rpsls.SPOCK), RpslsGame.Result.PLAYER_B
        )

    def test_rock_beats_spock_reversed(self):
        self.assertEqual(
            self.get_result(Rpsls.ROCK, Rpsls.SPOCK), RpslsGame.Result.PLAYER_B
        )

    # --- Invalid input ---

    def test_invalid_player_a_int(self):
        with self.assertRaises(AssertionError):
            self.get_result(1, Rpsls.ROCK)  # type: ignore[arg-type]

    def test_invalid_player_b_int(self):
        with self.assertRaises(AssertionError):
            self.get_result(Rpsls.ROCK, 1)  # type: ignore[arg-type]

    def test_invalid_both_int(self):
        with self.assertRaises(AssertionError):
            self.get_result(1, 2)  # type: ignore[arg-type]

    def test_invalid_none(self):
        with self.assertRaises(AssertionError):
            self.get_result(None, Rpsls.ROCK)  # type: ignore[arg-type]

    def test_invalid_str_rock(self):
        with self.assertRaises(AssertionError):
            self.get_result("ROCK", Rpsls.ROCK)  # type: ignore[arg-type]


class TestXyzGameEvaluate(TestXyzGameEvaluateBase, unittest.TestCase):
    """Tests for XyzGame.evaluate using if-statements."""

    def setUp(self):
        self.game = RpslsGame()

    def get_result(self, player_a, player_b):
        return self.game.evaluate(player_a, player_b)


class TestXyzGameEvaluateWithTable(TestXyzGameEvaluateBase, unittest.TestCase):
    """Tests for XyzGame.evaluate_with_table using the decision table."""

    def setUp(self):
        self.game = RpslsGame()

    def get_result(self, player_a, player_b):
        return self.game.evaluate_with_table(player_a, player_b)


if __name__ == "__main__":
    unittest.main()
