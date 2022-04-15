import pytest

from game import Letter, Word


@pytest.fixture
def word():
    myword = 'test'
    word = Word(myword)
    word.build()
    return word


class TestLetter:
    def test_create_a_letter(self):
        letter = Letter('a', 0)
        assert letter


class TestWord:
    def test_create_a_word(self):
        word = Word('test')
        assert word

    def test_build_letters(self):
        myword = 'test'
        word = Word(myword)
        word.build()

        assert len(word.letters) == len(myword)
        for i, e in zip(myword, word.letters):
            assert i == e.value

    def test_word_has_letter(self, word):
        letter = Letter('t', 0)

        assert word.has(letter)

    def test_word_has_no_letter(self, word):
        letter = Letter('z', 0)

        assert not word.has(letter)

    def test_word_has_letter_on_same_position(self, word):
        letter = Letter('t', 0)

        assert word.same_position(letter)

    def test_word_has_no_letter_on_same_position(self, word):
        letter = Letter('z', 0)

        assert not word.same_position(letter)
