import pytest

from game import Letter, Word, Game


@pytest.fixture
def word():
    myword = 'testt'
    word = Word(myword)
    return word


class TestLetter:
    def test_create_a_letter(self):
        letter = Letter('a', 0)
        assert letter


class TestWord:
    def test_create_a_word(self):
        word = Word('testt')
        assert word

    def test_word_must_have_5_letters(self):
        with pytest.raises(AssertionError):
            Word('abcdef')

    def test_build_letters(self):
        myword = 'testt'
        word = Word(myword)

        assert len(word.letters) == len(myword)
        for i, e in zip(myword, word.letters):
            assert i == e.value

    def test_word_has_letter_at_same_position(self, word):
        letter = Letter('t', 0)

        assert word.has_at_same_position(letter)

    def test_word_has_no_letter_at_same_position(self, word):
        letter = Letter('z', 0)

        assert not word.has_at_same_position(letter)

    def test_word_has_letter_at_different_position(self, word):
        letter = Letter('e', 0)

        assert word.has(letter)

    def test_word_has_no_letter_at_different_position(self, word):
        letter = Letter('z', 0)

        assert not word.has(letter)


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
