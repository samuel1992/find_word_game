import pytest

from game import Game
from word import Word


class TestGame:
    @pytest.mark.parametrize(
        'word, guessed_word, expected_len_of_hases',
        [
            ('ABCDE', 'ABCDE', (5,0,0)),
            ('ABCDE', 'FGHIJ', (0,5,0)),
            ('ABCDE', 'EDBCA', (0,0,5)),
            ('ABCDE', 'ZBEIY', (1,3,1)),
            ('ABCDE', 'AXYZA', (1,4,0)),
            ('ABADE', 'AXYZA', (1,3,1)),
        ]
    )
    def test_compare_words(self, word, guessed_word, expected_len_of_hases):
        """
        I tried to make all situations possible for the game logic:
        - having the same letters in the same position
        - having none of the letters
        - having the same letters but all in different positions
        - having some non existent letters, some in the same position, some in
          the different position
        """
        game = Game()
        word = Word(word)
        guessed_word = Word(guessed_word)

        game.compare_words(word, guessed_word)

        assert len(game.has_letters) == expected_len_of_hases[0]
        assert len(game.has_not_letters) == expected_len_of_hases[1]
        assert len(game.has_at_different_position_letters) == (
            expected_len_of_hases[2]
        )

    @pytest.mark.parametrize(
        'word, guessed_word, expected_string',
        [
            ('ABCDE', 'ABCDE', '+ + + + +'),
            ('ABCDE', 'FGHIJ', '- - - - -'),
            ('ABCDE', 'EDBCA', '| | | | |'),
            ('ABCDE', 'ZBEIY', '- + | - -'),
            ('ABCDE', 'AXYZA', '+ - - - -'),
            ('ABADE', 'AXYZA', '+ - - - |'),
        ]
    )
    def test_result_string(self, word, guessed_word, expected_string):
        game = Game()
        word = Word(word)
        guessed_word = Word(guessed_word)

        game.compare_words(word, guessed_word)

        assert game.result_string() == expected_string

    def test_found_the_word(self):
        game = Game()
        word = Word('testt')
        guessed_word = Word('testt')

        assert game.found_word(word, guessed_word)
