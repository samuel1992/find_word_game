from dataclasses import dataclass

from choose_word import choose_word


@dataclass
class Letter:
    value: str
    position: int


class Word:
    def __init__(self, word):
        assert len(word) == 5

        self.letters = [Letter(value=letter, position=position)
                        for position, letter in enumerate(word)]

    def has(self, letter):
        letter_values = [l.value for l in self.letters]

        return letter.value in letter_values

    def has_at_same_position(self, letter):
        return self.letters[letter.position] == letter


class Game:
    def __init__(self):
        self.has_letters = []
        self.has_not_letters = []
        self.has_at_different_position_letters = []

    def compare_words(self, word, guessed_word):
        for letter in guessed_word.letters:
            if word.has(letter) and word.has_at_same_position(letter):
                self.has_letters.append(letter)
            elif word.has(letter):
                self.has_at_different_position_letters.append(letter)
            else:
                self.has_not_letters.append(letter)
