import pytest

from word import Letter, Word


@pytest.fixture
def word():
    myword = 'testt'
    word = Word(myword)
    return word


class TestLetter:
    def test_create_a_letter(self):
        letter = Letter('a', 0)
        assert letter

    def test_letters_with_accents(self):
       letter = Letter('ã', 0)
       another = Letter('a', 0)

       assert letter == another
       assert letter in [another]

       letter = Letter('é', 0)
       another = Letter('e', 0)

       assert letter == another
       assert letter in [another]

    def test_letter_set_to_correct(self):
        letter = Letter('a', 0)
        letter.set_to_correct()

        assert letter.correct


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

    def test_word_has_letter(self, word):
        letter = Letter('e', 0)

        assert word.has(letter)

    def test_word_has_no_letter(self, word):
        letter = Letter('z', 0)

        assert not word.has(letter)

    def test_word_has_letter_at_same_position(self, word):
        letter = Letter('t', 0)

        assert word.has_at_same_position(letter)

    def test_word_has_no_letter_at_same_position(self, word):
        letter = Letter('z', 0)

        assert not word.has_at_same_position(letter)
